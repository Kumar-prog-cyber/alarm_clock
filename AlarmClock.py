from datetime import datetime
from playsound import playsound
from gtts import gTTS
import os
text="Wake up it's Time To go"
output=gTTS(text=text,lang='en',slow=False)
output.save('output.mp3')
alarm_time=input("Enter the time for the alarm :HH:MM:SS\n")

alarm_hour=alarm_time[0:2]
alarm_minute=alarm_time[3:5]
alarm_second=alarm_time[6:8]
alarm_period=alarm_time[9:11].upper()
print("Alarm setting up...")
while True:
    now = datetime.now()
    current_Hour=now.strftime("%I")
    current_Minute=now.strftime("%M")
    current_Second=now.strftime("%S")
    current_period=now.strftime("%p")
    if(alarm_period == current_period):
        if(alarm_hour==current_Hour):
            if(alarm_minute==current_Minute):
                if(alarm_second==current_Second):
                    print("Wake Up")
                    playsound(os.system('start output.mp3'))
                    break


