### An open source contribution by Shreya ###
# Speech-To-Text-and-Text-to-Speech-Conversion

Speech recognition is the ability of a machine or program to identify words and phrases in spoken language and convert them to a human readable text format. Rudimentary speech recognition software has a limited vocabulary of words and phrases, and it may only identify those speech which are spoken very clearly

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

### Text To Speech ###

Text-to-speech (TTS) is one kind of technology that is used to read aloud digital text. It can take anything regarding text. It can be combinations of words, this project convert them into audio. Also, all kinds of text files can be read aloud, including Word, pages document, online web pages can be read aloud. TTS can help kids who struggle with reading. Many tools and apps are available to convert text into speech. Python comes with a lot of handy and easily accessible libraries and we’re going to look at how we can deliver text-to-speech with Python in this project. Different API’s are available in Python in order to convert text to speech. One of Such API’s is the Google Text to Speech commonly known as the gTTS API. It is very easy to use the library which converts the text entered, into an audio file which can be saved as a mp3 file. It supports several languages and the speech can be delivered in any one of the two available audio speeds, fast or slow. More details can be found here.

To install the gTTS API, open terminal and write

`pip install gTTS`

Now you are good to start coding your Idea

Import Google Text to Speech

`from gtts import gTTS`

Import Audio method from IPython's Display Class

`from IPython.display import Audio` 

Import the extracted text in read mode

`text=f.read()`

save the string converted to speech as a .wav file

`tts.save('output.wav')` 

Now store the Audio file in a new object

`sound_file ='output.wav'`

Hey, you are good to hear what you have accomplished

`Audio(sound_file, autoplay=True)` 


