import pyttsx3
import wikipedia
voice=pyttsx3.init()
In=input("Searching wikipedia:")
result=wikipedia.summary(In,sentences=10)
print(result)
voice.say(result)
voice.runAndWait()