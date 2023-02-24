import subprocess
import time
import RPi.GPIO as GPIO
import pygame

button_pins = [26, 19, 13, 6, 5, 21, 20]
video_device = "/dev/video0"
audio_device = "hw:1"
recording_time = 5

def record_audio_video():
    # Define the command to capture audio and video
    recording_command = [
        "ffmpeg",
        "-f", "alsa",
        "-i", audio_device,
        "-f", "video4linux2",
        "-input_format", "mjpeg",
        "-video_size", "640x480",
        "-i", video_device,
        "-t", str(recording_time),
        "-y",
        "output.mp4"
    ]

    # Start the recording process
    subprocess.run(recording_command)

def play_audio_video():
    # Initialize pygame mixer
    pygame.mixer.pre_init(44100, -16, 2, 1024)
    pygame.init()

    # Load the audio file
    audio = pygame.mixer.Sound("output.mp4")

    # Create a new display surface
    screen = pygame.display.set_mode((640, 480))

    # Play the audio and display the video
    audio.play()
    video = pygame.movie.Movie("output.mp4")
    video.set_display(screen, pygame.Rect((0, 0, 640, 480)))
    video.play()

    # Wait for the playback to finish
    while video.get_busy():
        pygame.time.Clock().tick(30)

    # Clean up resources
    audio.stop()
    video.stop()

def main():
    # Set up GPIO pins
    GPIO.setmode(GPIO.BCM)
    for pin in button_pins:
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    while True:
        # Wait for a button press
        input_state = GPIO.input(button_pins)
        if input_state == GPIO.LOW:
            # Record audio and video
            record_audio_video()

            # Play back the merged audio and video
            play_audio_video()

if __name__ == "__main__":
    main()
