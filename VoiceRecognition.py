from subprocess import call
import speech_recognition as sr
import serial
import RPi.GPIO as GPIO      
import os
import time
import vlc
import datetime
import pyttsx3
from PIL import Image


r = sr.Recognizer()
m = sr.Microphone()
led=16
alarm=26
text = {}
text1 = {}
p = vlc.MediaPlayer("file:///home/pi/Downloads/Rollout.mp3")
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

with m as source: r.adjust_for_ambient_noise(source)
print("Set minimum energy threshold to {}".format(r.energy_threshold))

call(["espeak", "-s140  -ven+18 -z" , "Hello Mandy, I am ready to assist you"])

def listen1():
    with sr.Microphone() as source:
               r.adjust_for_ambient_noise(source)
               print("Awaiting Command");
               audio = r.listen(source)
               print("Affirmative");
    return audio

def voice(audio1):
       try: 
         text1 = r.recognize_google(audio1) 
##         call('espeak '+text, shell=True) 
         print ("You said: " + text1);
         return text1; 
       except sr.UnknownValueError: 
          call(["espeak", "-s140  -ven+18 -z" , "I am sorry Mandy but I could not understand"])
          print("I am sorry Mandy but I could not understand") 
          return 0
       except sr.RequestError as e: 
          print("Could not request results from Google")
          return 0
        
def main(text):
        audio1 = listen1() 
        text = voice(audio1);
        if 'light on' in text:
          GPIO.output(led , 1)
          call(["espeak", "-s140  -ven+18 -z" , "Okay Mandy, Switching ON the Lights"])
          print ("Light on");
        elif 'light off' in text:
            GPIO.output(led , 0)
            call(["espeak", "-s140  -ven+18 -z" , "Okay Mandy, Switching off the Lights"])
            print ("light off");
        elif 'music' in text:
            call(["espeak", "-s140  -ven+18 -z" , "Okay Mandy, Now playing Space X song Rollout"])
            p.play();
            print ("Play Music");
        elif 'stop' in text:
            p.stop();
            call(["espeak", "-s140  -ven+18 -z" , "Okay Mandy, Music is stopped"])
            print ("Stopped");    
        elif 'say hi' in text:
            call(["espeak", "-s140  -ven+18 -z" , "Hello"])
            print ("say hi");     
        elif 'what is your name' in text:
            call(["espeak", "-s140  -ven+18 -z" , "My name is Bob"])
            print ("what is your name");
        elif 'alarm on' in text:
            call(["espeak", "-s140  -ven+18 -z" , "Okay Mandy, Turning on the alarm"])
            GPIO.output(alarm , 1)
            print ("alarm on");
        elif 'alarm off' in text:
            call(["espeak", "-s140  -ven+18 -z" , "Okay Mandy, Turning off the alarm"])
            GPIO.output(alarm , 0)
            print ("alarm off");    
        elif 'goodbye' in text:
            call(["espeak", "-s140  -ven+18 -z" , "Goodbye Mandy"])
            print ("Goodbye!");
            quit()
        text = {}
       

    
if __name__ == '__main__':
 while(1):
     audio1 = listen1() 
     text = voice(audio1)
     if text == 'Bob': 
         text = {}
         call(["espeak", "-s140  -ven+18 -z" ,"Okay Mandy, waiting for your command"])
         main(text)
     else:
         call(["espeak", "-s140  -ven+18 -z" ,"Please repeat"])              