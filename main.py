import tkinter as tk
import pygame
import os

# Initialize pygame mixer
pygame.mixer.init()

# Load the sound file
sound_path = os.path.join(os.getcwd(), 'static', 'skrimer-golden-freddi-fnaf-1.mp3')
pygame.mixer.music.load(sound_path)

# Set volume to 500% (5.0)
pygame.mixer.music.set_volume(5.0)

def play_sound():
    pygame.mixer.music.play()

# Create the main window
root = tk.Tk()
root.title("Screamer Button")
root.attributes('-fullscreen', True)  # Make it fullscreen

# Create a button that fills the entire screen
button = tk.Button(root, text="PRESS ME", command=play_sound, font=("Arial", 50))
button.pack(fill=tk.BOTH, expand=True)

# Run the application
root.mainloop()