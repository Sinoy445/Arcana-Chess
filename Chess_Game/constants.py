"""
Game constants for Chess Arcana.
"""

# Window dimensions
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700
BOARD_SIZE = 560
SQUARE_SIZE = BOARD_SIZE // 8
BOARD_OFFSET_X = (WINDOW_WIDTH - BOARD_SIZE) // 2
BOARD_OFFSET_Y = (WINDOW_HEIGHT - BOARD_SIZE) // 2
FPS = 60

# Colors
BG_COLOR = (20, 20, 40)
BOARD_LIGHT = (240, 217, 181)
BOARD_DARK = (181, 136, 99)
HIGHLIGHT_COLOR = (255, 255, 0, 100)  # Semi-transparent yellow
VALID_MOVE_COLOR = (0, 255, 0, 150)   # Semi-transparent green
TEXT_COLOR = (255, 255, 255)

# Piece types
PAWN = 0
KNIGHT = 1
BISHOP = 2
ROOK = 3
QUEEN = 4
KING = 5
MAGE = 6

# Colors
WHITE = 0
BLACK = 1

# Custom event for AI thinking
USEREVENT = pygame.USEREVENT