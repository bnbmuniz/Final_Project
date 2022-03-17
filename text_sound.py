import pyttsx3
engine=pyttsx3.init()

dream_text="hi guys"
voices=engine.getProperty("voices")
#print(voices)

#RESOLVER O PQ DE FICAR REPETINDO

def text_audio(dream_text):
    """Text to Speech"""
    voices=engine.getProperty("voices")
    engine.setProperty("voice", "com.apple.speech.synthesis.voice.Victoria")
    engine.say(dream_text)
    engine.runAndWait()
    




#text_audio("Hi")