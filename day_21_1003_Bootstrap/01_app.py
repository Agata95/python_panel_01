from flask import Flask, render_template

app = Flask("01_app")


@app.route("/")
def mainpage():
    return render_template('text_page.html')


@app.route("/podaj_dane/")
def get_data_page():
    return render_template('podaj_dane.html')


@app.route("/submit_data", methods=['POST'])
def get_data_from_post():
    return "NIC"


app.run()
