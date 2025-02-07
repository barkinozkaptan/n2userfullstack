import axios from "axios";

// Create an axios instance with your Django backend's base URL
const service = axios.create({
  baseURL: "http://127.0.0.1:8000/api", // Replace with your Django backend API base URL
});

export default service;
