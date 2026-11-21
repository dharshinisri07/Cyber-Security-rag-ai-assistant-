# Cybersecurity RAG AI Assistant

A Retrieval-Augmented Generation (RAG) based AI assistant designed to provide context-aware answers to cybersecurity-related questions using semantic search and Google's Gemini large language model.

## 1. Overview

The Cybersecurity RAG AI Assistant integrates information retrieval and generative AI to answer questions within the cybersecurity domain.

The application retrieves relevant information from a custom cybersecurity knowledge base using FAISS vector similarity search and uses the retrieved context to generate informative responses through Google Gemini.

The project demonstrates the practical implementation of RAG architecture, text embeddings, vector databases, and large language models.

## 2. Objectives

- Develop a domain-specific AI assistant for cybersecurity knowledge.
- Implement Retrieval-Augmented Generation to improve response relevance.
- Build a searchable cybersecurity knowledge base.
- Integrate semantic search using vector embeddings and FAISS.
- Generate context-aware responses using Google Gemini.
- Develop an interactive chatbot interface.

## 3. Key Features

- **Retrieval-Augmented Generation:** Retrieves relevant knowledge before generating responses.
- **Custom Knowledge Base:** Uses a dataset containing 120 cybersecurity question-and-answer records.
- **Semantic Search:** Identifies relevant information using vector similarity.
- **Text Embeddings:** Uses the Sentence Transformers model `all-MiniLM-L6-v2`.
- **Vector Database:** Uses FAISS for efficient similarity-based retrieval.
- **LLM Integration:** Uses Google Gemini for response generation.
- **Interactive Interface:** Provides a conversational interface using Gradio.
- **Source-Aware Responses:** Includes retrieved source information with generated answers.

## 4. Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| Generative AI | Google Gemini |
| RAG Framework | LangChain |
| Embedding Model | Sentence Transformers |
| Vector Database | FAISS |
| User Interface | Gradio |
| Dataset Format | JSON |
| Environment Management | Python Virtual Environment |

## 5. System Architecture

The application follows a Retrieval-Augmented Generation pipeline.

1. **Knowledge Base Preparation:** Loads cybersecurity question-and-answer data.
2. **Text Processing:** Processes and splits the knowledge base into manageable text chunks.
3. **Embedding Generation:** Converts text chunks into numerical vector representations.
4. **Vector Database Creation:** Stores embeddings in a FAISS vector database.
5. **Query Processing:** Accepts a cybersecurity question from the user.
6. **Information Retrieval:** Retrieves the most relevant information using similarity search.
7. **Response Generation:** Passes the retrieved context and user query to Google Gemini.
8. **Response Presentation:** Displays the generated answer and source information through Gradio.

## 6. Project Structure

```text
Cyber-Security-RAG-AI-Assistant/
│
├── app.py
├── build_knowledge_base.py
├── requirements.txt
│
├── data/
│   └── QA/
│       ├── cybersecurity_qa.json
│       └── add_questions.py
│
├── src/
│   ├── document_loader.py
│   ├── embeddings.py
│   ├── llm.py
│   ├── rag_chain.py
│   ├── retriever.py
│   ├── text_splitter.py
│   └── vector_store.py
│
├── .gitignore
└── README.md
```

## 7. Installation and Execution

### Prerequisites

- Python 3.10 or later
- Google Gemini API key
- Git

### Step 1: Clone the Repository

```bash
git clone https://github.com/dharshinisri07/Cyber-Security-rag-ai-assistant-.git
```

### Step 2: Navigate to the Project Directory

```bash
cd Cyber-Security-rag-ai-assistant-
```

### Step 3: Create and Activate a Virtual Environment

```bash
python -m venv .venv
```

For Windows PowerShell:

```powershell
.venv\Scripts\activate
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Configure Environment Variables

Create a `.env` file in the root directory and add your Gemini API key:

```env
GOOGLE_API_KEY=your_gemini_api_key
```

Do not commit your actual API key or `.env` file to GitHub.

### Step 6: Build the Knowledge Base

```bash
python build_knowledge_base.py
```

This generates the local FAISS vector database required for information retrieval.

### Step 7: Launch the Application

```bash
python app.py
```

Open the local Gradio URL displayed in the terminal, typically:

`http://127.0.0.1:7860`

## 8. Working Principle

The system uses the following workflow:

```text
User Query
    |
    v
Query Processing
    |
    v
Embedding Generation
    |
    v
FAISS Similarity Search
    |
    v
Relevant Context Retrieval
    |
    v
Google Gemini
    |
    v
Context-Aware Response
    |
    v
Gradio Interface
```

## 9. Future Enhancements

- Integrate additional cybersecurity datasets and research documents.
- Expand PDF-based knowledge retrieval.
- Improve retrieval relevance and response evaluation.
- Implement conversation history and contextual follow-up questions.
- Explore integration with cybersecurity analysis tools.

## 10. Author

Dharshini Sri S.

MSc Artificial Intelligence and Cyber Security  
CHRIST University, Bangalore

GitHub: [dharshinisri07](https://github.com/dharshinisri07)

---

This project was developed as a practical implementation of Retrieval-Augmented Generation for domain-specific cybersecurity applications.
