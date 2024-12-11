# Add to this file for the sample app lab
from flask import Flask
from flask import request
from flask import render_template, redirect, url_for
from datetime import date

sample = Flask(__name__)

users = {
    "admin": "password123",  # Gebruikersnaam: admin, Wachtwoord: password123
}

@sample.route("/", methods=["GET", "POST"])
def main():
    vandaag = date.today()
    return render_template("index.html",datum=vandaag)
def login():
    if request.method == "POST":
        # Haal gebruikersnaam en wachtwoord op van het formulier
        username = request.form["username"]
        password = request.form["password"]

        # Controleer of de gebruikersnaam en wachtwoord overeenkomen
        if username in users and users[username] == password:
            return redirect(url_for("welcome"))
        else:
            return "Ongeldige inloggegevens, probeer het opnieuw."

    return render_template("index.html")

@sample.route("/welcome")
def welcome():
    return "Welkom, je bent succesvol ingelogd!"

if __name__ == "__main__":
    sample.run(host="0.0.0.0", port=5050)
