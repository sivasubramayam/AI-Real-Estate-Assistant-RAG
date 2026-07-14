# 🏠 AI Real Estate Assistant (RAG)

An intelligent AI-powered Real Estate Assistant built using **Retrieval-Augmented Generation (RAG)**. This application enables customers to instantly retrieve accurate information about real estate projects by asking questions in natural language.

Instead of manually searching through lengthy project brochures and documents, users can simply ask questions such as payment plans, amenities, floor plans, pricing, location, possession dates, builders, and more. The assistant retrieves relevant information from the knowledge base and generates reliable answers using Google's Gemini AI.

---

# 🎯 Project Objective

The objective of this project is to build an AI-powered customer support assistant for real estate companies. The assistant helps customers quickly find project-related information from official documents, reducing manual customer support effort while providing fast and accurate responses.

---

# 🚀 Features

- 🤖 AI-powered chatbot using Google Gemini
- 📄 Retrieval-Augmented Generation (RAG)
- 🔍 Semantic document search using FAISS
- 🧠 Context-aware conversation memory
- 🏘️ Multi-project support
- 📂 Project-wise filtering
- 📊 Confidence score for every response
- 📑 Source document citation
- 💬 Suggested question buttons
- 📥 Export chat as PDF
- 📈 Analytics dashboard
- 🔐 Login Authentication
- 🌐 Streamlit Web Application

---

# 🏗️ Real Estate Projects Included

- Horizon Business Park (HBP)
- SHT Residency
- UNR Heights

Users can search across all projects or select a specific project before asking questions.

---

# 💡 Example Questions

- What is the payment plan?
- Show available amenities.
- Compare HBP and SHT Residency.
- What is the possession date?
- Who is the builder?
- Show available floor plans.
- Explain the cancellation policy.
- What documents are required for booking?
- Recommend the best project.

---

# 🛠️ Tech Stack

## Frontend

- Streamlit

## Backend

- Python

## Artificial Intelligence

- Google Gemini 3.1 Flash Lite
- LangChain
- FAISS Vector Database
- HuggingFace Embeddings

## Libraries

- Streamlit
- LangChain
- LangChain Community
- LangChain Google GenAI
- HuggingFace Sentence Transformers
- FAISS
- ReportLab
- Python Dotenv

---

# 📂 Project Structure

```text
AI-Real-Estate-Assistant-RAG/
│
├── app.py
├── rag_engine.py
├── vector_store.py
├── login.py
├── analytics.py
├── dashboard.py
├── utils.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env
│
├── assets/
│   └── logo.png
│
├── data/
│   ├── hbp_payment_plan.pdf
│   ├── sht_payment_plan.pdf
│   └── unr_payment_plan.pdf
│
├── screenshots/
│   ├── login.png
│   ├── home_page.png
│   ├── project_selection.png
│   ├── scoures.png
│   ├── chunks.png
│   ├── dashboard.png
│   └── clear&export_chat.png
│
└── vector_db/
    ├── index.faiss
    └── index.pkl
```

---

# ⚙️ Installation

```bash
git clone https://github.com/sivasubramayam/AI-Real-Estate-Assistant-RAG.git
```

```bash
cd AI-Real-Estate-Assistant-RAG
```

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Create .env

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

### Run

```bash
streamlit run app.py
```

---

# 🧠 How It Works

1. User enters a question.
2. FAISS retrieves the most relevant document chunks.
3. Gemini receives the retrieved context.
4. AI generates an accurate answer.
5. Confidence score and sources are displayed.

---

# 📊 Features Implemented

- Login Authentication
- Conversation Memory
- Multi Project Filtering
- Semantic Search
- Retrieval-Augmented Generation
- Source Citations
- Confidence Score
- Analytics Dashboard
- Suggested Questions
- Export Chat to PDF
- Responsive Streamlit UI

---

# 📸 Screenshots

## 🔐 Login Page

![Login Page](screenshots/login.png)

---

## 🏠 Home Page

![Home Page](screenshots/home_page.png)

---

## 📂 Project Selection

![Project Selection](screenshots/project_selection.png)

---

## 🎯 Confidence Score

![Confidence Score](screenshots/scoures.png)

---

## 📄 Retrieved Context

![Retrieved Context](screenshots/chunks.png)

---

## 📊 Analytics Dashboard

![Analytics Dashboard](screenshots/dashboard.png)

---

## 📥 Export & Clear Chat

![Export Chat](screenshots/clear&export_chat.png)

---

# 🔮 Future Improvements

- Voice Assistant
- WhatsApp Integration
- CRM Integration
- Property Recommendation System
- Multi-language Support
- Admin Dashboard

---

# 👨‍💻 Author

**Chintala Siva Subramanyam**

B.Tech – Artificial Intelligence & Machine Learning

GitHub: https://github.com/sivasubramayam

---

# ⭐ Support

If you like this project, please give it a ⭐ on GitHub.