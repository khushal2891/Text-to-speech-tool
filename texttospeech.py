from gtts import gTTS  # Importing gTTS module for text-to-speech conversion
import os

# If you want to read from a file, you can change this
with open('sample.txt', 'r') as abc:  # Open the file in read mode
    text = abc.read()  # Read the text from the file

language = 'en'  # Specify the language, 'en' for English

# Create gTTS object with the specified text and language
obj = gTTS(text=text, lang=language, slow=False)

# Save the generated audio file
obj.save("sample.mp3")

# Play the audio file
os.system("sample.mp3")