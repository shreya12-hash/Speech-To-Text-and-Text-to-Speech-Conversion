# Speech-To-Text-and-Text-to-Speech-Conversion
### An open source contribution by Shreya ###
### Sppech to Text ###

In this part I have converted an audio file, that consists of some speech, to a text file in Python using SpeechRecognition library. As a result, we do not need to build any machine learning model from scratch, this library provides us with convenient wrappers for various well known public speech recognition APIs (such as Google Cloud Speech API, IBM Speech To Text, etc.).

To proceed further you need to install the SpeechRecognition library (the latest version when doing the project the current version available is 3.8.1). Now to install you can use pip or conda depending upon which development platform you are utilising. You can install by following command

`pip install SpeechRecognition`

or

`conda install SpeechRecognition`

Now import the module speech_recognition

`import speech_recognition as sr`

`r = sr.Recognizer()`

set the path to the sound file. PLease take a note that your Audio file should be in .wav format

`sound_file = 'C:/Users/Biswas/Downloads/female.wav'`

Read the audio file and store in a new object

`file_audio = sr.AudioFile(sound_file)`

Now we set the newly read audio file as the source to recognise as speech object

`with file_audio as source:`

     `audio_text = r.record(source)`

Then save the recognised text in an object called 'text' for further processing

`text= r.recognize_google(audio_text)`
 
 `print(text)`
 
 Now create a text file for further processing

`f = open("extracted1.txt", "w")`

`f.write(text)`

`f.close()`
