# Trifecta

A dark, choose-your-own-adventure game with hidden secrets, multiple endings, and plenty of ways to die. Beware.

The project started as a text-based adventure and is being rebuilt as a retro 8-bit pygame game inspired by old-school Zelda — tile-based movement, hand-drawn pixel art sprites, and a Tiled map environment already in progress.

---

## The Story

You have entered the Trifecta. Three rooms stand between you and escape — a vast dark dining room, a hallway lined with unsettling paintings, and a chamber of treasure that is not what it seems. Every decision matters. Some paths lead to freedom. Most do not.

Good luck. You will need it.

---

## This Repo

The project lives in two stages:

**text-adventure/** — The original playable version of Trifecta, built in Python as a terminal-based choose-your-own-adventure. Fully playable right now. Features an inventory system, hidden secret interactions, and multiple endings including several ways to die.

**pygame-version/** — The current work-in-progress rebuild as a retro 8-bit game. Includes a Tiled map environment, custom pixel art sprites, and a working pygame window with player movement.

---

## Sprites & Map

| Cat Sprite | Scarf Bunny | Tiled Map |
|------------|-------------|-----------|
| ![Cat sprite](assets/cat_sprite.png) | ![Scarf bunny sprite](assets/scarf_bunny.png) | ![Tiled map](assets/trifecta_map.png) |

---

## How to Play (Text Adventure)

Open `text-adventure/trifecta_text_adventure.ipynb` in Jupyter Notebook or Google Colab and run the cells. Type your choices when prompted.

A few tips:
- Pay attention to everything in the room descriptions
- Some interactions are not listed in the options menu
- Your inventory matters more than you think

---

## Running the Pygame Version

```bash
pip install pygame pytmx
python pygame-version/trifecta_1_0.py
```

> Note: The pygame version is a work in progress. Asset paths may need to be updated to match your local directory.

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core language |
| Pygame | Game loop, rendering, player movement |
| Tiled / pytmx | Tile-based map design and loading |
| Piskel | Pixel art sprite creation |
| Jupyter Notebook | Text adventure prototype |

---

## Project Structure

```
trifecta/
├── README.md
├── text-adventure/
│   └── trifecta_text_adventure.ipynb
├── pygame-version/
│   ├── main.py
│   ├── trifecta_1_0.py
│   ├── trifecta_map_.tmx
│   ├── scarf_bunny.tsx
│   ├── cat_sprite_1.tsx
│   └── cat_ani.tsx
└── assets/
    ├── cat_sprite.png
    ├── scarf_bunny.png
    └── trifecta_map.png
```

---

## What's Next

- Tile-based player movement through the three rooms
- NPC interactions and dialogue system
- Hidden object triggers matching the text adventure secrets
- Sound effects and retro chiptune music
- Multiple endings carried over from the text adventure
