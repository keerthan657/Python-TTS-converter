# Python-TTS-converter
A python script for converting text to speech with a friendly UI

This python script uses 'pyttsx3' library for offline text-2-speech conversion, and the PyQt5 package for implementing a friendly UI for this script.

The delay field - For delaying the speech initially (in sec)(Note: Not reducing the speed of speech)
The text field - What you want the engine to speak-out
The speak button - Click it to speak-out
The volume slider - Control volume of speech
The rate slider - Control voice rate from this slider
The male and female voice checkboxes : Select the voice of your speech output here (Automatically defaults to male voice if none or both are selected)

This basically covers all of this application

Going on to How it works :
The text is input to the appliation via PyQt5 and it's widgets and then, pyttsx3's speech engine converts the given text to speech
I also added error windows for if the delay time and text field were empty

Edit 1:
Added features for volume, rate of voice and tone of voice
Added default values for some parameters
#This is my first repo, feel free to make changes or correct my code(if any)
