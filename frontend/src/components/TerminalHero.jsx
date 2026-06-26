export default function TerminalHero() {
  return (
    <section className="overview-panel" aria-label="Derek Santos overview">
      <div className="overview-kicker">DEREK.OS BOOT SEQUENCE</div>
      <div className="overview-grid">
        <div className="overview-identity">
          <div className="pixel-avatar" aria-hidden="true">DS</div>
          <h1>Derek Santos</h1>
          <p>A software developer with a passion for automation and orchestration.</p>
        </div>
        <div className="overview-terminal-lines" aria-label="Profile commands">
          <p><span>&gt; role --current</span> Full-Stack Software Engineer</p>
          <p><span>&gt; experience --years</span> 10+</p>
          <p><span>&gt; focus</span> Python • Rust • MicroServices</p>
          <p><span>&gt; mode</span> automation • orchestration • distributed systems</p>
        </div>
      </div>
      <div className="terminal-mode-row" aria-label="Focus modes">
        <span>AUTOMATION</span>
        <span>ORCHESTRATION</span>
        <span>MICROSERVICES</span>
      </div>
      <div className="overview-hint">Use the module rail, command palette, or project inspector to navigate.</div>
    </section>
  );
}
