from gtts import gTTS
import os


def speak_the_sentence(sentence):
    tts = gTTS(text=sentence, lang='en')
    tts.save("sentence.mp3")
    os.system("mpg321 sentence.mp3")

