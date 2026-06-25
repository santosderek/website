export default function TerminalHero() {
  return (
    <section className="terminal-section">
      <div className="terminal">
        <div className="terminal-header">
          <nav className="terminal-header-buttons">
            <span className="control-item control-minimize">‒</span>
            <span className="control-item control-maximize">□</span>
            <span className="control-item control-close">˟</span>
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
          <div className="window-cursor"><span className="i-cursor-indicator">&gt;</span><span className="i-cursor-underscore">_</span></div>
        </main>
      </div>
    </section>
  );
}
