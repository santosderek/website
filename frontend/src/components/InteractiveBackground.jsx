import { useEffect, useState } from 'react';

export default function InteractiveBackground() {
  const [ripples, setRipples] = useState([]);

  useEffect(() => {
    function updatePointer(event) {
      document.documentElement.style.setProperty('--cursor-x', `${event.clientX}px`);
      document.documentElement.style.setProperty('--cursor-y', `${event.clientY}px`);
    }

    function addRipple(event) {
      const id = `${Date.now()}-${Math.random()}`;
      setRipples((current) => [...current.slice(-5), { id, x: event.clientX, y: event.clientY }]);
      window.setTimeout(() => {
        setRipples((current) => current.filter((ripple) => ripple.id !== id));
      }, 850);
    }

    window.addEventListener('pointermove', updatePointer, { passive: true });
    window.addEventListener('pointerdown', addRipple, { passive: true });
    return () => {
      window.removeEventListener('pointermove', updatePointer);
      window.removeEventListener('pointerdown', addRipple);
    };
  }, []);

  return (
    <div className="interactive-background" aria-hidden="true">
      <div className="cursor-liquid" />
      <div className="data-packets">
        {Array.from({ length: 18 }).map((_, index) => <span key={index} style={{ '--packet-index': index }} />)}
      </div>
      {ripples.map((ripple) => (
        <span
          className="pixel-ripple"
          key={ripple.id}
          style={{ left: ripple.x, top: ripple.y }}
        />
      ))}
    </div>
  );
}
