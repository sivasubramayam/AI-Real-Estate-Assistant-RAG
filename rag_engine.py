import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st

load_dotenv()

try:
    GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
except Exception:
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY not found. Please configure it in .env or Streamlit Secrets.")
#GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# -----------------------------
# Load Embeddings
# -----------------------------
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# -----------------------------
# Load FAISS
# -----------------------------
vector_db = FAISS.load_local(
    "vector_db",
    embeddings,
    allow_dangerous_deserialization=True
)

retriever = vector_db.as_retriever(search_kwargs={"k": 3})

# -----------------------------
# Load Gemini
# -----------------------------
#llm = ChatGoogleGenerativeAI(
    #model="gemini-3.1-flash-lite",
    #google_api_key=GOOGLE_API_KEY,
    #temperature=0.3
#)
#llm = ChatGoogleGenerativeAI(
    #model="gemini-2.5-flash",
    #google_api_key=GOOGLE_API_KEY,
    #temperature=0.3
#)

llm = ChatGoogleGenerativeAI(
    model="models/gemini-3.1-flash-lite",
    google_api_key=GOOGLE_API_KEY,
    temperature=0.3
)

# -----------------------------
# Ask Question Function
# -----------------------------
# -----------------------------
# Ask Question Function
# -----------------------------
#def ask_question(question, chat_history=[]):
def ask_question(question, history, project):
    comparison_words = [
    "compare",
    "difference",
    "vs",
    "versus"
]
    is_comparison = any(word in question.lower() for word in comparison_words)

    recommendation_words = [
    "recommend",
    "suggest",
    "best",
    "which project",
    "which property",
    "which one",
    "suitable",
    "good for me"
]

    is_recommendation = any(word in question.lower() for word in recommendation_words)

    # Retrieve relevant documents
    #docs = retriever.invoke(question)
    #docs = retriever.invoke(question)
    #docs_with_scores = vector_db.similarity_search_with_score(question,k=3)
    if is_comparison or is_recommendation:
        docs_with_scores = vector_db.similarity_search_with_score(
            question,
            k=8
    )
    else:
        docs_with_scores = vector_db.similarity_search_with_score(
        question,
        k=3
    )
    docs = []
    scores = []

    for doc, score in docs_with_scores:
        docs.append(doc)
        scores.append(score)
    filtered_docs = []
    if project != "Search All Projects":
        for doc in docs:

            source = doc.metadata["source"].lower()

            if project == "Horizon Business Park" and "hbp" in source:
                filtered_docs.append(doc)

            elif project == "SHT Residency" and "sht" in source:
                filtered_docs.append(doc)

            elif project == "UNR Heights" and "unr" in source:
                filtered_docs.append(doc)

        if filtered_docs:
            docs = filtered_docs

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    # Convert chat history to text
    history_text = ""

    for user_msg, ai_msg in history[-6:]:

        history_text += f"""
    User: {user_msg}

    Assistant: {ai_msg}

    """

    prompt = f"""
You are a professional AI Real Estate Assistant.

Your responsibilities:

- Answer ONLY from the provided knowledge base.
- Use the previous conversation if the user asks follow-up questions.
- Never make up information.
- If the answer is unavailable, politely say:
  "I couldn't find this information in the provided knowledge base."
- Answer in a professional and concise manner.
- Use bullet points whenever appropriate.
- If the user asks to compare two or more projects:
    - Create a well-formatted Markdown comparison table.
    - Compare only using the provided knowledge base.
    - If any information is missing, write "Not Available".
- Mention the project name whenever appropriate.
- Do not include information that is not present in the retrieved documents.
- If the user asks for a recommendation:
    - Recommend ONLY from the available projects.
    - Explain WHY the project is recommended.
    - Mention the advantages.
    - Do not recommend projects without supporting information.

------------------------

Previous Conversation

{history_text}

------------------------

Knowledge Base

{context}

------------------------

Current User Question

{question}

------------------------

Answer:
"""

    response = llm.invoke(prompt)

    if isinstance(response.content, list):

        answer = ""

        for item in response.content:

            if isinstance(item, dict):

                if item.get("type") == "text":
                    answer += item["text"]

    else:
        answer = response.content

    sources = list(
        {
            os.path.basename(doc.metadata["source"])
            for doc in docs
        }
    )
    confidence = round(
        (1 / (1 + scores[0])) * 100,
        2
    )

    return answer, sources, confidence , docs