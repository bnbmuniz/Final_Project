from distutils.command.config import LANG_EXT
from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import timedelta
import sqlalchemy
import speech_recognition as sr
from PIL import Image
import os

app = Flask(__name__)
app.secret_key="hello"
app.permanent_session_lifetime=timedelta(minutes=5)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        print("FORM DATA RECEIVED")

        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)

        if file:
            r = sr.Recognizer()
            audioFile = sr.AudioFile(file)
            with audioFile as source:
                data = r.record(source)
            transcript = r.recognize_google(data, key=None, language="en")
        
            for i in transcript.split( ):
                for files in os.listdir('static/img/'):
                    files = files.split('.')[0]
                    if i == files:
                        name  = i
            names = name +'.jpeg'

        return render_template('create.html', image = names, transcript=transcript)

    elif request.method == 'GET':
        return render_template('create.html')

if __name__== "__main__":
    app.run(debug=True)