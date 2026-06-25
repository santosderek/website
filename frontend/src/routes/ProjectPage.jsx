import { useParams } from 'react-router-dom';

import { projectPages } from '../data/projects.js';
import NotFound from './NotFound.jsx';

function ProjectHeader({ title, subtitle }) {
  return (
    <div className="row mt-4">
      <div className="col-sm-12 col-md-12 col-lg-12 mt-3 text-center">
        <h1>{title}</h1>
        <p className="w-50">{subtitle}</p>
      </div>
    </div>
  );
}

function TextSection({ section }) {
  return (
    <div className="row project_overview">
      <div className="col-sm-12 text-center"><h3>{section.title}</h3></div>
      {section.image ? (
        <div className="pt-4 col-sm-12 col-md-12 text-center">
          <img className="w-75" src={section.image} alt={section.imageAlt} />
        </div>
      ) : null}
      <div className="pt-4 col-sm-12 col-md-12">
        {section.paragraphs.map((paragraph) => <p className="w-75" key={paragraph}>{paragraph}</p>)}
      </div>
    </div>
  );
}

function VitalityDetails({ project }) {
  return (
    <>
      <div className="row mb-4"><div className="col-sm-12 col-md-12 col-lg-12 mt-3 text-center"><h2>Mission</h2></div></div>
      <div className="row mb-4">
        <div className="col-sm-12 col-md-12 text-center mission">
          <img src={project.mission.image} alt={project.mission.imageAlt} />
          <p className="text-center w-50 mt-4">{project.mission.text}</p>
        </div>
      </div>
      <div className="row"><div className="col-sm-12 col-md-12 col-lg-12 mt-3 text-center"><h2>Features</h2></div></div>
      <div className="row mt-3">
        {project.features.map((feature) => (
          <div className="col-sm-12 col-md-6 text-center feature" key={feature.image}>
            <img src={feature.image} alt="Vitality feature" className="w-75" />
            <p className="text-center w-75 pt-4">{feature.text}</p>
          </div>
        ))}
      </div>
      <div className="row career">
        <div className="col-sm-12 col-md-12 text-center">
          <h2>Technologies used</h2>
          <ul>{project.technologies.map((technology) => <li key={technology}>{technology}</li>)}</ul>
        </div>
      </div>
    </>
  );
}

function ProjectLinks({ links }) {
  if (!links?.length) return null;

  return (
    <div className="row mt-3">
      {links.map((link) => (
        <div className="col-sm-12 col-md-6 mt-3 text-center" key={link.href}>
          <h2 style={{ paddingBottom: '1em' }}>{link.title}</h2>
          <a href={link.href} className="button_link">{link.text}</a>
        </div>
      ))}
    </div>
  );
}

export default function ProjectPage() {
  const { project: projectSlug } = useParams();
  const project = projectPages[projectSlug];

  if (!project) {
    return <NotFound />;
  }

  return (
    <div id="content" className="content pt-3">
      <ProjectHeader title={project.title} subtitle={project.subtitle} />
      {projectSlug === 'vitality' ? <VitalityDetails project={project} /> : null}
      {project.sections.map((section) => <TextSection key={section.title} section={section} />)}
      <ProjectLinks links={project.links} />
    </div>
  );
}
