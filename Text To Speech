#Import Google Text to Speech
from gtts import gTTS 

#Import Audio method from IPython's Display Class
from IPython.display import Audio 

#import the extracted text in read mode
f = open("extracted1.txt", "r")
text=f.read()

#Provide the string to convert to speech
tts = gTTS(text ) 

#save the string converted to speech as a .wav file
tts.save('output.wav') 
sound_file ='output.wav'
Audio(sound_file, autoplay=True) 
