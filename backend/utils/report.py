from .send_report import send_report

async def report_pipeline(email: str, cars_num: int) -> None:
    """
    Pipeline de génération et envoi de rapport
    """
    subject = "FARM Cars Report"
    html_content = f"<p>Rapport pour {cars_num} voitures</p>"
    send_report(email, subject, html_content)
