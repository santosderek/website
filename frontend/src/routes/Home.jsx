import { useEffect, useState } from 'react';

import { getResumeData } from '../api/client.js';
import ContactSection from '../components/ContactSection.jsx';
import ExperienceSection from '../components/ExperienceSection.jsx';
import LoadingScreen from '../components/LoadingScreen.jsx';
import ProjectsSection from '../components/ProjectsSection.jsx';
import ResumeSection from '../components/ResumeSection.jsx';
import ScrollSpy from '../components/ScrollSpy.jsx';
import SkillsSection from '../components/SkillsSection.jsx';
import TerminalHero from '../components/TerminalHero.jsx';

export default function Home() {
  const [resumeData, setResumeData] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    let isMounted = true;
    getResumeData()
      .then((data) => { if (isMounted) setResumeData(data); })
      .catch((requestError) => { if (isMounted) setError(requestError); });
    return () => { isMounted = false; };
  }, []);

  if (error) {
    return <div className="content pt-3"><p className="text-center">Unable to load website content.</p></div>;
  }

  if (!resumeData) {
    return <LoadingScreen />;
  }

  return (
    <>
      <ScrollSpy />
      <div id="content">
        <div className="scrollspy">
          <TerminalHero />
          <div className="content pt-3">
            <ExperienceSection careers={resumeData.career} educations={resumeData.education} />
            <SkillsSection skills={resumeData.skills} />
            <ProjectsSection repos={resumeData.repos} />
            <ResumeSection />
            <ContactSection />
          </div>
        </div>
      </div>
    </>
  );
}
