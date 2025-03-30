import axios from 'axios';
import { getToken } from './auth';

const API_BASE_URL = 'http://localhost:8000/api'; // Update with backend URL

export const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

apiClient.interceptors.request.use((config) => {
  const token = getToken();
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});