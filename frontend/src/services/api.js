// Placeholder for Frontend API Client
const API_BASE_URL = process.env.REACT_APP_API_BASE_URL || 'http://localhost:8000/api/v1';

const getToken = () => localStorage.getItem('access_token');
const setToken = (token) => localStorage.setItem('access_token', token);
const removeToken = () => localStorage.removeItem('access_token');

export const loginUser = async (username, password) => {
  const formBody = new URLSearchParams();
  formBody.append('username', username);
  formBody.append('password', password);

  const response = await fetch(`${API_BASE_URL}/auth/login`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: formBody.toString(),
  });
  if (!response.ok) {
    throw new Error('Login failed');
  }
  const data = await response.json();
  setToken(data.access_token);
  return data;
};

export const chatWithBot = async (session_id, query, selected_text) => {
  const token = getToken();
  if (!token) {
    throw new Error('No authentication token found. Please log in.');
  }

  const response = await fetch(`${API_BASE_URL}/chat`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${token}`,
    },
    body: JSON.stringify({ session_id, message: query, selected_text }),
  });
  if (!response.ok) {
    throw new Error('Chat failed');
  }
  return response.json();
};

export const logoutUser = () => {
  removeToken();
};

export const isAuthenticated = () => {
  return getToken() !== null;
};