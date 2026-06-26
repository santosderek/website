import { useState } from 'react';

const iconFilter = 'invert(17%) sepia(0%) saturate(1641%) hue-rotate(158deg) brightness(96%) contrast(93%)';

function Icon({ src, alt }) {
  return <img style={{ width: '1.5em', filter: iconFilter }} src={src} alt={alt} />;
}

function navigateSection(section) {
  window.history.replaceState(null, '', `/#${section}`);
  window.dispatchEvent(new CustomEvent('derekos:navigate-section', { detail: section }));
}

export default function Navbar() {
  const [isOpen, setIsOpen] = useState(false);
  const collapseClassName = `navbar-collapse collapse w-100 dual-collapse2 ${isOpen ? 'show' : ''}`;

  return (
    <nav className="navbar navbar-expand-lg my-auto">
      <div className={`${collapseClassName} order-1 order-lg-0`}>
        <ul className="navbar-nav m-auto">
          <li className="nav-item"><button type="button" style={{ paddingRight: '.5em' }} onClick={() => navigateSection('experience')}>Experience</button></li>
          <li className="nav-item"><button type="button" style={{ paddingRight: '.5em' }} onClick={() => navigateSection('skills')}>Skills</button></li>
          <li className="nav-item"><button type="button" style={{ paddingRight: '.5em' }} onClick={() => navigateSection('projects')}>Projects</button></li>
          <li className="nav-item"><button type="button" style={{ paddingRight: '.5em' }} onClick={() => navigateSection('resume')}>Resume</button></li>
          <li className="nav-item"><button type="button" onClick={() => navigateSection('contact')}>Contact</button></li>
        </ul>
      </div>
      <div className="mx-auto order-0">
        <a className="navbar-brand mx-auto" href="/" style={{ fontSize: 'xx-large' }}>
          <img src="/static/images/santosderek.png" alt="Derek Santos" />
        </a>
        <button className="navbar-toggler ml-3" type="button" aria-expanded={isOpen} aria-label="Toggle navigation" onClick={() => setIsOpen((current) => !current)}>
          <span className="navbar-toggler-icon" />
        </button>
      </div>
      <div className={`${collapseClassName} order-3`}>
        <ul className="navbar-nav ml-auto">
          <li className="nav-item"><a className="nav-link" aria-label="GitHub" href="https://github.com/santosderek"><Icon src="/static/images/svg/github.svg" alt="GitHub" /></a></li>
          <li className="nav-item"><a className="nav-link" aria-label="LinkedIn" href="https://www.linkedin.com/in/santosderek/"><Icon src="/static/images/svg/linkedin.svg" alt="LinkedIn" /></a></li>
          <li className="nav-item"><a className="nav-link" aria-label="Email" href="mailto:santos.jon.derek@gmail.com"><Icon src="/static/images/svg/envelope.svg" alt="Email" /></a></li>
          <li className="nav-item"><a className="nav-link" aria-label="Download resume" href="/resume"><Icon src="/static/images/svg/download.svg" alt="Download resume" /></a></li>
        </ul>
      </div>
    </nav>
  );
}
