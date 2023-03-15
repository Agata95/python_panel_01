from flask import Flask, render_template, request
from funkcje.baza_danych import generate_token, create_user_record

app = Flask("01_app")


@app.route("/")
def mainpage():
    return render_template('text_page.html')


@app.route("/podaj_dane/")
def get_data_page():
    return render_template('podaj_dane.html')


@app.route("/submit_data", methods=['POST'])
def get_data_from_post():
    dane = request.form.to_dict()
    token = generate_token(20)
    # zczytywanie wprowadzonych danych przez użytkownika
    # zmienne z html: name=
    email = request.form['inputEmail']
    body = request.form['inputBody']

    return render_template("user_w_bazie.html",
                           user_email=email,
                           generated_token=token)


app.run()
