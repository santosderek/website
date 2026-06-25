import SectionHeader from './SectionHeader.jsx';

function Stars({ value }) {
  return (
    <span>
      {Array.from({ length: value }).map((_, index) => <i key={`solid-${index}`} style={{ fontSize: '.5em' }} className="fas fa-star" />)}
      {Array.from({ length: 5 - value }).map((_, index) => <i key={`empty-${index}`} style={{ fontSize: '.5em' }} className="far fa-star" />)}
    </span>
  );
}

function SkillTable({ entries }) {
  return (
    <table className="table table-hover">
      <tbody>
        {entries.map(([name, rating]) => (
          <tr key={name}>
            <td className="skill_title" scope="row"><span>{name}</span></td>
            <td className="skill_stars"><Stars value={rating} /></td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

function splitInHalf(items) {
  const midpoint = Math.floor(items.length / 2);
  return [items.slice(0, midpoint), items.slice(midpoint)];
}

export default function SkillsSection({ skills }) {
  const technologies = [...skills.technologies].sort((left, right) => right[1] - left[1]);
  const tools = [...skills.tools].sort((left, right) => right[1] - left[1]);
  const [technologiesLeft, technologiesRight] = splitInHalf(technologies);
  const [toolsLeft, toolsRight] = splitInHalf(tools);

  return (
    <>
      <SectionHeader id="skills" title="Skills" quote={'"Power! Unlimited power!" - Darth Sidious'} />
      <div className="row">
        <div className="col-sm-12 col-md-12"><h2><b>Technologies</b></h2></div>
        <div className="col-sm-6 col-lg-6"><SkillTable entries={technologiesLeft} /></div>
        <div className="col-sm-6 col-lg-6"><SkillTable entries={technologiesRight} /></div>
      </div>
      <hr />
      <div className="row">
        <div className="col-sm-12"><h2><b>Tools</b></h2></div>
        <div className="col-sm-6"><SkillTable entries={toolsLeft} /></div>
        <div className="col-sm-6"><SkillTable entries={toolsRight} /></div>
      </div>
    </>
  );
}
