from gtts import gTTS 
import os  
mytext = 'Welcome to home dear!eat some food'
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False) 
myobj.save("welcome.mp3") 
os.system("mpg321 welcome.mp3") 