Raspberry Pi Webcam Audio and Video Recording
This code is designed to run on a Raspberry Pi with a Logitech C270 webcam attached. It records audio and video when a button connected to one of the Raspberry Pi's GPIO pins is pressed, merges the audio and video into a single file, and plays back the resulting file on an HDMI display and a 1.6mm audio jack.

Installation
Before using this code, you will need to install a few dependencies on your Raspberry Pi:

Install ffmpeg by running the following command:

csharp
Copy code
sudo apt-get install ffmpeg
Install omxplayer by running the following command:

csharp
Copy code
sudo apt-get install omxplayer
Install the RPi.GPIO library by running the following command:

csharp
Copy code
sudo apt-get install python3-rpi.gpio
Install the moviepy library by running the following command:

Copy code
pip3 install moviepy
Usage
Connect your Logitech C270 webcam to your Raspberry Pi via USB.

Connect a button to one of the Raspberry Pi's GPIO pins. The button should be connected to the pin as follows: one leg of the button to the GPIO pin and the other leg to ground.

Update the button_pins list in the code to reflect the GPIO pins you have connected your button(s) to.

Run the code by executing the following command:

Copy code
python3 webcam_recording.py
Press one of the buttons connected to the Raspberry Pi's GPIO pins to start recording. The recording will last for 5 seconds.

After the recording is complete, the audio and video will be merged into a single file and played back on the HDMI display and the 1.6mm audio jack.

Customization
If you want to customize the video and audio recording settings, you can modify the recording_command list in the code. This list contains the command that ffmpeg uses to capture audio and video from the webcam.

If you want to customize the video playback settings, you can modify the video_playback_command list in the code. This list contains the command that omxplayer uses to play back the merged audio and video file.

Limitations
This code is designed to work specifically with the Logitech C270 webcam. If you are using a different webcam, you may need to modify the recording_command list to reflect the video and audio capture settings for your webcam.

This code is designed to capture audio from the webcam's built-in microphone. If you are using an external microphone, you will need to modify the recording_command list to reflect the input device for your microphone.