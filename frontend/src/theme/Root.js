// Root.js is a Docusaurus theme component that wraps the entire application.
// We can use it to inject our chatbot widget.
import React from 'react';
import Chatbot from '@site/src/components/Chatbot'; // Adjust path as necessary

function Root({ children }) {
  // You might want to conditionally render the chatbot or control its visibility
  // For demonstration, we'll render it directly.
  return (
    <>
      {children}
      <div style={{ position: 'fixed', bottom: 20, right: 20, zIndex: 1000 }}>
        <Chatbot />
      </div>
    </>
  );
}

export default Root;
