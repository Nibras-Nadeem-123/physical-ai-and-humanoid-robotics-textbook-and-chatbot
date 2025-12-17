import React, { useState, useEffect } from 'react';
import styles from './styles.module.css';
import { sendMessage } from '../../../services/api'; // Import the API service

function ChatWindow({ onClose, selectedText }) {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [sessionId, setSessionId] = useState(null); // Manage session ID
  const [consent, setConsent] = useState(false); // Manage user consent

  // Load messages and session ID from local storage on initial render
  useEffect(() => {
    const savedMessages = localStorage.getItem('chatbot_messages');
    if (savedMessages) {
      setMessages(JSON.parse(savedMessages));
    }
    const savedSessionId = localStorage.getItem('chatbot_session_id');
    if (savedSessionId) {
      setSessionId(savedSessionId);
    }
    const savedConsent = localStorage.getItem('chatbot_consent');
    if (savedConsent) {
      setConsent(JSON.parse(savedConsent));
    }
  }, []);

  // Save messages and session ID to local storage whenever they change
  useEffect(() => {
    localStorage.setItem('chatbot_messages', JSON.stringify(messages));
  }, [messages]);

  useEffect(() => {
    if (sessionId) {
      localStorage.setItem('chatbot_session_id', sessionId);
    }
  }, [sessionId]);

  useEffect(() => {
    localStorage.setItem('chatbot_consent', JSON.stringify(consent));
  }, [consent]);

  useEffect(() => {
    if (selectedText) {
      setInput(selectedText);
    }
  }, [selectedText]);

  const handleSendMessage = async () => {
    if (input.trim()) {
      const userMessage = { text: input, sender: 'user' };
      setMessages((prevMessages) => [...prevMessages, userMessage]);
      setInput('');

      try {
        const response = await sendMessage(sessionId, input, selectedText);
        setSessionId(response.session_id); // Update session ID from backend
        const botMessage = { text: response.response, sender: 'bot', sources: response.sources };
        setMessages((prevMessages) => [...prevMessages, botMessage]);
      } catch (error) {
        console.error('Error sending message:', error);
        const errorMessage = { text: 'Sorry, something went wrong. Please try again.', sender: 'bot' };
        setMessages((prevMessages) => [...prevMessages, errorMessage]);
      }
    }
  };

  const handleConsent = (hasConsented) => {
    setConsent(hasConsented);
    // Here you would typically notify the backend about the consent status
    if (hasConsented) {
      console.log('User consented to data usage.');
    } else {
      console.log('User declined data usage.');
      onClose(); // Close the chat window if consent is declined
    }
  };

  if (!consent) {
    return (
      <div className={styles.chatWindow}>
        <div className={styles.consentBanner}>
          <p>
            We use your chat history to improve our service. By clicking "Accept", you agree to our data usage policy.
          </p>
          <button onClick={() => handleConsent(true)}>Accept</button>
          <button onClick={() => handleConsent(false)}>Decline</button>
        </div>
      </div>
    );
  }

  return (
    <div className={styles.chatWindow}>
      <div className={styles.chatHeader}>
        <h3>Chatbot</h3>
        <button onClick={onClose}>X</button>
      </div>
      <div className={styles.chatBody}>
        {messages.map((msg, index) => (
          <div key={index} className={`${styles.chatMessage} ${styles[msg.sender]}`}>
            {msg.text}
            {msg.sources && msg.sources.length > 0 && (
              <div className={styles.chatSources}>
                (Sources: {msg.sources.join(', ')})
              </div>
            )}
          </div>
        ))}
      </div>
      <div className={styles.chatInput}>
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyPress={(e) => e.key === 'Enter' && handleSendMessage()}
          placeholder={selectedText ? `Ask about "${selectedText.substring(0, 20)}..."` : "Ask me anything..."}
        />
        <button onClick={handleSendMessage}>Send</button>
      </div>
    </div>
  );
}

export default ChatWindow;