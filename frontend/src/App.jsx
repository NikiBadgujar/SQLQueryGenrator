import { useState } from "react";
import QueryInput from "./components/QueryInput";
import SqlResult from "./components/SqlResult";
import { generateSQL } from "./services/api";

import "./App.css";

function App() {
  const [sql, setSql] = useState("");
  const [loading, setLoading] = useState(false);

  const handleGenerate = async (question) => {
    try {
      setLoading(true);

      const data = await generateSQL(question);

      setSql(data.generated_sql);
    } catch (error) {
      console.error(error);

      alert("Failed to generate SQL");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">
  <h1 className="title">
    🤖 AI SQL Generator
  </h1>

  <div className="card">
    <QueryInput onGenerate={handleGenerate} />
    <SqlResult sql={sql} />
  </div>
</div>
  );
}

export default App;