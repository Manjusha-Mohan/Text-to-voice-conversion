from gtts import gTTS
import os

my_text = "Welcome to Python Programming language"
language = 'en'

output = gTTS(text=my_text,lang=language,slow=False)
output.save("output.mp3")
os.system("start output.mp3")