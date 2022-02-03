#!/usr/bin/env python3

# I had success with this. I had to install the following:
#
# pip install gTTS
# pip install playsound
#
# And then run like this:
#
# ./tts-test.py hello how are you?

from gtts import gTTS
import os
import playsound
import sys

def speak(text):
    tts = gTTS(text=text, lang='en')

    filename = "abc.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

text = ' '.join(sys.argv[1:])
speak(text)
    
