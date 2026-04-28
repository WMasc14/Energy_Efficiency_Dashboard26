import { useState } from "react";
import Controls from "./Controls";
import Plot from "./Plot";
import { simulate } from "./api";

export default function Dashboard() {
  const [data, setData] = useState(null);

  const runSim = async (params) => {
    const result = await simulate(params);
    setData(result);
  };

  return (
    <div style={{ display: "grid", gridTemplateColumns: "300px 1fr", gap: "20px", padding: "20px" }}>
      <Controls onRun={runSim} />
      <Plot data={data} />
    </div>
  );
}