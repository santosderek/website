import { fireEvent, render, screen, waitFor, within } from '@testing-library/react';
import { MemoryRouter } from 'react-router-dom';
import { describe, expect, it, vi } from 'vitest';

import App from './App.jsx';

const resumePayload = {
  career: [{ title: 'Full-Stack Software Engineer', date: 'Now', location: 'Raleigh', descriptions: ['Builds things'] }],
  education: [{ title: 'NC State', date: '2016', degree: 'Computer Science', relevantCourses: ['Algorithms'], additional: [] }],
  leadership: [],
  repos: [{ title: 'Website', subtitle: 'Portfolio', description: 'Personal site', url: '/project/santosderek' }],
  skills: { technologies: [['Python', 5]], tools: [['Docker', 4]] },
};

function mockFetch() {
  global.fetch = vi.fn((path) => {
    if (path === '/api/v1/resume') {
      return Promise.resolve({ ok: true, json: () => Promise.resolve(resumePayload) });
    }
    if (path === '/api/v1/github/user') {
      return Promise.resolve({ ok: true, json: () => Promise.resolve({ public_repos: 42 }) });
    }
    return Promise.resolve({ ok: false, status: 404, json: () => Promise.resolve({}) });
  });
}

async function openPanel(name) {
  const sidebar = await screen.findByLabelText('Portfolio sections');
  fireEvent.click(within(sidebar).getByText(name));
}

describe('App', () => {
  it('renders the TUI workspace and API-backed panels', async () => {
    mockFetch();
    render(<MemoryRouter initialEntries={['/']}><App /></MemoryRouter>);

    await waitFor(() => expect(screen.getAllByText('Full-Stack Software Engineer').length).toBeGreaterThan(0));
    expect(screen.getByText('DEREK.OS // PORTFOLIO.EXE')).toBeInTheDocument();

    await openPanel('Projects');
    expect(await screen.findByText('Website')).toBeInTheDocument();
    expect(await screen.findByText('...and 42 more on github!')).toBeInTheDocument();

    await openPanel('Skills');
    expect(screen.getAllByText('Python').length).toBeGreaterThan(0);
  });

  it('toggles mobile navigation without Bootstrap JavaScript', () => {
    mockFetch();
    render(<MemoryRouter initialEntries={['/']}><App /></MemoryRouter>);

    const toggle = screen.getByRole('button', { name: /toggle navigation/i });
    expect(toggle).toHaveAttribute('aria-expanded', 'false');

    fireEvent.click(toggle);

    expect(toggle).toHaveAttribute('aria-expanded', 'true');
    expect(document.querySelectorAll('.navbar-collapse.show')).toHaveLength(2);
  });

  it('opens command palette from keyboard shortcut', async () => {
    mockFetch();
    render(<MemoryRouter initialEntries={['/']}><App /></MemoryRouter>);

    fireEvent.keyDown(window, { key: 'k', ctrlKey: true });

    expect(screen.getByRole('dialog', { name: /command palette/i })).toBeInTheDocument();
    expect(screen.getByPlaceholderText('> search site...')).toBeInTheDocument();
  });

  it('filters project cards by selected skill', async () => {
    mockFetch();
    render(<MemoryRouter initialEntries={['/']}><App /></MemoryRouter>);

    await openPanel('Skills');
    fireEvent.click(screen.getByRole('button', { name: 'Python' }));
    await openPanel('Projects');

    expect(await screen.findByText('Website')).toBeInTheDocument();
    expect(screen.getByText('Website').closest('article')).toHaveClass('is-highlighted');
  });

  it('opens the project drawer', async () => {
    mockFetch();
    render(<MemoryRouter initialEntries={['/']}><App /></MemoryRouter>);

    await openPanel('Projects');
    await screen.findByText('Website');
    fireEvent.click(screen.getByRole('button', { name: /inspect/i }));

    const drawer = screen.getByRole('dialog', { name: /website project details/i });
    expect(within(drawer).getByText('PROJECT MODULE')).toBeInTheDocument();
  });

  it('copies email from the contact module', async () => {
    mockFetch();
    Object.assign(navigator, { clipboard: { writeText: vi.fn(() => Promise.resolve()) } });
    render(<MemoryRouter initialEntries={['/']}><App /></MemoryRouter>);

    await openPanel('Contact');
    fireEvent.click(await screen.findByRole('button', { name: 'copy' }));

    expect(navigator.clipboard.writeText).toHaveBeenCalledWith('santos.jon.derek@gmail.com');
    expect(await screen.findByRole('status')).toHaveTextContent('TRANSMISSION COPIED');
  });

  it('minimizes and restores the terminal hero', async () => {
    mockFetch();
    render(<MemoryRouter initialEntries={['/']}><App /></MemoryRouter>);

    await openPanel('Overview');
    await screen.findByText('Derek Santos');
    fireEvent.click(screen.getByRole('button', { name: /minimize terminal/i }));
    expect(screen.getByText(/DEREK.OS minimized/i)).toBeInTheDocument();

    fireEvent.click(screen.getByText(/DEREK.OS minimized/i));
    expect(screen.getByRole('button', { name: /maximize terminal/i })).toBeInTheDocument();
  });

  it('renders project routes', () => {
    mockFetch();
    render(<MemoryRouter initialEntries={['/project/vitality']}><App /></MemoryRouter>);

    expect(screen.getByText('Vitality')).toBeInTheDocument();
    expect(screen.getByText('Mission')).toBeInTheDocument();
  });

  it('renders client-side not found routes', () => {
    mockFetch();
    render(<MemoryRouter initialEntries={['/missing']}><App /></MemoryRouter>);

    expect(screen.getByText('Sorry! Could not find page!')).toBeInTheDocument();
  });
});
