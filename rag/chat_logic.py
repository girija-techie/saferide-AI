from rag.db_queries import count_by_class, get_recent_detections
from rag.semantic_search import semantic_search
from rag.report_tool import generate_html_report
from rag.email_tool import send_email_report


def answer_question(question):
    q = question.lower()

    if "how many" in q:
        return f"Accidents: {count_by_class('2')}"

    if "recent" in q:
        rows = get_recent_detections()
        return "\n".join([str(r) for r in rows])

    if "risky" in q or "severe" in q:
        results = semantic_search(question)
        return "Semantic matches:\n" + "\n".join(results)

    if "show report" in q:
        rows = get_recent_detections(10)
        return generate_html_report(rows)

    if "email report" in q:
        send_email_report("fogocoj324@gamintor.com")
        return "📧 Email report sent successfully."

    return "I can answer questions about accidents, helmet violations, and reports."
