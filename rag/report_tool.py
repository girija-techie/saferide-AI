from rag.db_queries import get_recent_detections, get_summary_stats
from cloud.s3_utils import generate_presigned_url

CLASS_MAP = {0: "Helmet", 1: "No Helmet", 2: "Accident"}

def generate_html_report(detections):     
    html = """
    <html>
    <head>
        <style>
            body { font-family: Arial; padding: 20px; }
            h1 { color: #d32f2f; }
            table { border-collapse: collapse; width: 100%; }
            th, td { border: 1px solid #ddd; padding: 8px; }
            th { background-color: #f4f4f4; }
        </style>
    </head>
    <body>
        <h1>🚨 SafeRide AI – Detection Report</h1>
        <table>
            <tr>
                <th>Time</th>
                <th>Class</th>
                <th>Confidence</th>
                <th>Evidence</th>
            </tr>
    """

    for t, cls, conf, s3_url in detections:
        url = generate_presigned_url(s3_url.replace("s3://saferide-detections/", ""))
        html += f"""
            <tr>
                <td>{t}</td>
                <td>{CLASS_MAP[cls]}</td>
                <td>{conf:.2f}</td>
                <td><img src="{url}" width="250" /></td>
            </tr>
        """

    html += """
        </table>
    </body>
    </html>
    """

    return html

def generate_email_html():
    stats = get_summary_stats()
    rows = get_recent_detections(5)

    html = f"""
    <html>
    <body style="font-family: Arial;">
        <h2>🚨 SafeRide AI – Detection Report</h2>

        <h3>📊 Summary</h3>
        <ul>
            <li>Total detections: <b>{stats['total']}</b></li>
            <li>Accidents: <b>{stats['accidents']}</b></li>
            <li>No Helmet Violations: <b>{stats['no_helmet']}</b></li>
            <li>Average Confidence: <b>{stats['avg_confidence']}</b></li>
        </ul>

        <h3>📈 Detection Chart</h3>
        <img src="cid:chart">

        <h3>🖼️ Recent Evidence</h3>
        <table border="1" cellpadding="5" cellspacing="0">
            <tr>
                <th>Time</th>
                <th>Class</th>
                <th>Confidence</th>
                <th>Image</th>
            </tr>
    """

    for t, cls_id, conf, s3_url in rows:
        url = generate_presigned_url(
            s3_url.replace("s3://saferide-detections/", "")
        )
        html += f"""
        <tr>
            <td>{t}</td>
            <td>{CLASS_MAP.get(cls_id)}</td>
            <td>{conf:.2f}</td>
            <td><a href="{url}" target="_blank">View Image</a></td>
        </tr>
        """

    html += """
        </table>
    </body>
    </html>
    """

    return html

