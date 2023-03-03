import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


def mail_report(mail_to: str, mail_from: str, data: str, file: str = None) -> bool:
    ip = "jurkiewicz.tech"
    port = 465  # For SSL
    login = "python-course@jurkiewicz.tech"
    password = "zle_haslo"
    ####

    if file:
        attachment = open(file, 'rb')
        msg = MIMEMultipart()
        msg.attach(MIMEText(data))
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment', filename=file)
        msg.attach(part)
    else:
        text_type = 'plain'  # or 'html'
        msg = MIMEText(data, text_type, 'utf-8')

    msg['Subject'] = "Temat wiadomości"
    msg['From'] = mail_from
    #
    msg['To'] = mail_to

    try:
        # Create a secure SSL context
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(ip, port, context=context) as server:
            server.login(login, password)
            server.sendmail(msg['From'], msg['To'], msg.as_string())
            server.quit()
        return (True, "Test mail SUCCESS")
    except Exception as e:
        return (False, e)


if __name__ == "__main__":
    print(f"to jest tylko uruchomienie testowe: {__name__}")
    mail_ok, report = mail_report("adam.jurkiewicz.pythonista@gmail.com", "python-course@jurkiewicz.tech", "Treść INNA")
    if mail_ok:
        print(report)
    else:
        print(f"Test mail failed - {report}")

    print(f"to jest tylko uruchomienie testowe: {__name__} + załącznik")
    mail_ok, report = mail_report("adam.jurkiewicz.pythonista@gmail.com", "python-course@jurkiewicz.tech", "Treść INNA", file="baza_users.db")
    if mail_ok:
        print(report)
    else:
        print(f"Test mail failed - {report}")
else:
    print(f"Importujemy moduł: {__name__}")