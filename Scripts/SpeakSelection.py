# Enter script code

from gtts import gTTS
import playsound
import tempfile

def speak(text):
  tts = gTTS(text=text, lang='en')
  with tempfile.NamedTemporaryFile() as f:
    filename = f.name
    tts.save(filename)
    playsound.playsound(filename)

text = clipboard.get_selection()
speak(text)
