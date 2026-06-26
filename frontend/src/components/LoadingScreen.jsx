export default function LoadingScreen() {
  return (
    <div id="loading" className="row" style={{ minHeight: '80vh' }}>
      <div className="my-auto text-center">
        <p>LOADING</p>
        <div className="spinner-border text-success" role="status">
          <span className="sr-only">Loading...</span>
        </div>
      </div>
    </div>
  );
}
