# import smtplib


# def send_mail(message):
#     smtp_server = "smtp.gmail.com"
#     port = 587
#     sender_email = "lakshya21062@iiitd.ac.in"
#     receiver_email = ""
#     password = "axvfmkmjmfnzsogl"

#     try:
#         with smtplib.SMTP(smtp_server, port) as server:
#             server.starttls()
#             server.login(sender_email, password)
#             server.sendmail(sender_email, receiver_email, message)
#         print("Email sent successfully!")
#     except Exception as e:
#         print("Error sending email:", str(e))

# message = "Hey there! Just testing the email functionality."
# send_mail(message)

import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_email(sender_email, receiver_email, subject, message):
    message = Mail(
        from_email=sender_email,
        to_emails=receiver_email,
        subject=subject,
        plain_text_content=message)

    try:
        sg = SendGridAPIClient(api_key=os.environ.get('SSG.Y94s94GvTWiw3zoDxppS2A.y71sLUw5TiGmAi4XkoOGDBl69z74XuJArq3PV1Ik3YY'))
        response = sg.send(message)
        print("Email sent successfully!")
        print("Response status code:", response.status_code)
    except Exception as e:
        print("Error sending email:", str(e))

# Example usage
sender_email = "lakshya21062@iiitd.ac.in"
receiver_email = "lakshyasharaniiitd@gmail.com"
subject = "Testing SendGrid"
message = "Hey there! Just testing the SendGrid email functionality."

send_email(sender_email, receiver_email, subject, message)
