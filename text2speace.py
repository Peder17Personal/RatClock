import pyttsx3

def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    user_input = input("Enter text to speak: ")
    speak_text(user_input)