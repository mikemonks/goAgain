import RPi.GPIO as GPIO
import time
import subprocess
from moviepy.editor import *

# Set up GPIO pins
GPIO.setmode(GPIO.BCM)
button_pins = [26, 19, 13, 6, 5, 21, 20]
for pin in button_pins:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Set up audio and video recording
audio_filename = "audio.wav"
video_filename = "video.mp4"
recording_command = ["ffmpeg", "-f", "alsa", "-i", "hw:1", "-f", "v4l2", "-r", "30", "-s", "1280x720", "-i", "/dev/video0", "-t", "5", "-c:v", "libx264", "-preset", "ultrafast", "-qp", "0", "-pix_fmt", "yuv420p", "-c:a", "aac", "-strict", "experimental", "-b:a", "192k", "-shortest", "-y", video_filename]

# Set up video playback
video_playback_command = ["omxplayer", "-o", "hdmi", "-b", video_filename]

# Main loop
while True:
    # Wait for button press
    for pin in button_pins:
        if GPIO.input(pin) == GPIO.LOW:
            button_pressed = pin
            break
    else:
        time.sleep(0.1)
        continue

    # Record audio and video
    subprocess.run(recording_command, check=True)

    # Merge audio and video
    video = VideoFileClip(video_filename)
    audio = AudioFileClip(audio_filename)
    video_with_audio = video.set_audio(audio)
    merged_filename = f"{button_pressed}.mp4"
    video_with_audio.write_videofile(merged_filename)

    # Play back video
    subprocess.run(video_playback_command, check=True)

    print(f"Button {button_pressed} pressed - audio and video merged to {merged_filename}")
