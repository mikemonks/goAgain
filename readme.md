Raspberry Pi Button Recorder
This is a Python program for the Raspberry Pi that records audio and video when a button is pressed and plays back the merged audio and video when the button is pressed again. It uses ffmpeg to capture the audio and video, and pygame to play back the merged file. The program is designed to work with a Logitech C270 HD webcam, a USB audio adapter, and Raspbian Buster or later.

Installation
Install the required packages:

bash
Copy code
sudo apt-get update
sudo apt-get install python3 python3-pip python3-pygame ffmpeg
Clone the repository:

bash
Copy code
git clone https://github.com/exampleuser/rpi-button-recorder.git
cd rpi-button-recorder
Edit the button_pins, video_device, audio_device, and recording_time variables in recorder.py to match your setup.

Usage
Connect the button(s) to the GPIO pins specified in button_pins. The buttons should be connected between the GPIO pins and ground.

Run the program:

bash
Copy code
python3 recorder.py
Press one of the buttons to start recording. The program will record audio and video for recording_time seconds and save the output to output.mp4.

Press the same button again to play back the merged audio and video. The program will use pygame to play the file and display the video on the HDMI output and the audio on the 3.5mm audio jack.

Contributing
Contributions are welcome! If you find a bug or have a feature request, please open an issue on the GitHub repository. If you would like to contribute code, please fork the repository and submit a pull request with your changes.

License
This code is licensed under the MIT License. See the LICENSE file for details.