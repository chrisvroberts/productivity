import re

# This is a bash command that will be run. The first item
# is the menu python script I made. This should be adjusted to
# match the location of that script.
#
# The other elements are the menu options that you want.
# If you want to pick something other than the first unique
# character as the shortcut, add a preceeding underscore like I
# have in the first item. If you want the actual label to have
# an underscore (not to indicate a shortcut character) then put
# two, one after the other.
#
# Note also that you can use a digit as the shortcut character.
# These may be quicker to hit than letters on the keyboard
# depending on your laptop keyboard layout. 
command = [
  "/home/cvroberts/Documents/accessible-menu/accessible-menu",
  "display _window info",
  "show selection",
  "US to UK",
  "speech-to-text insert",
  "selected text to speech",
]

# This runs the script and 'selection' will be set to the
# option that you chose from the menu. This will match one
# of the strings in the 'command' list above. Note that any
# underscores you added above for the shortcuts will have been
# removed by the script (not sure if that is helpful or not).
# If nothing was selected then selection will be empty.
selection = system.exec_command('"' + '" "'.join(command) + '"')

# Now for each option you can choose what you want it to do.
# Here are some examples:
if selection == "display window info":
  # This command runs another AutoKey script by name. This
  # is quite handy. You may decide you want all of the options
  # to delegate to other AutoKey scripts. In that way, any that
  # you find you use a lot can easily be assigned their own
  # Hotkey rather than (or as well as) accessing them though this
  # menu script.
  engine.run_script("Display window info")
elif selection == "show selection":
  # This grabs any highlighted text and does something
  # with it. In this case it shows it you in a window but
  # we might hook this up to the sheech-to-text tool, for
  # example.
  txt = clipboard.get_selection()
  dialog.info_dialog("Current selection", txt)
elif selection == "US to UK":
  # Here is an example of some selected-text modification.
  # It uses simple repeated-substitution, working through
  # a list of hand-added substitutions. I think you mentioned
  # having such a list so that could be used here. If you list
  # is in a structured format we can update this code to read
  # those in from a file if that's useful. There may even be
  # python modules, or APIs, that will do this locale
  # conversion for you.
  #
  # Note here that you can use a Regular Expression as well
  # as just a string pattern. These are more powerful and
  # can be written to match the input text more precisely.
  # This may be useful if you find you patterns regularly
  # mis-correct certain words etc. I can help you write these
  # if that is useful.
  txt = clipboard.get_selection()
  substitutions = [
    ('ize', 'ise', False),
    ('yze', 'yse', False),
    ('([^l])l(ed|ing|er)\\b', '\\1ll\\2', True),
    ('ense\\b', 'ence', True),
  ]
  for pattern, sub, is_regex in substitutions:
    if is_regex:
      txt = re.sub(pattern, sub, txt)
    else:
      txt = txt.replace(pattern, sub)

  # This seems like a hacky way to replace the text... I suspect
  # there is a better way.
  keyboard.send_keys(txt)
elif selection == "speech-to-text insert":
  engine.run_script("InsertSpeech")
elif selection == "selected text to speech":
  engine.run_script("SpeakSelection")
elif selection == "":
  # Do nothing - you get here if you didn't pick anything from
  # the menu.
  pass
else:
  # Options that you have not hooked up to any code will arrive
  # here. There probably won't be any of these so this could be
  # replaced with 'pass' or removed. But this may be handy while
  # you are building up your options.
  dialog.info_dialog("Unhandled option", selection)
