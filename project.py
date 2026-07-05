import speech_recognition as sr
import pyttsx3
import webbrowser
import pywhatkit

# Initialize voice engine
engine = pyttsx3.init()

# Speak function
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Take command function
def take_command():

    listener = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")

        listener.adjust_for_ambient_noise(source, duration=1)

        try:

            # Wait max 5 sec for user to start speaking
            audio = listener.listen(
                source,
                timeout=10,
                phrase_time_limit=10
            )

            command = listener.recognize_google(audio)

            command = command.lower()

            print("You said:", command)

            return command

        # If user says nothing
        except sr.WaitTimeoutError:

            print("Timeout occurred")

            return "timeout"

        except Exception as e:

            print("Sorry, I can not hear you:", e)

            return "stop"

# Start assistant
speak("Dracula is ready")

while True:

    command = take_command()

    # Break automatically on timeout
    if command == "timeout":

        speak("No voice detected. Closing assistant")

        break

    # Open YouTube
    elif "open youtube" in command:

        speak("Opening YouTube")

        webbrowser.open("https://www.youtube.com")

    # Open Google
    elif "open google" in command:

        speak("Opening Google")

        webbrowser.open("https://www.google.com")

    # Play song
    elif "play" in command:

        song = command.replace("play", "")

        speak("Playing " + song)

        pywhatkit.playonyt(song)

    # Stop manually
    elif "stop" in command or "exit" in command:

        speak("Goodbye")

        break