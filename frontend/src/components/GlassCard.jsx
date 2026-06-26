import { useState } from 'react';

export default function GlassCard({ as: Component = 'div', className = '', children, ...props }) {
  const [style, setStyle] = useState({});

  function onMouseMove(event) {
    const rect = event.currentTarget.getBoundingClientRect();
    const x = event.clientX - rect.left;
    const y = event.clientY - rect.top;
    const rotateY = ((x / rect.width) - 0.5) * 8;
    const rotateX = -((y / rect.height) - 0.5) * 8;
    setStyle({
      '--card-x': `${x}px`,
      '--card-y': `${y}px`,
      transform: `perspective(900px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-6px)`,
    });
  }

  function onMouseLeave() {
    setStyle({});
  }

  return (
    <Component
      className={`glass-tilt ${className}`.trim()}
      onMouseMove={onMouseMove}
      onMouseLeave={onMouseLeave}
      style={style}
      {...props}
    >
      {children}
    </Component>
  );
}
