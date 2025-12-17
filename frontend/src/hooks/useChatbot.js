// Placeholder for Frontend-specific hooks
import { useState, useCallback } from 'react';
import { chatWithBot } from '../services/api';

const useChatbot = (token) => {
  const [messages, setMessages] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  const sendMessage = useCallback(async (query, context = null) => {
    setIsLoading(true);
    setError(null);
    try {
      const response = await chatWithBot(query, context, token);
      setMessages((prevMessages) => [...prevMessages, { sender: 'user', text: query }, { sender: 'bot', text: response.answer, citations: response.citations }]);
      return response;
    } catch (err) {
      setError(err);
      console.error("Failed to send message:", err);
    } finally {
      setIsLoading(false);
    }
  }, [token]);

  return { messages, isLoading, error, sendMessage };
};

export default useChatbot;
