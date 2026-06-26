import { useEffect, useMemo, useState } from 'react';

import ContactSection from './ContactSection.jsx';
import ExperienceSection from './ExperienceSection.jsx';
import ProjectsSection from './ProjectsSection.jsx';
import ResumeSection from './ResumeSection.jsx';
import SkillsSection from './SkillsSection.jsx';
import TerminalHero from './TerminalHero.jsx';

const panels = [
  { id: 'overview', label: 'Overview', command: 'boot --profile' },
  { id: 'experience', label: 'Experience', command: 'cat ./career.timeline' },
  { id: 'skills', label: 'Skills', command: 'scan --skills' },
  { id: 'projects', label: 'Projects', command: 'open ./project-lab' },
  { id: 'resume', label: 'Resume', command: 'compile resume.docx' },
  { id: 'contact', label: 'Contact', command: 'transmit --channel' },
];

export default function TuiWorkspace({ resumeData, selectedSkill, onSelectSkill }) {
  const [activePanel, setActivePanel] = useState('overview');

  const panel = useMemo(
    () => panels.find((candidate) => candidate.id === activePanel) || panels[0],
    [activePanel],
  );

  useEffect(() => {
    function activateFromHash() {
      const hash = window.location.hash.replace('#', '');
      if (panels.some((candidate) => candidate.id === hash)) {
        setActivePanel(hash);
      }
    }

    function activateFromEvent(event) {
      if (panels.some((candidate) => candidate.id === event.detail)) {
        setActivePanel(event.detail);
      }
    }

    activateFromHash();
    window.addEventListener('hashchange', activateFromHash);
    window.addEventListener('derekos:navigate-section', activateFromEvent);
    return () => {
      window.removeEventListener('hashchange', activateFromHash);
      window.removeEventListener('derekos:navigate-section', activateFromEvent);
    };
  }, []);

  function activatePanel(panelId) {
    setActivePanel(panelId);
    window.history.replaceState(null, '', panelId === 'overview' ? '/' : `#${panelId}`);
  }

  return (
    <section className="tui-workspace" aria-label="Interactive portfolio TUI">
      <div className="tui-window">
        <header className="tui-titlebar">
          <div className="tui-titlebar-controls" aria-hidden="true"><span /> <span /> <span /></div>
          <div className="tui-title">DEREK.OS // PORTFOLIO.EXE</div>
          <div className="tui-status">{new Date().getFullYear()} · ONLINE</div>
        </header>

        <div className="tui-body">
          <aside className="tui-sidebar" aria-label="Portfolio sections">
            <div className="tui-sidebar-heading">/modules</div>
            {panels.map((candidate) => (
              <button
                key={candidate.id}
                type="button"
                className={`tui-nav-button ${candidate.id === activePanel ? 'active' : ''}`}
                onClick={() => activatePanel(candidate.id)}
              >
                <span>▸</span>{candidate.label}
              </button>
            ))}
          </aside>

          <main className="tui-main">
            <div className="tui-command-line">
              <span className="prompt">derek@santos:~$</span>
              <span>{panel.command}</span>
            </div>
            <div className="tui-content" id={panel.id} tabIndex={0}>
              {activePanel === 'overview' ? <TerminalHero /> : null}
              {activePanel === 'experience' ? <ExperienceSection careers={resumeData.career} educations={resumeData.education} /> : null}
              {activePanel === 'skills' ? <SkillsSection skills={resumeData.skills} selectedSkill={selectedSkill} onSelectSkill={onSelectSkill} /> : null}
              {activePanel === 'projects' ? <ProjectsSection repos={resumeData.repos} selectedSkill={selectedSkill} /> : null}
              {activePanel === 'resume' ? <ResumeSection /> : null}
              {activePanel === 'contact' ? <ContactSection /> : null}
            </div>
          </main>
        </div>
      </div>
    </section>
  );
}
