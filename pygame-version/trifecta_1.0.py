import pygame
import pytmx
from pytmx.util_pygame import load_pygame

# Initialize Pygame
pygame.init()

# Screen setup
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Lilla's Animated Game")

try:
    # Load Tiled map
    tmx_data = load_pygame("C:/Users/Lilla/lillpygame/trifecta map1.0.tmx")

    # Load player sprite
    spritesheet = pygame.image.load("C:/Users/Lilla/Downloads/New Piskel (1).png").convert_alpha()
except Exception as e:
    print("Error loading files:", e)
    pygame.quit()
    exit()

frame_width = 32  # Width of each frame in pixels
frame_height = 32  # Height of each frame in pixels
frame_count = 3  # Total number of frames in the animation (update to match the actual frames)
current_frame = 0  # Start at the first frame
animation_speed = 0.1  # Speed of animation
frame_timer = 0

# Extract frames from the spritesheet with bounds checking
frames = [
    spritesheet.subsurface(pygame.Rect(i * frame_width, 0, frame_width, frame_height))
    for i in range(frame_count)
    if (i + 1) * frame_width <= spritesheet.get_width()  # Ensure within bounds
]
print(f"Loaded {len(frames)} frames for the animation.")  # Debugging check

# Set initial player position
player_rect = frames[0].get_rect(topleft=(50, 50))

# Movement speed
speed = 5

# Function to draw the Tiled map
def draw_map():
    for layer in tmx_data.visible_layers:
        if isinstance(layer, pytmx.TiledTileLayer):
            for x, y, gid in layer:
                tile = tmx_data.get_tile_image_by_gid(gid)
                if tile:
                    screen.blit(tile, (x * tmx_data.tilewidth, y * tmx_data.tileheight))

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key states for movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= speed  # Move left
    if keys[pygame.K_RIGHT]:
        player_rect.x += speed  # Move right
    if keys[pygame.K_UP]:
        player_rect.y -= speed  # Move up
    if keys[pygame.K_DOWN]:
        player_rect.y += speed  # Move down

    # Update animation frame
    frame_timer += animation_speed
    if frame_timer >= 1:
        frame_timer = 0
        current_frame = (current_frame + 1) % len(frames)

    # Clear the screen and draw the map
    screen.fill((0, 0, 0))
    draw_map()  # Draw the Tiled map

    # Draw the current frame of the animated sprite
    screen.blit(frames[current_frame], player_rect)

    # Update the display
    pygame.display.flip()
    pygame.time.Clock().tick(30)  # Frame rate

# Quit Pygame
pygame.quit()
