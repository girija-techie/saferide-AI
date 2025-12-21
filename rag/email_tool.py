import os
import smtplib
from email.message import EmailMessage
from email.utils import make_msgid

from rag.chart_tool import generate_chart
from rag.report_tool import generate_email_html

EMAIL = os.getenv("EMAIL_ID")
PASSWORD = os.getenv("EMAIL_APP_PASSWORD")


def send_email_report(to_email):
    # Generate chart and HTML
    chart_path = generate_chart()
    html = generate_email_html()

    # Create email
    msg = EmailMessage()
    msg["Subject"] = "🚨 SafeRide AI – Detection Report"
    msg["From"] = EMAIL
    msg["To"] = to_email

    # Plain-text fallback (IMPORTANT)
    msg.set_content(
        "SafeRide AI Detection Report.\n"
        "Please view this email in an HTML-compatible client."
    )

    # Create CID for inline image
    image_cid = make_msgid(domain="saferide.ai")

    # Attach HTML version
    msg.add_alternative(
        html.replace("cid:chart", f"cid:{image_cid[1:-1]}"),
        subtype="html"
    )

    # Attach chart image as related content
    with open(chart_path, "rb") as f:
        msg.get_payload()[1].add_related(
            f.read(),
            maintype="image",
            subtype="png",
            cid=image_cid
        )

    # Send email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL, PASSWORD)
        server.send_message(msg)
