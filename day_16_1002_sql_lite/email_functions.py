import smtplib, ssl
from email.mime.text import MIMEText


def mail_report(mail_to: str, mail_from: str, data: str) -> bool:
    ip = "jurkiewicz.tech"
    port = 465  # For SSL
    login = "eh-2023@jurkiewicz.tech"
    password = "dVVz]),Z^[Uk"
    # password = "zle_haslo"
    ####

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
        return (True, "Test mail SUCCESS")
    except Exception as e:
        return (False, e)


if __name__ == "__main__":
    print(f"to jest tylko uruchomienie testowe: {__name__}")
    mail_ok, report = mail_report("adam.jurkiewicz.pythonista@gmail.com", "eh-2023@jurkiewicz.tech", "Treść INNA")
    if mail_ok:
        print(report)
    else:
        print(f"Test mail failed - {report}")
else:
    print(f"Importujemy moduł: {__name__}")