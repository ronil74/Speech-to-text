import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen for input
def listen():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        return text.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Can you please repeat?")
        return listen()
    except sr.RequestError:
        speak("Sorry, there was an error with the speech recognition service.")
        return listen()

# Main function
def main():
    speak("Hello! How can I assist you?")
    while True:
        command = listen()
        if "yes" in command:
            speak("Great! What can I do for you?")
        elif "no" in command:
            speak("Okay, let me know if you need anything.")
        else:
            speak("I'm sorry, I didn't understand that.")

if __name__ == "__main__":
    main()
