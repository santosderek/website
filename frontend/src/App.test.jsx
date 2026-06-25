import { fireEvent, render, screen, waitFor } from '@testing-library/react';
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

describe('App', () => {
  it('renders home content from the Flask API', async () => {
    mockFetch();
    render(<MemoryRouter initialEntries={['/']}><App /></MemoryRouter>);

    await waitFor(() => expect(screen.getAllByText('Full-Stack Software Engineer').length).toBeGreaterThan(0));
    expect(screen.getByText('Website')).toBeInTheDocument();
    expect(screen.getByText('Python')).toBeInTheDocument();
    expect(await screen.findByText('...and 42 more on github!')).toBeInTheDocument();
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
