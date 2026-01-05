import pygame
import os
import random
import time

# Initialize pygame
pygame.init()

# Get screen size
info = pygame.display.Info()
screen_width = info.current_w
screen_height = info.current_h

# Create fullscreen display
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.set_caption("Screamer Button")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Font
font = pygame.font.Font(None, 100)

# Button rect (full screen)
button_rect = pygame.Rect(0, 0, screen_width, screen_height)

# Load sound
sound_path = os.path.join(os.getcwd(), 'static', 'skrimer-golden-freddi-fnaf-1.mp3')
pygame.mixer.music.load(sound_path)
pygame.mixer.music.set_volume(5.0)

def shake_screen(duration=1.0, intensity=10):
    start_time = time.time()
    while time.time() - start_time < duration:
        offset_x = random.randint(-intensity, intensity)
        offset_y = random.randint(-intensity, intensity)
        screen.fill(BLACK)
        # Draw button with offset
        pygame.draw.rect(screen, RED, button_rect.move(offset_x, offset_y))
        text = font.render("PRESS ME", True, WHITE)
        text_rect = text.get_rect(center=(screen_width // 2 + offset_x, screen_height // 2 + offset_y))
        screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.wait(50)  # Small delay for shake effect

def play_sound():
    time.sleep(1)  # Wait 1 second
    pygame.mixer.music.play()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                shake_screen()
                play_sound()

    # Draw static screen
    screen.fill(BLACK)
    pygame.draw.rect(screen, RED, button_rect)
    text = font.render("PRESS ME", True, WHITE)
    text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()

pygame.quit()