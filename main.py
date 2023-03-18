import pyttsx3

def speak(text):
  engine = pyttsx3.init()
  engine.say(text)
  engine.runAndWait()

speak("Hello, Bitches! You hoes should have never given me the opportunity to build programs. You scared of AI taking over when you need to be scared of me taking your BITCH!")