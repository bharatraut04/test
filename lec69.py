import pyttsx3

# Initialize the engine
engine = pyttsx3.init()

# Optional: Change voice (0 for male, 1 for female typically)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) 

# Speak text
engine.say("Hello, this is a native Windows voice." \
"i am james bond  ")
engine.runAndWait()
