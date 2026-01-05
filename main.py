import tkinter as tk
import pygame

# Initialize pygame mixer
pygame.mixer.init()

# Load the sound file
sound = pygame.mixer.Sound('skrimer-golden-freddi-fnaf-1.mp3')

# Set volume to 500% (5.0)
sound.set_volume(5.0)

def play_sound():
    sound.play()

# Create the main window
root = tk.Tk()
root.title("Screamer Button")
root.attributes('-fullscreen', True)  # Make it fullscreen

# Create a button that fills the entire screen
button = tk.Button(root, text="PRESS ME", command=play_sound, font=("Arial", 50))
button.pack(fill=tk.BOTH, expand=True)

# Run the application
root.mainloop()