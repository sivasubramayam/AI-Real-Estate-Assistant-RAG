import json
import os

LOG_FILE = "chat_logs.json"


def save_chat(question, project, confidence):
    log = {
    "question": question,
    "project": project,
    "confidence": round(float(confidence), 2)
}

    if os.path.exists(LOG_FILE):

        with open(LOG_FILE, "r") as f:
            data = json.load(f)

    else:
        data = []

    data.append(log)

    with open(LOG_FILE, "w") as f:
        json.dump(data, f, indent=4)