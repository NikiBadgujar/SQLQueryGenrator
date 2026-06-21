import { useState } from "react";

function QueryInput({ onGenerate }) {
  const [question, setQuestion] = useState("");

  const handleSubmit = () => {
    if (!question.trim()) return;

    onGenerate(question);
  };

  return (
    <div>
      <textarea
        rows="5"
        placeholder="Ask in plain English..."
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
      />

      <button onClick={handleSubmit}  style={{
    backgroundColor: "red",
    color: "white",
    padding: "10px 20px",
    border: "none",
    borderRadius: "8px",
    cursor: "pointer"
  }}
>
        Generate SQL
      </button>
    </div>
  );
}

export default QueryInput;