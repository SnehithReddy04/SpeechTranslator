
from googletrans import Translator
import speech_recognition as spr
from gtts import gTTS
import os

from lang import *




mic = spr.Microphone(device_index=0)
initiate=spr.Recognizer()
talk=spr.Recognizer()

with mic as source:
    print(" Start speaking by saying hello!")
    print(".................")

    initiate.adjust_for_ambient_noise(source)
    audio = initiate.listen(source)
if 'hello' in initiate.recognize_google(audio):
    initiate=spr.Recognizer()
    t=Translator()
    print("Enter the language u speak")
    sl=input()
    csl=getcode(sl)
    with mic as source:
        print(" speak a sentence you want to convert")
        audio=talk.listen(source)
        sentence=talk.recognize_google(audio, language=csl)
        print("enter the language to be converted")
        tl = input()
        ctl=getcode(tl)
        print(sentence)
        try:
            sentence = talk.recognize_google(audio, language=csl)
            transtextobj=t.translate(sentence, src=csl, dest=ctl)
            transtext=transtextobj.text
            outaud = gTTS(text=transtext, lang=ctl, slow=False)
            outaud.save('sts1.mp3')
            os.system('sts1.mp3')
        except spr.UnknownValueError:
            print("Unable to understand the input")
        except spr.RequestError as e:
            print("Unable to access required translation".format(e))