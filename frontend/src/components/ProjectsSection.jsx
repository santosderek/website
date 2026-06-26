import { useEffect, useMemo, useState } from 'react';

import { getGithubUser } from '../api/client.js';
import GlassCard from './GlassCard.jsx';
import ProjectDrawer from './ProjectDrawer.jsx';
import SectionHeader from './SectionHeader.jsx';

const projectTags = {
  Website: ['React', 'Flask', 'Python', 'Docker', 'REST APIs', 'JSON'],
  'santosderek.com': ['React', 'Flask', 'Python', 'Docker', 'REST APIs', 'JSON'],
  'Imgur to Folder': ['Python', 'REST APIs', 'Automation'],
  Vitality: ['Python', 'Flask', 'Docker', 'Github Actions', 'MongoDB'],
  'Fruit Fly Tracking': ['C++', 'Open Computer Vision'],
  'Flask-Kasa': ['Python', 'Flask', 'Automation', 'REST APIs'],
};

export default function ProjectsSection({ repos, selectedSkill = 'all' }) {
  const [githubUser, setGithubUser] = useState({});
  const [activeProject, setActiveProject] = useState(null);

  useEffect(() => {
    let isMounted = true;
    getGithubUser()
      .then((data) => { if (isMounted) setGithubUser(data || {}); })
      .catch(() => { if (isMounted) setGithubUser({}); });
    return () => { isMounted = false; };
  }, []);

  const enrichedRepos = useMemo(() => repos.map((repo) => ({
    ...repo,
    tags: projectTags[repo.title] || [],
  })), [repos]);

  return (
    <>
      <SectionHeader id="projects" title="Projects" quote={'"Do. Or do not. There is no try." - Yoda'} />
      <div className="row project-grid">
        {enrichedRepos.map((repo) => {
          const isHighlighted = selectedSkill === 'all' || repo.tags.some((tag) => tag.toLowerCase() === selectedSkill.toLowerCase());
          return (
            <GlassCard
              as="article"
              className={`card mb-3 project-card ${isHighlighted ? 'is-highlighted' : 'is-dimmed'}`}
              key={repo.title}
            >
              <div className="card-header">{repo.title}</div>
              <div className="card-body">
                <h5 className="card-title">{repo.subtitle}</h5>
                {repo.description ? <p className="card-text">{repo.description}</p> : null}
                <div className="project-tags">
                  {repo.tags.map((tag) => <span key={tag}>{tag}</span>)}
                </div>
                <div className="project-actions">
                  <button className="button_link" type="button" onClick={() => setActiveProject(repo)}>inspect</button>
                  <a className="button_link" href={repo.url}>{repo.url.startsWith('/') ? 'open' : 'source'}</a>
                </div>
              </div>
            </GlassCard>
          );
        })}

        <div className="col-sm-12 text-center mt-4 mb-5">
          <a className="button_link" href="https://github.com/santosderek">
            {githubUser.public_repos ? `...and ${githubUser.public_repos} more on github!` : '...and many more!'}
          </a>
        </div>
      </div>
      <ProjectDrawer project={activeProject} onClose={() => setActiveProject(null)} />
    </>
  );
}
