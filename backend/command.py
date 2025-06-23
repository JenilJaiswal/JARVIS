import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices') 
    print(voices)
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 190)
    engine.say(text)
    engine.runAndWait()
    
speak("Hello, I am JARVIS How can I assist you today?")