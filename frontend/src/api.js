// src/api.js
import axios from 'axios';

const API = axios.create({
  baseURL: 'http://localhost:8000' // URL ของ Backend FastAPI
});

export default API;
