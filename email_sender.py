from email.message import EmailMessage
from env import google_code, email
import ssl
import smtplib

email_sender = email
email_password = google_code

email_receiver = 'alexbrkk0099@gmail.com'
subject = "Talk me"
body = """
Hello its me, Luis :)
"""

em = EmailMessage()

em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)


context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
