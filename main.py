import re
import transformers
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
import speech_recognition as sr 
import pyttsx3


from sound_text_correct import *
from translate import *
from summarization import *
from clean_sum_text import *
from text_sound import *

engine=pyttsx3.init()
voices=engine.getProperty("voices")
# get audio from the microphone                                                                       
r = sr.Recognizer() 


def main_function(choice_1):
    sound_text(choice_1)
    dream="dream.txt"
    if (choice_1=="Portuguese-PT")|(choice_1=="Portuguese-BR"):
        translate(dream)
        sum_text(dream)
        print(dream)
    else:
        sum_text(dream)
        #text_audio("English","Please check if the following is your dream: ")
        print(dream)
        #if dreamiscorrect=="yes":
        #    clean_dream (dream_summarized)
        #else:
            #text_audio("English","Please write down your dream: ")
            #buttom to write dream down
        #put function that turns text to image here

print(main_function("Portuguese-BR"))
