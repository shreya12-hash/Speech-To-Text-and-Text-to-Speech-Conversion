### An open source contribution by Shreya ###

#import the module speech_recognition
import speech_recognition as sr
r = sr.Recognizer()
sound_file = 'C:/Users/Biswas/Downloads/female.wav'
file_audio = sr.AudioFile(sound_file)

# Now we set the newly read audio file as the source to recognise as speech object
with file_audio as source:
    audio_text = r.record(source)

#Then save the recognised text in an object called 'text' for further processing
text= r.recognize_google(audio_text)

print(text)

# Now create a text file for further processing
f = open("extracted1.txt", "w")
f.write(text)
f.close()
