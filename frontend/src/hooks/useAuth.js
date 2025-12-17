// frontend/src/hooks/useAuth.js
import React, { createContext, useState, useContext, useEffect } from 'react';
import { login, logout, updateConsent } from '../services/api'; // Adjust path if necessary

const AuthContext = createContext(null);

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null); // { username, hasConsented }
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [loading, setLoading] = useState(true); // For initial token check

  useEffect(() => {
    // Check for token in localStorage on initial load
    const token = localStorage.getItem('access_token');
    if (token) {
      // In a real app, you'd verify the token with the backend
      // For this example, we'll assume a token means authenticated
      // and fetch user details or just set a placeholder user.
      // For now, setting a dummy user for demonstration.
      setUser({ username: 'testuser', hasConsented: false }); // Will be updated by consent call
      setIsAuthenticated(true);
    }
    setLoading(false);
  }, []);

  const signIn = async (username, password) => {
    try {
      setLoading(true);
      await login(username, password);
      setUser({ username: username, hasConsented: false }); // Consent will be fetched/updated later
      setIsAuthenticated(true);
      setLoading(false);
      return true;
    } catch (error) {
      console.error('Login failed:', error);
      setLoading(false);
      return false;
    }
  };

  const signOut = () => {
    logout();
    setUser(null);
    setIsAuthenticated(false);
  };

  const giveConsent = async (consented) => {
    try {
      const updatedUser = await updateConsent(consented);
      setUser(prev => ({ ...prev, hasConsented: updatedUser.has_consented }));
      return true;
    } catch (error) {
      console.error('Consent update failed:', error);
      return false;
    }
  };

  return (
    <AuthContext.Provider value={{ user, isAuthenticated, loading, signIn, signOut, giveConsent }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  return useContext(AuthContext);
};
