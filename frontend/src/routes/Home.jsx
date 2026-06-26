import { useEffect, useState } from 'react';

import { getResumeData } from '../api/client.js';
import LoadingScreen from '../components/LoadingScreen.jsx';
import TuiWorkspace from '../components/TuiWorkspace.jsx';

export default function Home() {
  const [resumeData, setResumeData] = useState(null);
  const [error, setError] = useState(null);
  const [selectedSkill, setSelectedSkill] = useState('all');

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

  return <TuiWorkspace resumeData={resumeData} selectedSkill={selectedSkill} onSelectSkill={setSelectedSkill} />;
}
