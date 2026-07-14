import streamlit as st
from login import login
from rag_engine import ask_question
from utils import export_chat
from analytics import save_chat

st.set_page_config(
    page_title="Real Estate AI Assistant",
    page_icon="🏠",
    layout="wide"
)

# ------------------------
# Session Variables
# ------------------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "messages" not in st.session_state:
    st.session_state.messages = []

# ------------------------
# Login
# ------------------------

if not st.session_state.logged_in:
    login()
    st.stop()

# ------------------------
# Sidebar
# ------------------------

with st.sidebar:
    st.title("🏠 Real Estate AI")
    page = st.radio(
    "Navigation",
    [
        "🏠 AI Assistant",
        "📊 Dashboard"
    ]
)

    st.image("assets/logo.png", width=120)

    st.title("🏠 Real Estate AI")

    st.markdown("---")

    st.subheader("📂 Select Project")

    project = st.selectbox(
        "",
        [
            "Search All Projects",
            "Horizon Business Park",
            "SHT Residency",
            "UNR Heights"
        ]
    )

    st.markdown("---")

    st.subheader("💡 Example Questions")

    st.markdown("""
- What is the payment plan?
- Show amenities
- What is the location?
- Compare projects
- Show floor plan
- What is the possession date?
""")

    st.markdown("---")

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")
    if st.button("📥 Export Chat"):
        pdf_file = export_chat(st.session_state.messages)

        with open(pdf_file, "rb") as file:

            st.download_button(
                "⬇ Download PDF",
                file,
                file_name="RealEstateChat.pdf",
                mime="application/pdf"
            )

    st.markdown("---")
    st.caption("Version 1.0")
# ------------------------
# Main Page
# ------------------------
if page == "🏠 AI Assistant":
    st.title("🏠 AI Real Estate Assistant")

    st.markdown(
    """
    Ask questions about:

    ✅ Payment Plans

    ✅ Amenities

    ✅ Floor Plans

    ✅ Project Location

    ✅ Construction Status

    ✅ Pricing Information
    """
    )



    if len(st.session_state.messages) == 0:

        st.info(
            """
    👋 Welcome!

    You can ask questions like:

    • Tell me about HBP.

    • What is the payment plan?

    • What amenities are available?

    • Who is the builder?

    • Explain the cancellation policy.

    • What documents are required for booking?
    """
        )

    # ------------------------
    # Display Chat History
    # ------------------------

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):
            st.markdown(message["content"])

            if "sources" in message:
                st.markdown("**📄 Sources**")

                for source in message["sources"]:
                    st.write("•", source)




    st.subheader("💡 Suggested Questions")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("💰 Payment Plan"):
            st.session_state.selected_question = "Explain the payment plan."

    with col2:
        if st.button("🏊 Amenities"):
            st.session_state.selected_question = "What amenities are available?"

    with col3:
        if st.button("📍 Location"):
            st.session_state.selected_question = "Where is the project located?"

    col4, col5, col6 = st.columns(3)

    with col4:
        if st.button("📐 Floor Plans"):
            st.session_state.selected_question = "Show available floor plans."

    with col5:
        if st.button("📞 Contact"):
            st.session_state.selected_question = "Provide contact details."

    with col6:
        if st.button("🏡 Recommend Project"):
            st.session_state.selected_question = "Recommend the best project."



    # ------------------------
    # User Input
    # ------------------------

    #question = st.chat_input("Ask your question...")
    typed_question = st.chat_input("Ask your question...")

    question = typed_question

    if "selected_question" in st.session_state:

        question = st.session_state.selected_question

        del st.session_state.selected_question

    if question:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        with st.chat_message("user"):
            st.markdown(question)

        with st.spinner("Searching documents..."):
            history = []

        for i in range(len(st.session_state.messages) - 1):

            if (
                st.session_state.messages[i]["role"] == "user"
                and
                st.session_state.messages[i + 1]["role"] == "assistant"
            ):

                history.append(
                    (
                        st.session_state.messages[i]["content"],
                        st.session_state.messages[i + 1]["content"]
                    )
                )

        answer, sources ,confidence , docs = ask_question(
        question,
        history,
        project
        )

        save_chat(
            question,
            project,
            confidence
        )
        st.session_state.messages.append(

            {
                "role": "assistant",
                "content": answer,
                "sources": sources
            }
        )

        with st.chat_message("assistant"):

            st.markdown(answer)
            #st.success(f"Confidence : {confidence}%")
            st.markdown("### 🎯 Confidence")
            st.progress(int(confidence))
            st.write(f"{confidence}%")
            st.markdown("**📄 Sources**")

        with st.expander("📄 Source Documents"):
            for source in sources:
                st.info(f"📄 {source}")
        with st.expander("Retrieved Context"):
            for i, doc in enumerate(docs):

                st.write(f"### Chunk {i+1}")

                st.write(doc.page_content)



elif page == "📊 Dashboard":

    import json
    import os
    from collections import Counter

    st.title("📊 Real Estate Analytics Dashboard")

    # ------------------------
    # Check if log file exists
    # ------------------------

    if not os.path.exists("chat_logs.json"):
        st.warning("No analytics data available yet.")
        st.stop()

    with open("chat_logs.json", "r") as f:
        data = json.load(f)

    if len(data) == 0:
        st.warning("No chat history found.")
        st.stop()

    # ------------------------
    # Metrics
    # ------------------------

    total_questions = len(data)

    avg_confidence = sum(
        item["confidence"] for item in data
    ) / total_questions

    st.subheader("📈 Overall Statistics")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Total Questions", total_questions)

    with col2:
        st.metric(
            "Average Confidence",
            f"{avg_confidence:.2f}%"
        )

    st.markdown("---")

    # ------------------------
    # Project Usage
    # ------------------------

    st.subheader("🏠 Project Usage")

    project_counter = Counter(
        item["project"] for item in data
    )

    st.bar_chart(project_counter)

    st.markdown("---")

    # ------------------------
    # Top Questions
    # ------------------------

    st.subheader("🔥 Most Asked Questions")

    question_counter = Counter(
        item["question"] for item in data
    )

    for question, count in question_counter.most_common(10):

        st.write(f"**{count}×** — {question}")

    st.markdown("---")

    # ------------------------
    # Recent Chats
    # ------------------------

    st.subheader("📝 Recent Questions")

    for item in reversed(data[-10:]):

        st.info(
            f"""
**Question:** {item['question']}

**Project:** {item['project']}

**Confidence:** {item['confidence']:.2f}%
"""
        )