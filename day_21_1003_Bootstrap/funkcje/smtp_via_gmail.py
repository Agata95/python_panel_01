# https://support.google.com/accounts/answer/185833?visit_id=638130393974242422-268600675&p=InvalidSecondFactor&rd=1

import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


def send_email_imap(username, password, recipient, subject, body, attachment=None):
    # Create a new SMTP object and connect to the Gmail SMTP server
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    try:
        smtp_conn = smtplib.SMTP(smtp_server, smtp_port)
        smtp_conn.ehlo()
        smtp_conn.starttls()
        smtp_conn.ehlo()
        smtp_conn.login(username, password)

        # Create a new MIME message object and fill in the details
        msg = MIMEMultipart()
        msg['From'] = username
        msg['To'] = recipient
        msg['Subject'] = subject
        msg.attach(MIMEText(body))

        # Attach a file if specified
        if attachment is not None:
            with open(attachment, 'rb') as f:
                part = MIMEApplication(f.read(), Name=attachment)
                part['Content-Disposition'] = f'attachment; filename="{attachment}"'
                msg.attach(part)

        # Convert the message to a string and send it via SMTP
        smtp_conn.sendmail(username, recipient, msg.as_string())

        # Disconnect from the SMTP server
        smtp_conn.quit()
        return True
    except smtplib.SMTPAuthenticationError:
        print("AUTH ERROR")
        return False


# if __name__ == "__main__":
#     send_email_imap("adam.jurkiewicz.pythonista@gmail.com", "day_18_0103/gmail_code.txt", "adam@jurkiewicz.tech", "testowy", "To jest testowy mail.")
