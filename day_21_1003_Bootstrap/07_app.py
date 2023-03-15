from flask import Flask, render_template, request
from funkcje.baza_danych import generate_token, create_user_record, check_mail
from random import randint
from funkcje.smtp_via_gmail import send_email_imap
from faker import Faker

app = Flask("01_app")
DATABASE = "users.db"


@app.route("/")
def mainpage():
    return render_template('text_page.html')


@app.route("/podaj_dane/")
def get_data_page():
    return render_template('podaj_dane.html')


@app.route("/submit_data", methods=['POST'])
def get_data_from_post():
    obrazek = f"https://thispersondoesnotexist.xyz/img/{randint(3317, 4315)}.jpg"
    dane = request.form.to_dict()
    token = generate_token(20)
    # zczytywanie wprowadzonych danych przez użytkownika
    # zmienne z html: name=
    email = request.form['inputEmail']
    body = request.form['inputBody']

    created = "Nie udał się zapis do bazy"
    if create_user_record(DATABASE, email, token):
        created = "Wszystko super, dane w bazie"

        email_from = 'XXX'
        email_to = email
        email_subject = "Logowanie z hasłem"
        email_login_passwd = 'XXX'
        email_body = f"""
        Aby się autoryzować, kliknij:

        127.0.0.1:5000/auth/{email_to}/{token}

        Link autoryzacyjny dla {token}
        <hr>
        {body}
        <hr>
        <h3> Zespół wsparcia </h3>
        """
        if send_email_imap(email_from, email_login_passwd, email_to, email_subject, email_body):
            created += ' Email wysłany.'
        else:
            created += f" Ale wysyłka email się nie powiodła."

    return render_template("user_w_bazie.html",
                           user_email=email,
                           generated_token=token,
                           picture=obrazek,
                           desc=created)


@app.route("/auth/<from_email>/<user_token>")
def check_user(from_email, user_token):
    authorized = check_mail(DATABASE, from_email, user_token)
    if authorized:
        obrazek = f"https://thispersondoesnotexist.xyz/img/{randint(3317, 4315)}.jpg"
        fake_person = Faker("pl_PL")
        return render_template("authorized.html",
                               user_email=from_email,
                               generated_token=user_token,
                               name=fake_person.name(),
                               address=fake_person.street_name(),
                               city=fake_person.city(),
                               picture=obrazek)
    else:
        return "<h3> Not authorized </h3>"


app.run()
