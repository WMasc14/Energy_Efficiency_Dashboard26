import { LineChart, Line, XAxis, YAxis, Tooltip } from "recharts";

export default function Plot({ data }) {
  if (!data) return <div>Run simulation to see results</div>;

  const chartData = data.time.map((t, i) => ({
    time: t,
    CA: data.CA[i]
  }));

  return (
    <div>
      <h2>Results</h2>
      <LineChart width={700} height={400} data={chartData}>
        <XAxis dataKey="time" />
        <YAxis />
        <Tooltip />
        <Line type="monotone" dataKey="CA" stroke="#00ffcc" />
      </LineChart>
    </div>
  );
}