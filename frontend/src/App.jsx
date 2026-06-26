import { Route, Routes } from 'react-router-dom';

import CommandPalette from './components/CommandPalette.jsx';
import InteractiveBackground from './components/InteractiveBackground.jsx';
import ScrollSpy from './components/ScrollSpy.jsx';
import Home from './routes/Home.jsx';
import NotFound from './routes/NotFound.jsx';
import ProjectPage from './routes/ProjectPage.jsx';

export default function App() {
  return (
    <>
      <InteractiveBackground />
      <CommandPalette />
      <main>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/project/:project" element={<ProjectLayout />} />
          <Route path="*" element={<NotFound />} />
        </Routes>
      </main>
    </>
  );
}

function ProjectLayout() {
  return <ProjectPage />;
}

export { ScrollSpy };
