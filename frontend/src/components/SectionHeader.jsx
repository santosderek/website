export default function SectionHeader({ id, title, quote }) {
  return (
    <div className="jumbotron pl-5">
      <h1 className="display-4 text-center" id={id}>{title}</h1>
      <p className="lead text-center">{quote}</p>
    </div>
  );
}
