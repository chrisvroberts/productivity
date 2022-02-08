#!/usr/bin/env python3

# I had success with this. I had to install the following:
#
# pip install googletrans==4.0.0-rc1
#
# And then run like this:
#
# ./trans-test.py how are you today

from googletrans import Translator
import sys

text = ' '.join(sys.argv[1:])
translator = Translator()
translation = translator.translate(text, src='en', dest='de')
print(translation.text)
