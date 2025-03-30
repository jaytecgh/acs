import axios from 'axios';
import { jwtDecode } from "jwt-decode";

const API_BASE_URL = 'http://localhost:8000/api/auth'; // Update with your backend auth URL

export const login = async (email: string, password: string) => {
  try {
    const response = await axios.post(`${API_BASE_URL}/login/`, { email, password });
    localStorage.setItem('token', response.data.access);
    return response.data;
  } catch (error) {
    throw error;
  }
};

export const logout = () => {
  localStorage.removeItem('token');
};

export const getToken = (): string | null => {
  return localStorage.getItem("token");
};

export const getUser = () => {
  const token = getToken();
  if (!token) return null;
  return jwtDecode(token);
};

export const getUserRole = (): string | null => {
  const token = getToken();
  if (!token) return null;
  
  const decoded: any = jwtDecode(token);
  return decoded.role || null;
};

export const isAuthenticated = () => {
  return !!getToken();
};
