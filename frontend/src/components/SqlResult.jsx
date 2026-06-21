function SqlResult({ sql }) {
  return (
    <div>
      <h2>Generated SQL</h2>

      <pre>
        <code>{sql}</code>
      </pre>
    </div>
  );
}

export default SqlResult;