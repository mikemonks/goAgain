import os
import pygame
import subprocess
import time
import RPi.GPIO as GPIO

# GPIO button pins
BUTTON_PINS = [26, 19, 13, 6, 5, 21, 20]

# Video settings for Logitech C270 webcam
VIDEO_DEVICE = "/dev/video0"
VIDEO_SIZE = "1280x720"
VIDEO_FPS = 30

# Audio settings for USB audio adapter
AUDIO_DEVICE = "hw:1"
AUDIO_CHANNELS = 2
AUDIO_RATE = 44100
AUDIO_FORMAT = "S16_LE"

# Recording settings
RECORDING_TIME = 10  # seconds
OUTPUT_FILE = "output.mp4"

# Initialize Pygame for audio playback
pygame.mixer.pre_init(channels=2, rate=AUDIO_RATE)
pygame.init()

# Set up GPIO
GPIO.setmode(GPIO.BCM)
for pin in BUTTON_PINS:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Function to start recording
def start_recording():
    # Build ffmpeg command for recording audio and video
    ffmpeg_cmd = (
        f"ffmpeg -f alsa -ac {AUDIO_CHANNELS} -ar {AUDIO_RATE} -i {AUDIO_DEVICE} "
        f"-f v4l2 -video_size {VIDEO_SIZE} -framerate {VIDEO_FPS} -i {VIDEO_DEVICE} "
        f"-t {RECORDING_TIME} -y {OUTPUT_FILE}"
    )

    # Start recording process
    subprocess.Popen(ffmpeg_cmd, shell=True)

# Function to play merged audio and video
def play_merged():
    # Load video and audio files
    video = pygame.movie.Movie(OUTPUT_FILE)
    audio = pygame.mixer.Sound(OUTPUT_FILE)

    # Set up video display on HDMI output
    pygame.display.init()
    pygame.display.set_mode((0,0), pygame.FULLSCREEN)

    # Play audio and video
    audio.play()
    video.play()

    # Wait for playback to finish
    while video.get_busy():
        pygame.time.Clock().tick(30)

# Main loop
while True:
    # Wait for button press
    GPIO.wait_for_edge(BUTTON_PINS, GPIO.FALLING)

    # Determine which button was pressed
    button_pin = GPIO.wait_for_edge(BUTTON_PINS, GPIO.RISING)

    # Start recording or playback depending on button
    if button_pin == BUTTON_PINS[0]:
        start_recording()
    elif button_pin == BUTTON_PINS[1]:
        play_merged()
