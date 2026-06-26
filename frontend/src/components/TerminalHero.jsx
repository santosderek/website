import { useState } from 'react';

export default function TerminalHero() {
  const [isMinimized, setIsMinimized] = useState(false);
  const [isExpanded, setIsExpanded] = useState(false);

  if (isMinimized) {
    return (
      <section className="terminal-section terminal-section-minimized">
        <button className="terminal-minimized" type="button" onClick={() => setIsMinimized(false)}>
          ▓ DEREK.OS minimized — click to restore
        </button>
      </section>
    );
  }

  return (
    <section className="terminal-section">
      <div className={`terminal ${isExpanded ? 'terminal-expanded' : ''}`}>
        <div className="terminal-header">
          <nav className="terminal-header-buttons" aria-label="Terminal controls">
            <button className="control-item control-minimize" type="button" onClick={() => setIsMinimized(true)} aria-label="Minimize terminal">‒</button>
            <button className="control-item control-maximize" type="button" onClick={() => setIsExpanded((current) => !current)} aria-label="Maximize terminal">□</button>
            <button className="control-item control-close" type="button" onClick={() => setIsMinimized(true)} aria-label="Close terminal">˟</button>
          </nav>
        </div>
        <main className="terminal-body">
          <div className="window-cursor"><span className="i-cursor-indicator">&gt; who -u | pixelify</span></div>
          <div className="terminal-flex-container">
            <div className="terminal-flex-item-1 terminal-body-header"><p>Derek Santos</p></div>
            <div className="terminal-flex-item-2 terminal-body-description">
              <p>A software developer with a passion for automation and orchestration.</p>
              <p><span>Title:</span> Full-Stack Software Engineer</p>
              <p><span>Coding Experience:</span> 10+ years</p>
              <p><span>Passions:</span> Python, Rust, MicroServices</p>
            </div>
          </div>
          <div className="terminal-mode-row" aria-label="Focus modes">
            <span>AUTOMATION</span>
            <span>ORCHESTRATION</span>
            <span>MICROSERVICES</span>
          </div>
          <div className="window-cursor"><span className="i-cursor-indicator">&gt;</span><span className="i-cursor-underscore">_</span></div>
        </main>
      </div>
    </section>
  );
}
