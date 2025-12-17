// frontend/src/services/api.js

const API_BASE_URL = process.env.NODE_ENV === 'production'
  ? 'https://your-production-backend-url.com' // TODO: Replace with your production backend URL
  : 'http://localhost:8000'; // Default to localhost for development

const getAuthHeaders = () => {
  const token = localStorage.getItem('access_token');
  return token ? { Authorization: `Bearer ${token}` } : {};
};

export const login = async (username, password) => {
  const response = await fetch(`${API_BASE_URL}/api/auth/login`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: new URLSearchParams({
      username,
      password,
    }),
  });

  if (!response.ok) {
    const errorData = await response.json();
    throw new Error(errorData.detail || 'Login failed');
  }

  const data = await response.json();
  localStorage.setItem('access_token', data.access_token);
  return data;
};

export const updateConsent = async (hasConsented) => {
  const response = await fetch(`${API_BASE_URL}/api/auth/consent`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
      ...getAuthHeaders(),
    },
    body: JSON.stringify({ has_consented: hasConsented }),
  });

  if (!response.ok) {
    const errorData = await response.json();
    throw new Error(errorData.detail || 'Consent update failed');
  }

  return response.json();
};

export const chatWithBot = async (query, session_id, history) => {
  const response = await fetch(`${API_BASE_URL}/api/chat`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      ...getAuthHeaders(),
    },
    body: JSON.stringify({ query, session_id, history }),
  });

  if (!response.ok) {
    const errorData = await response.json();
    throw new Error(errorData.detail || 'Chat failed');
  }

  return response.json();
};

export const logout = () => {
  localStorage.removeItem('access_token');
};
