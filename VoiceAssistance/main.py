import speech_recognition as sr
import pyttsx3
import datetime
import os

voice_inbuilt = pyttsx3.init()


def greet():
    now = datetime.datetime.now()
    current_time = int(now.strftime("%H"))
    # print(current_time)
    if 4 < current_time < 12:
        speech = "Hi, Good Morning, I am Lenovo G 50 45, Welcome , How may I help you?"
    elif 12 < current_time < 16:
        speech = "Hi, Good Afternoon, I am Lenovo G 50 45, Welcome , How may I help you?"
    elif 16 < current_time < 23:
        speech = "Hi, Good Evening, I am Lenovo G 50 45, Welcome , How may I help you?"
    else:
        speech = "Hi, It is time for bed already, what are you doing, still i am here to help you, whatsup?"

    voice_inbuilt.say(speech)
    voice_inbuilt.runAndWait()


def speak(voice):
    try:
        if "vs code" in voice:
            speech = "Wait...Opening VsCode"
            voice_inbuilt.say(speech)
            voice_inbuilt.runAndWait()
            path = ("C:\\Users\\Sonu\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
            os.startfile(path)
        elif "who are you" in voice:
            voice_inbuilt.say("I am lenovo g 50 45, I was bought by Ritendu on September 2016, I am here to help you and make your life easier, THANK YOU")
            voice_inbuilt.runAndWait()
        elif "sublime" in voice:
            speech = "Wait...Opening sublime text"
            voice_inbuilt.say(speech)
            voice_inbuilt.runAndWait()
            path = ("C:\\Program Files\\Sublime Text 3\\sublime_text.exe")
            os.startfile(path)
        elif "java" in voice:
            speech = "Wait...Opening intellij"
            voice_inbuilt.say(speech)
            voice_inbuilt.runAndWait()
            path = ("C:\\Program Files\\JetBrains\\IntelliJ IDEA Community Edition 2020.1.1\\bin\\idea64.exe")
            os.startfile(path)
        elif "pycharm" in voice:
            speech = "Wait...Opening pycharm"
            voice_inbuilt.say(speech)
            voice_inbuilt.runAndWait()
            path = ("C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.1\\bin\\pycharm64.exe")
            os.startfile(path)
        elif "photoshop" in voice:
            speech = "Wait...Opening photoshop"
            voice_inbuilt.say(speech)
            voice_inbuilt.runAndWait()
            path = ("C:\\Program Files\\Adobe\\Adobe Photoshop CC 2019\\Photoshop.exe")
            os.startfile(path)
        elif "xd" in voice:
            speech = "Wait...Opening adobe xd"
            voice_inbuilt.say(speech)
            voice_inbuilt.runAndWait()
            path = ("C:\\Users\\Sonu\\Desktop\\Adobe XD")
            os.startfile(path)
        elif "github" in voice:
            speech = "Wait...Opening source tree"
            voice_inbuilt.say(speech)
            voice_inbuilt.runAndWait()
            path = ("C:\\Users\\Sonu\\Desktop\\SourceTreeSetup-3.3.8.exe")
            os.startfile(path)
        elif "android studio" in voice:
            speech = "Wait...Opening android studio"
            voice_inbuilt.say(speech)
            voice_inbuilt.runAndWait()
            path = ("C:\\Program Files\\Android\\Android Studio\\bin\\studio64.exe")
            os.startfile(path)
        elif "chrome" in voice:
            speech = "Wait...Opening chrome"
            voice_inbuilt.say(speech)
            voice_inbuilt.runAndWait()
            path = ("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
            os.startfile(path)
        elif "GIT bash" in voice:
            speech = "Wait...Opening gitbash"
            voice_inbuilt.say(speech)
            voice_inbuilt.runAndWait()
            path = ("C:\\Program Files\\Git\\git-bash.exe --cd-to-home")
            os.startfile(path)
        elif "bye" in voice:
            exit()
    except Exception as e:
        speech = "Sorry you said nothing "
        voice_inbuilt.say(speech)
        voice_inbuilt.runAndWait()


if __name__ == "__main__":
    sample_rate = 48000
    chunk_size = 2048
    r = sr.Recognizer()
    greet()

    while True:
        with sr.Microphone(0, sample_rate, chunk_size) as source:
            r.adjust_for_ambient_noise(source)
            print("Listening...")
            voice_inbuilt.say("to initiate me please say start or say stop to sleep me")
            voice_inbuilt.runAndWait()

            try:
                audio = r.listen(source)
                text = r.recognize_google(audio)
                if "start" in text.lower():
                    voice_inbuilt.say("I am Listening...")
                    voice_inbuilt.runAndWait()
                    start_audio = r.listen(source)
                    instruction = r.recognize_google(start_audio)
                    print(instruction)
                    speak(instruction.lower())

                elif "stop" in text.lower():
                    voice_inbuilt.say("Please say Start when you want to initiate me again...")
                    voice_inbuilt.runAndWait()
                    while True:
                        try:
                            stop_audio = r.listen(source)
                            instruction = r.recognize_google(stop_audio)
                        except Exception as e:
                            instruction = " "
                        if "start" in instruction.lower():
                            break
                        elif "bye" in instruction.lower():
                            voice_inbuilt.say("Thank you have a nice day, stay safe")
                            voice_inbuilt.runAndWait()
                            exit()
                        else:
                            continue

                elif "bye" in text.lower():
                    voice_inbuilt.say("Thank you have a nice day, stay safe")
                    voice_inbuilt.runAndWait()
                    exit()

            except Exception as e:
                error = "please say something..."
                voice_inbuilt.say(error)
                voice_inbuilt.runAndWait()

