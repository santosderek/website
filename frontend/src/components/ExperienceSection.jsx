import SectionHeader from './SectionHeader.jsx';

export default function ExperienceSection({ careers, educations }) {
  return (
    <>
      <SectionHeader id="experience" title="Experience" quote={'"The only way to know how strong you are is to keep testing your limits." – Jor El'} />
      <div className="row"><div className="col"><h2>Career</h2></div></div>
      {careers.map((career) => (
        <div className="row career" key={`${career.title}-${career.date}`}>
          <div className="col-md-12 col-lg-4 career_header">
            <h3>{career.title}</h3>
            {career.type ? <p>{career.type}</p> : null}
            <p>{career.date}</p>
            <p>{career.location}</p>
          </div>
          <div className="col-md-12 col-lg-8 career_description">
            <ul>{career.descriptions.map((description) => <li key={description}>{description}</li>)}</ul>
          </div>
        </div>
      ))}

      <hr />
      <div className="row"><div className="col"><h2>Education</h2></div></div>
      {educations.map((education) => (
        <div className="row education" key={`${education.title}-${education.date}`}>
          <div className="col-sm-12 col-lg-4">
            <h3>{education.title}</h3>
            <p>{education.date}</p>
          </div>
          <div className="col-sm-12 col-lg-8 education_description">
            <p><b>{education.degree}</b></p>
            <p><em>Relevant Courses:</em></p>
            <ul>{education.relevantCourses.map((course) => <li key={course}>{course}</li>)}</ul>
            {education.additional.map((addition) => <p key={addition}>{addition}</p>)}
          </div>
        </div>
      ))}
    </>
  );
}
