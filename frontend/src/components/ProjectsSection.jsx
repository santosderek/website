import { useEffect, useState } from 'react';

import { getGithubUser } from '../api/client.js';
import SectionHeader from './SectionHeader.jsx';

export default function ProjectsSection({ repos }) {
  const [githubUser, setGithubUser] = useState({});

  useEffect(() => {
    let isMounted = true;
    getGithubUser()
      .then((data) => { if (isMounted) setGithubUser(data || {}); })
      .catch(() => { if (isMounted) setGithubUser({}); });
    return () => { isMounted = false; };
  }, []);

  return (
    <>
      <SectionHeader id="projects" title="Projects" quote={'"Do. Or do not. There is no try." - Yoda'} />
      <div className="row">
        {repos.map((repo) => (
          <a href={repo.url} key={repo.title}>
            <div className="card mb-3" style={{ maxWidth: '18rem' }}>
              <div className="card-header">{repo.title}</div>
              <div className="card-body">
                <h5 className="card-title">{repo.subtitle}</h5>
                <p className="card-text">{repo.description}</p>
              </div>
            </div>
          </a>
        ))}

        <div className="col-sm-12 text-center mt-4 mb-5">
          <a className="button_link" href="https://github.com/santosderek">
            {githubUser.public_repos ? `...and ${githubUser.public_repos} more on github!` : '...and many more!'}
          </a>
        </div>
      </div>
    </>
  );
}
