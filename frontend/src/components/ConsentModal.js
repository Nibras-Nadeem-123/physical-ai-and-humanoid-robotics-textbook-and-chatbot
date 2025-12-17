// frontend/src/components/ConsentModal.js
import React from 'react';
import { useAuth } from '../hooks/useAuth';

function ConsentModal({ isOpen, onClose }) {
  const { user, giveConsent } = useAuth();

  if (!isOpen) return null;

  const handleConsent = async (consented) => {
    const success = await giveConsent(consented);
    if (success) {
      onClose();
    } else {
      // Handle error, e.g., show a toast message
      alert('Failed to update consent. Please try again.');
    }
  };

  return (
    <div style={modalOverlayStyle}>
      <div style={modalContentStyle}>
        <h2>Data Usage Consent</h2>
        <p>
          To use the chatbot, you must consent to our data usage policy.
          This means your chat interactions may be used to improve the chatbot's performance.
        </p>
        <div style={buttonContainerStyle}>
          <button onClick={() => handleConsent(true)} style={consentButtonStyle}>
            I Consent
          </button>
          <button onClick={() => handleConsent(false)} style={denyButtonStyle}>
            I Do Not Consent
          </button>
        </div>
      </div>
    </div>
  );
}

const modalOverlayStyle = {
  position: 'fixed',
  top: 0,
  left: 0,
  right: 0,
  bottom: 0,
  backgroundColor: 'rgba(0, 0, 0, 0.7)',
  display: 'flex',
  alignItems: 'center',
  justifyContent: 'center',
  zIndex: 1000,
};

const modalContentStyle = {
  backgroundColor: '#333', // Dark background for the modal
  padding: '30px',
  borderRadius: '8px',
  boxShadow: '0 4px 10px rgba(0, 0, 0, 0.3)',
  color: '#fff', // White text
  maxWidth: '500px',
  textAlign: 'center',
};

const buttonContainerStyle = {
  marginTop: '20px',
  display: 'flex',
  justifyContent: 'space-around',
};

const consentButtonStyle = {
  backgroundColor: '#4CAF50', // Green
  color: 'white',
  padding: '10px 20px',
  border: 'none',
  borderRadius: '5px',
  cursor: 'pointer',
  fontSize: '16px',
};

const denyButtonStyle = {
  backgroundColor: '#f44336', // Red
  color: 'white',
  padding: '10px 20px',
  border: 'none',
  borderRadius: '5px',
  cursor: 'pointer',
  fontSize: '16px',
};


export default ConsentModal;