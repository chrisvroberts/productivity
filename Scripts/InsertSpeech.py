# Enter script code

import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as src:
  audio = r.listen(src)
  voice_data = r.recognize_google(audio)
  keyboard.send_keys(voice_data)
