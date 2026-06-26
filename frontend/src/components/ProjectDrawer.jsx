import { useEffect, useState } from 'react';

const tabs = ['overview', 'stack', 'links'];

const projectMeta = {
  'santosderek.com': {
    stack: ['React Router', 'Flask API', 'Python', 'Docker'],
    details: 'Personal portfolio and JSON-powered resume system, now split into a React frontend and API backend.',
  },
  Vitality: {
    stack: ['Flask', 'Docker', 'GitHub Actions', 'Nginx'],
    details: 'Fitness platform concept with trainers, scheduling, workouts, maps, and nutrition recommendations.',
  },
  'Flask-Kasa': {
    stack: ['Python', 'Flask', 'IoT', 'Automation'],
    details: 'Webhook-driven Kasa light automation project for media-room workflows.',
  },
};

export default function ProjectDrawer({ project, onClose }) {
  const [activeTab, setActiveTab] = useState('overview');

  useEffect(() => {
    function onKeyDown(event) {
      if (event.key === 'Escape') onClose();
    }
    window.addEventListener('keydown', onKeyDown);
    return () => window.removeEventListener('keydown', onKeyDown);
  }, [onClose]);

  if (!project) return null;

  const meta = projectMeta[project.title] || {
    stack: ['Python', 'Automation', 'Open Source'],
    details: project.subtitle,
  };

  return (
    <div className="project-drawer-overlay" role="dialog" aria-modal="true" aria-label={`${project.title} project details`} onMouseDown={onClose}>
      <aside className="project-drawer" onMouseDown={(event) => event.stopPropagation()}>
        <div className="project-drawer-header">
          <div>
            <small>PROJECT MODULE</small>
            <h2>{project.title}</h2>
          </div>
          <button type="button" onClick={onClose} aria-label="Close project drawer">×</button>
        </div>

        <div className="project-tabs" role="tablist" aria-label="Project detail tabs">
          {tabs.map((tab) => (
            <button
              key={tab}
              className={activeTab === tab ? 'active' : ''}
              type="button"
              onClick={() => setActiveTab(tab)}
            >
              {tab}
            </button>
          ))}
        </div>

        {activeTab === 'overview' ? (
          <div className="drawer-panel">
            <p>{meta.details}</p>
            <p>{project.subtitle}</p>
          </div>
        ) : null}

        {activeTab === 'stack' ? (
          <div className="drawer-panel stack-panel">
            {meta.stack.map((item) => <span key={item}>{item}</span>)}
          </div>
        ) : null}

        {activeTab === 'links' ? (
          <div className="drawer-panel">
            <a className="button_link" href={project.url}>{project.url.startsWith('/') ? 'Open project page' : 'Open source'}</a>
            <a className="button_link" href="https://github.com/santosderek">Open GitHub profile</a>
          </div>
        ) : null}
      </aside>
    </div>
  );
}
