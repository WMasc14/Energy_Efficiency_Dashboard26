import axios from "axios";

export const simulate = async (params) => {
  const res = await axios.post("http://localhost:8000/simulate", params);
  return res.data;
};