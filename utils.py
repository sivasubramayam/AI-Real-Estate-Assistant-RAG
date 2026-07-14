from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def export_chat(messages, filename="chat_history.pdf"):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    elements = []

    title = Paragraph("<b>Real Estate AI Assistant</b>", styles["Title"])

    elements.append(title)

    elements.append(Paragraph("<br/><br/>", styles["Normal"]))

    for message in messages:

        role = message["role"].capitalize()

        content = message["content"]

        text = f"<b>{role}:</b><br/>{content}<br/><br/>"

        elements.append(
            Paragraph(text, styles["BodyText"])
        )

    doc.build(elements)

    return filename