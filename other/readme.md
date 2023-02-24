Raspberry Pi Audio and Video Recorder
This is a Python script that records audio and video from a Logitech C270 webcam and saves the output to an MP4 file. It also provides a playback feature that merges the audio and video files and plays them back on the Raspberry Pi's HDMI output and 3.5mm audio jack.

Requirements
Raspberry Pi running Raspbian Buster or later
Logitech C270 webcam
USB audio adapter (if using HDMI output for video playback)
Pygame library (sudo apt-get install python-pygame)
FFMpeg (sudo apt-get install ffmpeg)
Installation
Connect the Logitech C270 webcam to the Raspberry Pi's USB port.
Connect the USB audio adapter to the Raspberry Pi's USB port (if using HDMI output for video playback).
Install the Pygame library and FFMpeg by running the following commands in a terminal:
csharp
Copy code
sudo apt-get install python-pygame
sudo apt-get install ffmpeg
Download the recorder.py file to your Raspberry Pi.
Run the recorder.py script in a terminal by typing python recorder.py.
Usage
Press button 1 to start recording. The script will record audio and video for a fixed period of time (10 seconds by default) and save the output to an MP4 file (output.mp4 by default).
Press button 2 to play back the merged audio and video. The script will play back the audio and video files using Pygame and display them on the Raspberry Pi's HDMI output and 3.5mm audio jack.
Note: You may need to adjust the recording settings and output file name in the recorder.py script to match your specific setup.