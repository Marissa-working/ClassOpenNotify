!pip install requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests

def check_class_status():
    url = "https://public.enroll.wisc.edu/api/search/v1/enrollmentPackages/1244/412/008122"
    response = requests.get(url)

    if response.status_code == 200:
        data = dict(response.json()[0])
        status = data.get("packageEnrollmentStatus", {}).get("status")

        if status == "CLOSED":
            notify_user("Class is closed!")
            #send_email_notification("Class is closed.")
        else:
            send_email_notification("Class is open!!!!")
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

def notify_user(message):
    print(f"Notification: {message}")

def send_email_notification(message):
    sender_email = "***********"
    receiver_email = "***********"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = "***********"
    smtp_password = "***********"

    subject = "Class Enroll Status Notification"
    body = message

    # Create the email message
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    # Connect to the SMTP server
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

if __name__ == "__main__":
    check_class_status()

