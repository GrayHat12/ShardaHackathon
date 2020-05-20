from gtts import gTTS
import playsound
import os
import speech_recognition as sr
import pyfiglet
import random
import sel_data

filename = "file.mp3"

BOT_READY = False
BOT_REPLY = ""

query = [["hi", "hello", "hey"], ["how are you", ""], []]
response = [["hello", "hi", "hey"], ["i am fine", "i am good", ""], []]


class TTS():
    def play(self, text):
        tts = gTTS(text)
        print(text)
        tts.save(filename)
        playsound.playsound(filename)
        os.remove(filename)

    def listen(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        try:
            bot = BOT()
            user_text = r.recognize_google(audio)
            print(user_text)
            bot.get_reply(user_text)
        except LookupError:
            print("Could not understand audio")


class UI():
    def __init__(self):
        fonts = ["banner3-D", "basic", "block", "bulbhead", "coinstak", "colossal", "computer", "cosmic", "lean",
                 "letters", "o8", "roman", "rowancap", "rozzo", "speed", "univers"]
        FONT = int(random.random() * len(fonts))
        fig = pyfiglet.figlet_format("GrayBot", font=fonts[FONT], width=200)
        print(fig)
        print("Tour Guide\n")

    def start(self):
        tts = TTS()
        i = 0
        while (True):
            if i % 2 == 0:
                print('''\nUser>  ''', end="")
                tts.listen()
                i += 1

            else:
                print('''\nGrayBot>  ''', end="")
                while (not BOT_READY):
                    pass
                tts.play(BOT_REPLY)
                BOT_READY = False
                i += 1


class BOT():
    def get_reply(self, text=""):
        global BOT_READY
        global BOT_REPLY
        sel_data.entity(text)
        tut = sel_data.entity(text)
        BOT_READY = True
        return tut


if __name__ == '__main__':
    ui = UI()
    ui.start()
