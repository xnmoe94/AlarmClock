from datetime import datetime
from playsound import playsound
import pyttsx3

alarm_time = (input("Enter the time of alarm to be set:HH:MM:SS\n"))  # [12:40:12]
alarm_hour  = alarm_time[0:2]
alarm_minute = alarm_time[3:5]
alarm_seconds = alarm_time[6:8]
AM_PM = alarm_time[9:11]

print ('Setting Up the Alarm Colock')

while True:
    Engine = pyttsx3.init()

    now = datetime.now()
    current_hour = now.strftime("%I")
    current_minute = now.strftime("%M")
    current_seconds = now.strftime("%S")
    current_period = now.strftime("%p")

    if (AM_PM == current_period):
        if alarm_hour == current_hour:
            if alarm_minute == current_minute:
                if alarm_seconds == current_seconds:
                    Engine.say('Wake Up it is time for Work')
                    Engine.runAndWait()
                    playsound('/Users/muhammad/Desktop/audio.mp3')
                    break

