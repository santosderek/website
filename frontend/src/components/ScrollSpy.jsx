import { useEffect, useState } from 'react';

const sections = [
  ['experience', 'Experience'],
  ['skills', 'Skills'],
  ['projects', 'Projects'],
  ['resume', 'Resume'],
  ['contact', 'Contact'],
];

export default function ScrollSpy() {
  const [visible, setVisible] = useState(false);
  const [active, setActive] = useState('experience');

  useEffect(() => {
    function onScroll() {
      const experience = document.getElementById('experience');
      const shouldShow = window.innerWidth > 1400 && experience && window.scrollY > experience.offsetTop - 200;
      setVisible(Boolean(shouldShow));

      const current = sections
        .map(([id]) => document.getElementById(id))
        .filter(Boolean)
        .reverse()
        .find((element) => window.scrollY >= element.offsetTop - 250);
      if (current) {
        setActive(current.id);
      }
    }

    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', onScroll);
    return () => {
      window.removeEventListener('scroll', onScroll);
      window.removeEventListener('resize', onScroll);
    };
  }, []);

  return (
    <div id="pageLocationScrollSpy" className="list-group" style={{ display: visible ? 'block' : 'none' }}>
      {sections.map(([id, label]) => (
        <a key={id} className={`list-group-item list-group-item-action ${active === id ? 'active' : ''}`} href={`#${id}`}>
          {label}
        </a>
      ))}
    </div>
  );
}
