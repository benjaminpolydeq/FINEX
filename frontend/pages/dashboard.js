import { useState } from "react";
import axios from "axios";

export default function Dashboard() {
  const [file, setFile] = useState(null);
  const [category, setCategory] = useState("Finance");
  const [type, setType] = useState("CSV");

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append("file", file);
    formData.append("category", category);
    formData.append("type", type);
    formData.append("user_id", 1); // ID d'exemple

    const res = await axios.post("http://localhost:8000/contributions/", formData, {
      headers: { "Content-Type": "multipart/form-data" },
    });
    alert(res.data.msg);
  };

  return (
    <div>
      <h1>FinEx - Dashboard Collaborateur</h1>
      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <select onChange={(e) => setCategory(e.target.value)}>
        <option value="Finance">Finance</option>
      </select>
      <select onChange={(e) => setType(e.target.value)}>
        <option value="CSV">CSV</option>
        <option value="Report">Report</option>
        <option value="Annotation">Annotation</option>
      </select>
      <button onClick={handleUpload}>Upload Contribution</button>
    </div>
  );
}