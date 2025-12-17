# Embedding the Chatbot in Docusaurus

This document provides instructions on how to embed the Physical AI Textbook RAG Chatbot into your Docusaurus website.

## 1. Add Chatbot Components to Docusaurus

You will need to integrate the `FloatingButton.js` and `ChatWindow.js` components into your Docusaurus theme.

### Option A: Swizzling (Recommended for customization)

1.  **Swizzle a component**: If you want to customize how the chatbot button or window appears, you can swizzle an existing Docusaurus component (e.g., `Layout` or `Navbar`) to inject the chatbot.
    ```bash
    npx @docusaurus/theme-classic swizzle @docusaurus/theme-classic Layout --danger
    ```
2.  **Copy Chatbot components**: Copy `frontend/src/components/Chatbot/FloatingButton.js` and `frontend/src/components/Chatbot/ChatWindow.js` to a suitable location within your swizzled theme (e.g., `src/theme/Chatbot`).
3.  **Import and Render**: In your swizzled `Layout.js` (or other component), import and render the `FloatingButton` and `ChatWindow` components.

    ```javascript
    import React, { useState } from 'react';
    import Layout from '@theme-original/Layout';
    import FloatingButton from './Chatbot/FloatingButton'; // Adjust path
    import ChatWindow from './Chatbot/ChatWindow';       // Adjust path

    export default function LayoutWrapper(props) {
      const [isChatOpen, setIsChatOpen] = useState(false);
      const [selectedText, setSelectedText] = useState('');

      const toggleChat = () => setIsChatOpen(!isChatOpen);

      // Implement logic to capture selected text, e.g., on mouseup event
      // document.addEventListener('mouseup', handleTextSelection);

      return (
        <Layout {...props}>
          {props.children}
          <FloatingButton onClick={toggleChat} />
          {isChatOpen && <ChatWindow onClose={toggleChat} selectedText={selectedText} />}
        </Layout>
      );
    }
    ```

### Option B: Direct Script Injection (Simpler, less customizable)

1.  **Build Chatbot Widget**: You can build the chatbot as a standalone JavaScript bundle. (This step assumes you have a build process for the frontend widget).
2.  **Inject Script**: Add the built JavaScript file and its CSS into your Docusaurus `docusaurus.config.js` or directly into `src/pages/index.js` or a theme component.

    ```javascript
    // docusaurus.config.js
    module.exports = {
      // ... other config
      headTags: [
        {
          tagName: 'script',
          attributes: {
            src: '/path/to/your/chatbot-widget.js', // Adjust path
            defer: true,
          },
        },
        {
          tagName: 'link',
          attributes: {
            rel: 'stylesheet',
            href: '/path/to/your/chatbot-widget.css', // Adjust path
          },
        },
      ],
      // ...
    };
    ```

## 2. Configure Environment Variables

Ensure your Docusaurus build environment has access to the `REACT_APP_API_BASE_URL` pointing to your FastAPI backend.

```bash
# Example .env file for Docusaurus development
REACT_APP_API_BASE_URL="http://localhost:8000/api/v1"
```

## 3. Database Migration

Ensure your PostgreSQL database has the `users` and `agent_skills` tables created. You might use a tool like Alembic for schema migrations.

```sql
-- Example SQL for users table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    hashed_password VARCHAR(255) NOT NULL,
    has_consented BOOLEAN DEFAULT FALSE
);

-- Example SQL for agent_skills table
CREATE TABLE agent_skills (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL,
    description TEXT,
    metadata JSONB,
    is_active BOOLEAN DEFAULT TRUE
);
```

By following these steps, you can embed the chatbot into your Docusaurus textbook.
