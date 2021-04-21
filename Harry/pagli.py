import speech_recognition as sr
import pyttsx3

engine=pyttsx3.init() # Initialiser for text to speech
listener=sr.Recognizer() # Recogniser object 

def speak():
    engine.say("Main pagli hoon...")
    engine.setProperty('rate',125)
    engine.runAndWait()

speak()
v,r=engine.getProperty('volume'),engine.getProperty('rate')
print(v)
engine.setProperty('rate',125)
speak()
rate=engine.getProperty('rate')
print(rate)

# try:
#     with sr.Microphone() as src:
#         print("Listening...")
#         voice=listener.listen(src)
#         command=listener.recognize_google(voice)
#         print(command)
# except:
#     print('Try Again...')