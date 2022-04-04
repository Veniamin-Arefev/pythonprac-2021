"""Main game objects."""


class GameObjects():
    """Main game objects class."""

    monsters = {(i, j): {} for i in range(10) for j in range(10)}
    player_coords = 0 + 0j

    directions = {
        'up': 0 - 1j,
        'down': 0 + 1j,
        'left': -1 + 0j,
        'right': 1 + 0j,
    }
