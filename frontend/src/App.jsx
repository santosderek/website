import { Route, Routes } from 'react-router-dom';

import Navbar from './components/Navbar.jsx';
import ScrollSpy from './components/ScrollSpy.jsx';
import Home from './routes/Home.jsx';
import NotFound from './routes/NotFound.jsx';
import ProjectPage from './routes/ProjectPage.jsx';

export default function App() {
  return (
    <>
      <header>
        <Navbar />
      </header>
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
