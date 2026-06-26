import { useState } from 'react';

import SectionHeader from './SectionHeader.jsx';

const email = 'santos.jon.derek@gmail.com';
const iconFilter = 'invert(17%) sepia(0%) saturate(1641%) hue-rotate(158deg) brightness(96%) contrast(93%)';

function ContactIcon({ src, alt }) {
  return <img style={{ width: '1.5em', filter: iconFilter }} src={src} alt={alt} />;
}

export default function ContactSection() {
  const [toast, setToast] = useState('');

  async function copyEmail() {
    try {
      await navigator.clipboard.writeText(email);
      setToast('TRANSMISSION COPIED');
    } catch {
      setToast('COPY EMAIL: ' + email);
    }
    window.setTimeout(() => setToast(''), 1800);
  }

  return (
    <>
      <SectionHeader id="contact" title="Contact" quote={'"And my axe!" - Gimli'} />
      <div className="row text-center contact-module">
        <div className="col-sm-12 col-md-12">
          <p>The best way to contact me is through email or linkedin!</p>
          <div className="contact-grid">
            <div className="contact-card">
              <ContactIcon src="/static/images/svg/envelope.svg" alt="Email" />
              <span>{email}</span>
              <button className="button_link" type="button" onClick={copyEmail}>copy</button>
            </div>
            <a className="contact-card" href="https://www.linkedin.com/in/santosderek/">
              <ContactIcon src="/static/images/svg/linkedin.svg" alt="LinkedIn" />
              <span>https://www.linkedin.com/in/santosderek/</span>
              <strong>open</strong>
            </a>
          </div>
          {toast ? <div className="pixel-toast" role="status">{toast}</div> : null}
        </div>
      </div>
      <div className="row" id="justsomespace" aria-hidden="true">
        {Array.from({ length: 15 }).map((_, index) => <br key={index} />)}
      </div>
    </>
  );
}
