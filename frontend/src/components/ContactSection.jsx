import SectionHeader from './SectionHeader.jsx';

const iconFilter = 'invert(17%) sepia(0%) saturate(1641%) hue-rotate(158deg) brightness(96%) contrast(93%)';

function ContactIcon({ src, alt }) {
  return <img style={{ width: '1.5em', filter: iconFilter }} src={src} alt={alt} />;
}

export default function ContactSection() {
  return (
    <>
      <SectionHeader id="contact" title="Contact" quote={'"And my axe!" - Gimli'} />
      <div className="row text-center">
        <div className="col-sm-12 col-md-12">
          <p>The best way to contact me is through email or linkedin!</p>
          <a href="mailto:santos.jon.derek@gmail.com">
            <ContactIcon src="/static/images/svg/envelope.svg" alt="Email" /> <span>santos.jon.derek@gmail.com</span>
          </a>
          <br />
          <a href="https://www.linkedin.com/in/santosderek/">
            <ContactIcon src="/static/images/svg/linkedin.svg" alt="LinkedIn" /> <span>https://www.linkedin.com/in/santosderek/</span>
          </a>
        </div>
      </div>
      <div className="row" id="justsomespace" aria-hidden="true">
        {Array.from({ length: 15 }).map((_, index) => <br key={index} />)}
      </div>
    </>
  );
}
