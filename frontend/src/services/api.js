import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8000",
});

export const generateSQL = async (question) => {
  const response = await api.post("/generate-sql", {
    question,
  });

  return response.data;
};