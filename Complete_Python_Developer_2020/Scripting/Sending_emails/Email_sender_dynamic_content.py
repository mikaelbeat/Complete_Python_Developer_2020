
import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path


html = Template(Path("Index.html").read_text())

email = EmailMessage()
email["from"] = "Super Lottery"
email["to"] = "ryynanenphm@gmail.com"
email["subject"] = "You have won 1,000,000€!"

email.set_content(html.substitute(name="TinTin"), "html")

with smtplib.SMTP(host = "smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("email_address","password")
    smtp.send_message(email)
    print("Email sent!")
