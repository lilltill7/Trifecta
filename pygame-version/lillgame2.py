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

# Set up the font
font = pygame.font.Font(None, 74)

# Room backgrounds (you can change these to images later)
room1_img = pygame.image.load("room1.jpg")

def draw_room(room_number):
    if room_number == 1:
        screen.blit(room1_img, (0, 0))  # Display the image at (0, 0)
    elif room_number == 2:
        screen.fill((150, 50, 50))  # Still use color for now
    elif room_number == 3:
        screen.fill((50, 150, 50))
    elif room_number == 2:
        screen.fill((150, 50, 50))  # Dark red for the second room
        text = font.render("Second Room", True, WHITE)
        screen.blit(text, (250, 250))
    elif room_number == 3:
        screen.fill((50, 150, 50))  # Dark green for the third room
        text = font.render("Third Room", True, WHITE)
        screen.blit(text, (250, 250))

# Main game loop
def game_loop():
    current_room = 1
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    current_room = 1
                elif event.key == pygame.K_2:
                    current_room = 2
                elif event.key == pygame.K_3:
                    current_room = 3

        draw_room(current_room)
        pygame.display.flip()
        pygame.time.Clock().tick(60)

if __name__ == "__main__":
    game_loop()
