import { useState } from 'react';

import SectionHeader from './SectionHeader.jsx';

export default function ResumeSection() {
  const [isCompiling, setIsCompiling] = useState(false);

  function downloadResume(event) {
    event.preventDefault();
    setIsCompiling(true);
    window.setTimeout(() => {
      window.location.href = '/resume';
    }, 650);
  }

  return (
    <>
      <SectionHeader id="resume" title="Resume" quote={'"The Force will be with you. Always." - Obi-Wan Kenobi'} />
      <div className="row text-center resume-module">
        <div className="col-sm-12 col-md-12">
          <div className="resume-status-card">
            <div className="resume-status-header">
              <span>RESUME.DOCX</span>
              <strong>{isCompiling ? '● COMPILING' : '● READY'}</strong>
            </div>
            <p>
              My resume is automated to be created based on the contents of this website.<br />
              Upon clicking the download button on <b>either the top right of the navbar</b>, going to{' '}
              <b><a href="/resume">/resume </a></b>, or <b><a href="/resume">clicking here</a></b>, the Flask application
              (this website) will generate a formatted Microsoft Word file and send the file to your computer. This will
              ensure you always get the most up-to-date version of my resume.
            </p>
            <div className="resume-preview">
              <span>source: /api/v1/resume</span>
              <span>format: docx</span>
              <span>sections: career • education • skills</span>
            </div>
            <a className={`button_link resume-download ${isCompiling ? 'is-compiling' : ''}`} href="/resume" onClick={downloadResume}>
              {isCompiling ? 'compiling resume...' : 'generate + download'}
            </a>
          </div>
        </div>
      </div>
    </>
  );
}
