import json
import streamlit as st

with open("chat_logs.json") as f:
    data = json.load(f)

st.title("📊 Analytics Dashboard")

st.metric(
    "Total Questions",
    len(data)
)
#show project usage
projects = {}

for item in data:

    p = item["project"]

    projects[p] = projects.get(p, 0) + 1

st.bar_chart(projects)
#average confidence
avg = sum(
    x["confidence"]
    for x in data
) / len(data)

st.metric(
    "Average Confidence",
    f"{avg:.2f}%"
)
# most asked questions 
questions = {}

for item in data:

    q = item["question"]

    questions[q] = questions.get(q, 0) + 1

st.subheader("Top Questions")

st.write(
    sorted(
        questions.items(),
        key=lambda x: x[1],
        reverse=True
    )[:5]
)