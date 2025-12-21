import matplotlib.pyplot as plt
from rag.db_queries import get_summary_stats

def generate_chart():
    stats = get_summary_stats()

    labels = ["Accidents", "No Helmet"]
    values = [stats["accidents"], stats["no_helmet"]]

    plt.figure()
    plt.bar(labels, values)
    plt.title("Detection Distribution")
    plt.tight_layout()

    chart_path = "report_chart.png"
    plt.savefig(chart_path)
    plt.close()

    return chart_path
