# send report by email
from decouple import config

def send_report(email: str, subject: str, HTMLcontent: str) -> None:
    """
    Simule l'envoi d'email en mode développement
    """
    print("=== Email Simulation ===")
    print(f"To: {email}")
    print(f"Subject: {subject}")
    print(f"Content: {HTMLcontent}")
    print("=== End Simulation ===")
    return None
