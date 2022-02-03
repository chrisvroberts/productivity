#!/usr/bin/env python3

# I had success with this. I had to install the following:
#
# sudo apt-get install portaudio19-dev
# pip install pyaudio
# pip install SpeechRecognition
#
# And then run like this:
#
# ./sr-test.py

import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as src:
  audio = r.listen(src)
  voice_data = r.recognize_google(audio)
  print(voice_data)
