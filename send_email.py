import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
import os
from config import *

# Email details
sender_email = SENDER_EMAIL
receiver_email = RECEIVER_EMAIL
subject = "2025 Jubilee - Pilgrims of Hope"
body = """Hey bro,

Hope you're well.

Whatever the situation right now, you got it! 

Keep your head held up high - Hope does not disappoint!"""

# SMTP server details (for Gmail)
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = GMAIL_USERNAME
smtp_password = GMAIL_PASSWORD

# File paths (image and PDF in the same folder as the script)
script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, "2025 jubilee-pilgrims of hope VISION Board.png")
pdf_path = os.path.join(script_dir, "Pilgrims of Hope.pdf")

# Create the email
msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = subject

# Add body
msg.attach(MIMEText(body, "plain"))

# Attach image
with open(image_path, "rb") as img:
    image = MIMEImage(img.read(), name=os.path.basename(image_path))
    msg.attach(image)

# Attach PDF
with open(pdf_path, "rb") as pdf:
    attach = MIMEApplication(pdf.read(), _subtype="pdf")
    attach.add_header("Content-Disposition", "attachment", filename=os.path.basename(pdf_path))
    msg.attach(attach)

# Send the email
try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Upgrade the connection to secure
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
    print("Email sent successfully!")
except Exception as e:
    print(f"Error: {e}")