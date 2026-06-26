import { useEffect, useMemo, useState } from 'react';
import { useNavigate } from 'react-router-dom';

const actions = [
  { id: 'experience', label: 'Jump to Experience', hint: '/experience', type: 'hash', value: 'experience' },
  { id: 'skills', label: 'Jump to Skills', hint: '/skills', type: 'hash', value: 'skills' },
  { id: 'projects', label: 'Jump to Projects', hint: '/projects', type: 'hash', value: 'projects' },
  { id: 'resume-section', label: 'Jump to Resume Section', hint: '/resume-section', type: 'hash', value: 'resume' },
  { id: 'contact', label: 'Jump to Contact', hint: '/contact', type: 'hash', value: 'contact' },
  { id: 'project-vitality', label: 'Open Vitality Project', hint: '/project/vitality', type: 'route', value: '/project/vitality' },
  { id: 'project-site', label: 'Open santosderek.com Project', hint: '/project/santosderek', type: 'route', value: '/project/santosderek' },
  { id: 'download-resume', label: 'Download Resume', hint: '/resume', type: 'location', value: '/resume' },
  { id: 'github', label: 'Open GitHub', hint: 'external', type: 'external', value: 'https://github.com/santosderek' },
  { id: 'linkedin', label: 'Open LinkedIn', hint: 'external', type: 'external', value: 'https://www.linkedin.com/in/santosderek/' },
];

export default function CommandPalette() {
  const navigate = useNavigate();
  const [isOpen, setIsOpen] = useState(false);
  const [query, setQuery] = useState('');
  const [activeIndex, setActiveIndex] = useState(0);

  const filteredActions = useMemo(() => {
    const normalized = query.trim().toLowerCase();
    if (!normalized) return actions;
    return actions.filter((action) => `${action.label} ${action.hint}`.toLowerCase().includes(normalized));
  }, [query]);

  useEffect(() => {
    if (activeIndex >= filteredActions.length) {
      setActiveIndex(0);
    }
  }, [activeIndex, filteredActions.length]);

  useEffect(() => {
    function onKeyDown(event) {
      const isPaletteShortcut = (event.key.toLowerCase() === 'k' && (event.metaKey || event.ctrlKey)) || (event.key === '/' && !isOpen);
      if (isPaletteShortcut) {
        event.preventDefault();
        setIsOpen(true);
        return;
      }

      if (!isOpen) return;

      if (event.key === 'Escape') {
        setIsOpen(false);
        setQuery('');
      } else if (event.key === 'ArrowDown') {
        event.preventDefault();
        setActiveIndex((current) => Math.min(current + 1, Math.max(filteredActions.length - 1, 0)));
      } else if (event.key === 'ArrowUp') {
        event.preventDefault();
        setActiveIndex((current) => Math.max(current - 1, 0));
      } else if (event.key === 'Enter') {
        event.preventDefault();
        const action = filteredActions[activeIndex];
        if (action) runAction(action);
      }
    }

    window.addEventListener('keydown', onKeyDown);
    return () => window.removeEventListener('keydown', onKeyDown);
  }, [activeIndex, filteredActions, isOpen]);

  function runAction(action) {
    setIsOpen(false);
    setQuery('');

    if (action.type === 'hash') {
      if (window.location.pathname !== '/') {
        navigate('/');
      }
      window.history.replaceState(null, '', `#${action.value}`);
      window.dispatchEvent(new CustomEvent('derekos:navigate-section', { detail: action.value }));
      window.setTimeout(() => document.getElementById(action.value)?.focus(), 80);
      return;
    }

    if (action.type === 'route') {
      navigate(action.value);
      return;
    }

    window.location.href = action.value;
  }

  if (!isOpen) {
    return (
      <button className="command-trigger" type="button" onClick={() => setIsOpen(true)} aria-label="Open command palette">
        ⌘K
      </button>
    );
  }

  return (
    <div className="command-overlay" role="dialog" aria-modal="true" aria-label="Command palette" onMouseDown={() => setIsOpen(false)}>
      <div className="command-palette" onMouseDown={(event) => event.stopPropagation()}>
        <div className="command-title">DEREK.OS COMMAND</div>
        <label className="sr-only" htmlFor="command-search">Search commands</label>
        <input
          id="command-search"
          autoFocus
          value={query}
          onChange={(event) => { setQuery(event.target.value); setActiveIndex(0); }}
          placeholder="> search site..."
        />
        <div className="command-list">
          {filteredActions.map((action, index) => (
            <button
              className={`command-item ${index === activeIndex ? 'active' : ''}`}
              key={action.id}
              type="button"
              onMouseEnter={() => setActiveIndex(index)}
              onClick={() => runAction(action)}
            >
              <span>{action.label}</span>
              <small>{action.hint}</small>
            </button>
          ))}
          {filteredActions.length === 0 ? <p className="command-empty">No matching command.</p> : null}
        </div>
      </div>
    </div>
  );
}
