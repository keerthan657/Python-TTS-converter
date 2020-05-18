# Python-TTS-converter
A python script for converting text to speech with a friendly UI

This python script uses 'pyttsx3' module for text-2-speech conversion, and the PyQt5 package for implementing a friendly UI for this program.

Let's see the result first :
![python TTS application](https://github.com/keerthan657/My-Images/blob/master/python%20tts%20application.PNG)

The delay field - for delaying the speech initially (in sec)(Note: Not reducing the speed of speech)
The text field - what you want to be converted to speech
The speak button - click it to speak-out

This basically covers all of this application

Going on to How it works :
The text is input to the appliation via PyQt5 and it's widgets and then, pyttsx3's speech engine converts the given text to speech

If the delay time is not from 0 to 10 sec, the program shows up an error dialog as shown :
![Warning Message](https://github.com/keerthan657/My-Images/blob/master/python%20tts%20application%20-%20warning.PNG)
