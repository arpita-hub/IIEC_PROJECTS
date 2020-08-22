import os
import pyttsx3

pyttsx3.speak("Hi,What's your name")
name = input("Hi, What's your name? \n")
print("Hi, " + name + " I am Eve, I am here to help you" "\U0001f600")
pyttsx3.speak("Hi, " + name + " I am Eve, I am here to help you")
print("I can open the program that you want \n")
pyttsx3.speak("I can open the program that you want")
print("If you want to exit,Please type exit \n")
pyttsx3.speak("If you want to exit,Please type exit")
pyttsx3.speak("Please enter the name of the program")

while True:
    programName = input("Please enter the name of the program \n")

    if (("gedit" in programName) or ("editor" in programName) or ("notepad" in programName)):
        if ("gedit" in programName):
            os.system("gedit")
        elif ("editor" in programName):
            pyttsx3.speak(
                "Which editor you want I have two options 1. gedit \n 2. vim \n")
            editor = input(
                "Which editor you want I have two options 1. gedit \n 2. vim \n")
            if ("gedit" in editor):
                os.system("gedit")

            elif ("vim" in editor):
                os.system("vim")

            else:
                print("Sorry I have no other editor available ")
                pyttsx3.speak("Sorry I have no other editor available")

    elif (("google" in programName) or ("browser" in programName) or ("firefox" in programName)):
        if ("google" in programName) or ("chrome" in programName):
            os.system("chromium")
        elif ("firefox" in programName):
            os.system("firefox")
        elif ("browser" in programName):
            pyttsx3.speak(
                "Which browser you want I have two options 1. Google Chrome \n 2. Firefox \n")
            browser = input(
                "Which browser you want I have two options 1. google chrome \n 2. firefox \n")

            if ("google chrome" in browser) or ("chrome" in browser) or ("google" in browser):
                os.system("chromium")

            elif ("firefox" in browser):
                os.system("firefox")

            else:
                print("Sorry I have no other browser available ")
                pyttsx3.speak(
                    "Sorry I have no other browser available")

    elif ("terminal" in programName):
        os.system("gnome-terminal")

    elif ("exit" in programName) or ("quit" in programName) or ("stop" in programName):
        print("Thanks for Visiting")
        pyttsx3.speak("Thanks for Visiting")
        break

    else:
        print("Not Supported")
