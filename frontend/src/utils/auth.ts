import axios from 'axios';
import { jwtDecode } from "jwt-decode";

const VITE_API_BASE_URL = import.meta.env.VITE_API_BASE_URL; // Adjust to your backend route & change when hosting

export const login = async (email: string, password: string) => {
  const response = await axios.post(`${VITE_API_BASE_URL}/auth/token/`, {
    email,
    password,
  }); 

  const { access, refresh, user } = response.data;

  localStorage.setItem("access", access);
  localStorage.setItem("refresh", refresh);
  localStorage.setItem("user", JSON.stringify(user));
};

export const register = async (email: string, password: string, full_name: string) => {
  const response = await axios.post(`${VITE_API_BASE_URL}/auth/register/`, {
    email,
    password,
    full_name,
  });
  return response.data;
};


export const requestPasswordReset = async (email: string) => {
  try {
    const response = await axios.post(`${VITE_API_BASE_URL}/auth/forgot-password/`, { email });
    return response.data;
  } catch (error) {
    throw error;
  }
};

export const resetPassword = async (token: string, newPassword: string) => {
  try {
    const response = await axios.post(`${VITE_API_BASE_URL}/auth/reset-password/`, { token, password: newPassword });
    return response.data;
  } catch (error) {
    throw error;
  }
};

export const logout = async () => {
  const refresh = localStorage.getItem("refresh");
  if (refresh) {
    await axios.post(`${VITE_API_BASE_URL}/auth/logout/`, { refresh });
  }
  localStorage.removeItem("access");
  localStorage.removeItem("refresh");
  localStorage.removeItem("user");
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
  const token = getToken();
  if (!token) return false;
  try {
    const decoded: any = jwtDecode(token);
    const exp = decoded.exp * 1000;
    return Date.now() < exp;
  } catch {
    return false;
  }
};

export const refreshAccessToken = async () => {
  const refresh = localStorage.getItem("refresh");
  if (!refresh) throw new Error("No refresh token available");

  try {
    const response = await axios.post(`${VITE_API_BASE_URL}/auth/token/refresh/`, { refresh });
    localStorage.setItem("token", response.data.access);
    return response.data.access;
  } catch (error) {
    logout();
    throw error;
  }
};

