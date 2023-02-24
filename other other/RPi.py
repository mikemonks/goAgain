import RPi.GPIO as GPIO
import time
import os

#variables:
butPressed = [True, True, True, True, True, True, True]#if button i is pressed, then butPressed[i] is False
pin = [26, 19, 13, 6, 5, 21, 20]#GPIO pins of each button
recordBool = False#True if a record is in progress

GPIO.setmode(GPIO.BCM)
for i in range(0, 7):
    GPIO.setup(pin[i], GPIO.IN, pull_up_down=GPIO.PUD_UP)#sets Pi's internal resistors to pull-up

while True:
    for i in range(0, 7):
        butPressed[i] = GPIO.input(pin[i])#checks if a button is pressed
        if butPressed[i] == False:#if a button is pressed
            previousTime = time.time()
            while butPressed[i] == False and recordBool == False:
                butPressed[i] = GPIO.input(pin[i])
                if time.time() - previousTime > 1.0:#if the button is pressed for more than a second, then recordBool is True
                    recordBool = True

            if recordBool == True:#if recordBool is True, it plays a beep sound and then records
                os.system("aplay -D plughw:CARD=Device_1,DEV=0 beep.wav")
                os.system("arecord %d.wav -D sysdefault:CARD=1 -f cd -d 20 &" %i)#records for maximum 20 seconds in file i.wav, with cd quality
                while butPressed[i] == False:
                    butPressed[i] = GPIO.input(pin[i])

                os.system("pkill -9 arecord")#the record is stopped when the button is let go, or after 20 seconds
                recordBool = False

            else:#if recordBool is False, it plays sound i.wav
                os.system("aplay -D plughw:CARD=Device_1,DEV=0 %d.wav" %i)

    time.sleep(0.1)