import smtplib
import json
import random
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Load accounts
with open("accounts.json") as f:
    accounts = json.load(f)

# Configurable
subject = "Meeting Schedule Update"
body = """\
Hi there,

Just a quick update on our meeting schedule. We’ll move it to Thursday at 10 AM instead of Friday. Let me know if that still works for you.

Best regards,  
Jinwoo  
"""

# List of recipient emails
recipients = [
    "recipient1@example.com",
    "recipient2@example.com"
]

def send_email(account, to_email):
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
        print(f"[✓] Sent to {to_email} from {account['email']}")
    except Exception as e:
        print(f"[✗] Failed to {to_email} from {account['email']}: {e}")

# Rotating send logic
for account in accounts:
    for recipient in recipients:
        send_email(account, recipient)
        time.sleep(10)  # Delay between recipients (per account)
    print(f"[~] Waiting before switching account...\n")
    time.sleep(30)  # Delay before next account rotation
