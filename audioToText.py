import speech_recognition as sr

r = sr.Recognizer()

def getAudioToText(filename,input_lang):
    with sr.AudioFile(filename) as source:
        audio = r.record(source)

    try:
        text = r.recognize_google(audio,language=input_lang)
        print("You said: " + text)
        return text
    except:
        print("Error")