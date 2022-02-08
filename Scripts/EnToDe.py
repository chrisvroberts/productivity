# Enter script code
from googletrans import Translator

text = clipboard.get_selection()
translator = Translator()
translation = translator.translate(text, src='en', dest='de')
keyboard.send_keys(translation.text)
