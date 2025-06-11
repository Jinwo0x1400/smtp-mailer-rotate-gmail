import smtplib
import json
import random
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Load accounts
with open("accounts.json") as f:
    accounts = json.load(f)

# Email content
subject = "Meeting Schedule Update"

body = """\
Hi [Recipient Name],

Just a quick update on our meeting schedule. We’ll move it to Thursday at 10 AM instead of Friday. Let me know if that still works for you.

Best regards,  
Jinwoo  
"""
to_email = "yourclient@example.com"


def send_email(account):
    try:
        msg = MIMEMultipart()
        msg["From"] = account["email"]
        msg["To"] = to_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(account["email"], account["password"])
        server.send_message(msg)
        server.quit()
        print(f"[✓] Sent from {account['email']}")
    except Exception as e:
        print(f"[✗] Failed from {account['email']}: {e}")

# Send using each account
for account in accounts:
    send_email(account)
    time.sleep(10)  # Delay between emails
