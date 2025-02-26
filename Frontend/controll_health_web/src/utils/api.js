import axios from "axios";

const API_BASE_URL = "http://127.0.0.1:3001"; // Thay thế bằng URL backend của bạn

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

export const loginUser = async (email, password) => {
  const response = await api.post("/login", { email, password });
  return response.data;
};

export const registerUser = async (userData) => {
  const response = await api.post("/register", userData);
  return response.data;
};

export const fetchHealthData = async (token) => {
  const response = await api.get("/health-data", {
    headers: { Authorization: `Bearer ${token}` },
  });
  return response.data;
};

export default api;
