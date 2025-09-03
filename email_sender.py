import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Gmail credentials
sender_email = # your email
password = # Your Google App Password

# List of recipients
recipients = ["person1@gmail.com", "person2@gmail.com", "person3@gmail.com"]

# Email subject & body
subject = "Personal Email from Python"
body = "Hello,\n\nThis is a personalized email sent just to you!"

try:
    # Connect to Gmail SMTP server
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, password)

    for recipient in recipients:
        # Create a new message for each recipient
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = recipient
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        server.sendmail(sender_email, recipient, message.as_string())
        print(f"✅ Email sent to {recipient}")

    server.quit()
    print("📨 All emails sent successfully!")

except Exception as e:
    print(f"❌ Error: {e}")

