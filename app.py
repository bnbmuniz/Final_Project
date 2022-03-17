from distutils.command.config import LANG_EXT
from attr import dataclass
from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import timedelta
import sqlalchemy
import speech_recognition as sr
from PIL import Image
import os
import transformers
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
import time
import argparse
import multiprocessing
from playsound import playsound


from sound_text_correct import sound_text_Eng

#from translate import *
from summarization import *
#from clean_sum_text import *
#from text_sound import text_audio
from clip_fft_helper import main

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
        mytxt = sound_text_Eng()
        global text
        text = sum_text(mytxt)
        text = text.strip()
        #print(text)

        return render_template('create.html', value = text)
    return render_template('create.html')

@app.route("/image")
def image():
    print("DREAM RECEIVED")
    music_name= "static/yoga_wait.mp3"
    print(text)
    p1 = multiprocessing.Process(target= main, args=(text, [300, 300], 10, 10))
    p2 = multiprocessing.Process(target= playsound, args=(music_name,))

    p1.start()
    p2.start()

    p1.join()
    if p1.is_alive() == False:
        p2.terminate()
    return render_template("create.html")
    
@app.route("/final")
def final():
    x = text.strip().lower().split( )
    name = x[0] + "_" + x[1] + "_" + x[2]
    for files in os.listdir('static/'):
        files = files.split('.')[0]
        if files.startswith(name):
            pic_name = files + '.jpg'
            print('picname'+ pic_name)
            if pic_name != None:
                return render_template("create.html", image= pic_name)
                



if __name__== "__main__":
    app.run(debug=True)