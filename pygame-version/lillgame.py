import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Trifecta Adventure")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the font for pixelated text (if you have a pixel font)
font = pygame.font.Font(None, 74)

# Main game loop
def game_loop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Fill screen with black
        screen.fill(BLACK)

        # Display some text in the center of the screen
        text = font.render("Welcome to the Trifecta", True, WHITE)
        text_rect = text.get_rect(center=(screen_width//2, screen_height//2))
        screen.blit(text, text_rect)

        # Update the display
        pygame.display.flip()

        # Frame rate control (60 FPS)
        pygame.time.Clock().tick(60)

# Start the game
if __name__ == "__main__":
    game_loop()
