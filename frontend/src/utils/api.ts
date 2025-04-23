import axios from 'axios';
import { getToken, refreshAccessToken, logout } from './auth';

const VITE_API_BASE_UR = import.meta.env.VITE_API_BASE_UR;

export const apiClient = axios.create({
  baseURL: VITE_API_BASE_UR,
  headers: {
    'Content-Type': 'application/json',
  },
});

// 🔁 Auto-refresh logic for expired access token
apiClient.interceptors.response.use(
  response => response,
  async error => {
    const originalRequest = error.config;

    // If 401 and not already retried
    if (error.response?.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;
      try {
        const newAccessToken = await refreshAccessToken();
        // Set new token in header and retry
        originalRequest.headers['Authorization'] = `Bearer ${newAccessToken}`;
        return apiClient(originalRequest);
      } catch (err) {
        logout();
        return Promise.reject(err);
      }
    }

    return Promise.reject(error);
  }
);

apiClient.interceptors.request.use(config => {
  const token = getToken();
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});
