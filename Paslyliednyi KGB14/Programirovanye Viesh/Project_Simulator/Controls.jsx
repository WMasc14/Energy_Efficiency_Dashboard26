import { useState } from "react";

export default function Controls({ onRun }) {
  const [params, setParams] = useState({
    CA0: 2,
    F: 1,
    V: 10,
    k: 0.3,
    time: 20
  });

  return (
    <div>
      <h2>Controls</h2>

      {Object.keys(params).map((key) => (
        <div key={key} style={{ marginBottom: "10px" }}>
          <label>{key}</label>
          <input
            type="number"
            value={params[key]}
            onChange={(e) => setParams({ ...params, [key]: +e.target.value })}
          />
        </div>
      ))}

      <button onClick={() => onRun(params)}>
        Run Simulation
      </button>
    </div>
  );
}