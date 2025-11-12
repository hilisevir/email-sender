import base64
from email.mime.text import MIMEText
from gmail_service import gmail_service


def send_email(destination: str, content: str):
    service = gmail_service()

    # сreate a plain text message
    message = MIMEText(content)
    message['to'] = destination
    message['subject'] = 'Automated message'
    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()

    try:
        # send the email
        sent = service.users().messages().send(
            userId="me",
            body={'raw': raw}
        ).execute()
        print(f"Email successfully sent! ID: {sent['id']}")
    except Exception as e:
        print(f"Error sending email: {e}")


if __name__ == '__main__':
    send_email("<youremail>@gmail.com", "Hello! This is a test email sent via the Gmail API.")
