# 🏠 AI Real Estate Assistant (RAG)

An intelligent Real Estate AI Assistant built using **Retrieval-Augmented Generation (RAG)** that helps customers instantly retrieve accurate information about real estate projects from PDF documents.

The assistant answers questions related to payment plans, amenities, floor plans, locations, possession dates, pricing, builders, and other project details using Google's Gemini AI and a FAISS vector database.

---

## 🚀 Features

- 🤖 AI-powered chatbot using Google Gemini
- 📄 PDF document-based knowledge base
- 🔍 Semantic search using FAISS Vector Database
- 🧠 Context-aware conversation memory
- 🏘️ Multi-project support
- 📊 Confidence score for every answer
- 📑 Source document citation
- 📂 Project-wise filtering
- 📥 Export chat as PDF
- 📈 Analytics dashboard
- 💬 Suggested question buttons
- 🔐 Login Authentication
- 🌐 Streamlit Web Application

---

## 🏗️ Projects Included

- Horizon Business Park (HBP)
- SHT Residency
- UNR Heights

Users can search within a specific project or across all projects.

---

## 🛠️ Tech Stack

### Frontend
- Streamlit

### Backend
- Python

### AI & RAG
- Google Gemini
- LangChain
- FAISS
- HuggingFace Embeddings

### Libraries
- sentence-transformers
- langchain-google-genai
- langchain-community
- reportlab
- python-dotenv

---

## 📁 Project Structure

```text
RealEstate-RAG/
│
├── app.py
├── rag_engine.py
├── vector_store.py
├── login.py
├── analytics.py
├── utils.py
├── requirements.txt
├── README.md
│
├── assets/
├── data/
├── vector_db/
│
└── .env
