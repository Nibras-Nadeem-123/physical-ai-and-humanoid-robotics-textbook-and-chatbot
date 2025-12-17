// frontend/src/pages/chat.js
import React, { useState } from 'react';
import Layout from '@theme/Layout';
import { AuthProvider, useAuth } from '../hooks/useAuth';
import ChatComponent from '../components/Chat'; // Renamed to avoid conflict with function
import styles from './chat.module.css'; // We will create this CSS module

function LoginPage() {
  const { signIn, loading } = useAuth();
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    const success = await signIn(username, password);
    if (!success) {
      setError('Login failed. Please check your credentials.');
    }
  };

  return (
    <div className={styles.loginContainer}>
      <h1 className={styles.title}>Login to Chatbot</h1>
      <form onSubmit={handleSubmit} className={styles.loginForm}>
        <input
          type="text"
          placeholder="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          disabled={loading}
          className={styles.inputField}
        />
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          disabled={loading}
          className={styles.inputField}
        />
        <button type="submit" disabled={loading} className={styles.loginButton}>
          {loading ? 'Logging in...' : 'Login'}
        </button>
        {error && <p className={styles.errorMessage}>{error}</p>}
      </form>
      <p className={styles.note}>
        Note: For demonstration, use username "testuser" and password "testpassword".
      </p>
    </div>
  );
}

function ChatPageContent() {
  const { isAuthenticated, loading } = useAuth();

  if (loading) {
    return (
      <div className={styles.loadingContainer}>
        <p>Loading authentication status...</p>
      </div>
    );
  }

  if (!isAuthenticated) {
    return <LoginPage />;
  }

  return <ChatComponent />;
}

export default function ChatPage() {
  return (
    <Layout title="Chatbot" description="Chat with our AI assistant">
      <main>
        <AuthProvider>
          <ChatPageContent />
        </AuthProvider>
      </main>
    </Layout>
  );
}
