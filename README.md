# 📧 SMTP Mailer with Gmail Rotation
Copyright © Jinwo0x1400

This project demonstrates how to send emails using **rotating Gmail SMTP accounts** to avoid rate limits and improve delivery success.

---

## 📋 Features

- Rotate between multiple Gmail accounts
- Secure login using App Passwords
- Send email to one or many recipients
- Log email status

---

## 🔧 Step-by-Step Setup

### 1. Enable SMTP Access in Gmail

Go to:
https://myaccount.google.com/security

- Turn ON 2-Step Verification
- Scroll down to **App Passwords**
- Create an App Password for "Mail"
- Save the password securely

---

### 2. Prepare Your Gmail Accounts

Edit `accounts.json` with the following format:

```json
[
  {
    "email": "yourgmail1@gmail.com",
    "password": "yourapppassword1"
  },
  {
    "email": "yourgmail2@gmail.com",
    "password": "yourapppassword2"
  }
]
```

---

### 3. Run the Mailer

```bash
python mailer.py
```

---

## 📎 Notes

- Gmail App Password is required; regular password will not work.
- Avoid using more than 5 emails per minute per account.

---

## ⚠️ Legal

Use this responsibly. Do not send unsolicited or spam emails.

---
**Copyright © Jinwo0x1400**
