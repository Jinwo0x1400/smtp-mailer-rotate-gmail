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
subject = "Test Email from Rotating Gmail SMTP"
body = "This is a test email using rotated Gmail accounts."
to_email = "recipient@example.com"  # Replace with your recipient

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
