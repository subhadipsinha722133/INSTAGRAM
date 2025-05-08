import pyttsx3


a = int(input("enter number:-"))
b = int(input("enter number:-"))
c = a + b


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voices", voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    print(audio)


if __name__ == "__main__":
    speak(c)
