// frontend/src/components/Chat.js
import React, { useState, useEffect, useRef } from 'react';
import { useAuth } from '../hooks/useAuth';
import { chatWithBot } from '../services/api';
import ConsentModal from './ConsentModal';
import './Chat.css'; // We will create this CSS file

function Chat() {
  const { user, isAuthenticated, signOut } = useAuth();
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const [session_id, setSessionId] = useState(null);
  const [showConsentModal, setShowConsentModal] = useState(false);

  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  useEffect(() => {
    if (isAuthenticated && user && user.hasConsented === false) {
      setShowConsentModal(true);
    } else {
      setShowConsentModal(false);
    }
  }, [isAuthenticated, user]);


  const handleSendMessage = async (e) => {
    e.preventDefault();
    if (!input.trim() || loading || !isAuthenticated) return;

    if (!user || user.hasConsented === false) {
      setShowConsentModal(true);
      return;
    }

    const newMessage = { role: 'user', content: input };
    setMessages((prevMessages) => [...prevMessages, newMessage]);
    setInput('');
    setLoading(true);

    try {
      const history = messages.map(msg => ({role: msg.role, content: msg.content}));
      const response = await chatWithBot(input, session_id, history);
      setMessages((prevMessages) => [...prevMessages, { role: 'assistant', content: response.response }]);
      if (!session_id) {
        setSessionId(response.session_id);
      }
    } catch (error) {
      console.error('Error sending message:', error);
      setMessages((prevMessages) => [
        ...prevMessages,
        { role: 'assistant', content: 'Sorry, something went wrong. Please try again.' },
      ]);
    } finally {
      setLoading(false);
    }
  };

  if (!isAuthenticated) {
    return <p>Please log in to use the chatbot.</p>;
  }

  return (
    <div className="chat-container">
      <ConsentModal isOpen={showConsentModal} onClose={() => setShowConsentModal(false)} />
      <div className="chat-header">
        <h2>AI Chatbot</h2>
        <button onClick={signOut} className="logout-button">Logout</button>
      </div>
      <div className="chat-messages">
        {messages.map((msg, index) => (
          <div key={index} className={`chat-message ${msg.role}`}>
            <strong>{msg.role === 'user' ? 'You:' : 'Bot:'}</strong> {msg.content}
          </div>
        ))}
        {loading && <div className="chat-message assistant"><strong>Bot:</strong> Thinking...</div>}
        <div ref={messagesEndRef} />
      </div>
      <form onSubmit={handleSendMessage} className="chat-input-form">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type your message..."
          disabled={loading || !user?.hasConsented}
        />
        <button type="submit" disabled={loading || !user?.hasConsented}>
          Send
        </button>
      </form>
    </div>
  );
}

export default Chat;