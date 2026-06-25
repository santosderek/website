import SectionHeader from './SectionHeader.jsx';

export default function ResumeSection() {
  return (
    <>
      <SectionHeader id="resume" title="Resume" quote={'"The Force will be with you. Always." - Obi-Wan Kenobi'} />
      <div className="row text-center">
        <div className="col-sm-12 col-md-12">
          <p>
            My resume is automated to be created based on the contents of this website.<br />
            Upon clicking the download button on <b>either the top right of the navbar</b>, going to{' '}
            <b><a href="/resume">/resume </a></b>, or <b><a href="/resume">clicking here</a></b>, the Flask application
            (this website) will generate a formatted Microsoft Word file and send the file to your computer. This will
            ensure you always get the most up-to-date version of my resume.
          </p>
        </div>
      </div>
    </>
  );
}
