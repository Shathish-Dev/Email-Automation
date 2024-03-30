import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

def send_email():
    # Retrieve sender and recipient email addresses from environment variables
    sender_email = os.environ.get('SENDER_EMAIL')
    sender_name = "Shathish Bot"  # Set sender name
    to_email = os.environ.get('RECIPIENT_EMAIL')
    
    # Email content
    subject = "Daily Email Automation"
    body = "<p>Good Morning, Have a great day shathish !!</p>"

    # Set up SMTP server
    smtp_server = "smtp.gmail.com"
    smtp_port = 587  # Gmail SMTP port

    # Retrieve email login credentials from environment variables
    gmail_user = os.environ.get('GMAIL_USERNAME')
    gmail_password = os.environ.get('GMAIL_PASSWORD')

    # Create message container
    msg = MIMEMultipart()
    msg['From'] = f"{sender_name} <{sender_email}>"  # Include sender name
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach body
    msg.attach(MIMEText(body, 'html'))

    # Create SMTP session
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(gmail_user, gmail_password)
        server.sendmail(sender_email, to_email, msg.as_string())
        print("Email sent successfully")
    except Exception as e:
        print(f"Error sending email: {str(e)}")
    finally:
        server.quit()

if __name__ == "__main__":
    send_email()
