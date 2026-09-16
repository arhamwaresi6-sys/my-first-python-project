import speech_recognition as sr
import webbrowser
import pyttsx3

r = sr.Recognizer()
engine = pyttsx3.init()


def processor(c):
    if "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")

    elif "open google" in c.lower():
        webbrowser.open("https://www.google.com")

    elif "hello" in c.lower():
        speak("Hello! How can I help you?")

    else:
        speak("I don't understand that command.")


def speak(text):
    engine.say(text)
    engine.runAndWait()


if __name__ == "__main__":

    speak("Initializing Jarvis...")

    # Listen for "Jarvis"
    while True:
        try:
            with sr.Microphone(device_index=0) as source:
                print("Listening...")

                audio = r.listen(
                    source,
                    timeout=2,
                    phrase_time_limit=1
                )

            print("Recognizing...")
            command = r.recognize_google(audio)
            print("You said:", command)

            # Wake word detected
            if command.lower() == "jarvis":

                speak("Yes?")

                # Listen for the actual command
                with sr.Microphone(device_index=0) as source:
                    print("Listening for command...")

                    audio = r.listen(
                        source,
                        timeout=5,
                        phrase_time_limit=5
                    )

                print("Recognizing command...")
                command = r.recognize_google(audio)

                print("Command:", command)

                # Process the command
                processor(command)

        except sr.WaitTimeoutError:
            print("No speech detected.")

        except sr.UnknownValueError:
            print("Could not understand the audio.")

        except sr.RequestError as e:
            print("Google Speech Recognition error:", e)

        except Exception as e:
            print("Error:", e)

