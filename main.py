import speech_recognition as sr
import webbrowser
import pyttsx3

r = sr.Recognizer()
engine = pyttsx3.init()  # object creation
def processor(c):
    pass
def speak(text):
    engine.say(text)
    engine.runAndWait() # it makes the program to wait till it says


if __name__ == "__main__":  # Added missing colon here and double underscores
    speak("Initializing jarivis...")
    #listen for the jarivis
    while True:
        try:
            with sr.Microphone(device_index=0) as source:
                print("listenning...")
                audio = r.listen(source,timeout=2,phrase_time_limit=1)
            print("recognizing....")
            command = r.recognize_google(audio)
            print(command)
            if command == "jarvis":
                pass
        except Exception as e:
            print("Error! {0}".format(e))
#adding on master commit b
# i am adding a comment here A
# i am adding a comment here
a = 1
print(1)
b = "arham"
print(b)
a = 2
print(a)
b = 12
print(b)
