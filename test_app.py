from rag_engine import ask_question

answer, sources = ask_question(
    "What is the payment plan for HBP?"
)

print(answer)

print()

print(sources)