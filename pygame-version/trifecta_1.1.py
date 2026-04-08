import pygame
import pytmx
from pytmx.util_pygame import load_pygame
import time

def load_tile_animations(tmx_data):
    animations = {}
    for tileset in tmx_data.tilesets:
        for tile_id in range(tileset.firstgid, tileset.firstgid + tileset.tilecount):
            tile = tmx_data.get_tile_properties_by_gid(tile_id)
            if tile and 'animation' in tile:
                animations[tile_id] = [(frame.gid, frame.duration) for frame in tile['animation']]
    return animations

def draw_map(screen, tmx_data, animations, center_x, center_y, current_time):
    screen_width, screen_height = screen.get_size()
    for layer in tmx_data.visible_layers:
        if isinstance(layer, pytmx.TiledTileLayer):
            for x, y, gid in layer:
                tile_image = None
                animation = animations.get(gid)
                if animation:
                    total_duration = sum(duration for _, duration in animation)
                    time_in_animation = current_time % total_duration
                    elapsed = 0
                    for frame_gid, duration in animation:
                        if elapsed + duration > time_in_animation:
                            tile_image = tmx_data.get_tile_image_by_gid(frame_gid)
                            break
                        elapsed += duration
                else:
                    tile_image = tmx_data.get_tile_image_by_gid(gid)

                if tile_image:
                    tile_screen_x = (x * tmx_data.tilewidth) - center_x + screen_width // 2
                    tile_screen_y = (y * tmx_data.tileheight) - center_y + screen_height // 2
                    screen.blit(tile_image, (tile_screen_x, tile_screen_y))

def main():
    pygame.init()
    screen_width, screen_height = 1280, 720
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    tmx_data = load_pygame('C:/Users/Lilla/lillpygame/trifecta map..tmx')
    animations = load_tile_animations(tmx_data)
    player_image = pygame.image.load('C:/Users/Lilla/Downloads/New Piskel (1).png').convert_alpha()
    player_rect = player_image.get_rect(center=(screen_width // 2, screen_height // 2))
    player_speed = 0.5
    start_time = time.time()

    running = True
    while running:
        current_time = (time.time() - start_time) * 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_rect.x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_rect.x += player_speed
        if keys[pygame.K_UP]:
            player_rect.y -= player_speed
        if keys[pygame.K_DOWN]:
            player_rect.y += player_speed

        screen.fill((0, 0, 0))
        draw_map(screen, tmx_data, animations, player_rect.centerx, player_rect.centery, current_time)
        screen.blit(player_image, player_rect)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
