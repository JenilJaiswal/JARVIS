import pyttsx3
import speech_recognition as sr
import eel

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices') 
    print(voices)
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 190)
    engine.say(text)
    engine.runAndWait()
  
@eel.expose    
def takecommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('listening....')
        eel.DisplayMessage('listening....')
        r.pause_threshold = 1 # I want to chnage the threshold for the pause
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, 10, 6)

    try:
        print('recognizing')
        eel.DisplayMessage('recognizing....')
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
        eel.DisplayMessage(query)
        speak(query)
        eel.ShowHood()
    except Exception as e:
        return ""
    
    return query.lower()


# text = takecommand()

# speak(text)
# speak("Hello, I am JARVIS How can I assist you today?")