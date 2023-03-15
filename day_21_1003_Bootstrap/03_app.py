from flask import Flask, render_template, request
from funkcje.baza_danych import generate_token, create_user_record
from random import randint

app = Flask("01_app")


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
    if create_user_record('users.db', email, token):
        created = "Wszystko super, dane w bazie"

    return render_template("user_w_bazie.html",
                           user_email=email,
                           generated_token=token,
                           picture=obrazek,
                           desc=created)


app.run()
