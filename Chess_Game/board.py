"""
Board management for Chess Arcana.
Handles the 8x8 grid and piece placement.
"""

import pygame
from pieces import *
from constants import *

class Board:
    def __init__(self):
        """Initialize the chess board with starting piece positions."""
        self.grid = [[None for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
        self.white_king_pos = (0, 4)  # Will be updated when king is placed
        self.black_king_pos = (7, 4)  # Will be updated when king is placed
        self.setup_board()

    def setup_board(self):
        """Set up the initial chess position."""
        # Clear board
        self.grid = [[None for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

        # Place pawns
        for col in range(BOARD_COLS):
            self.grid[1][col] = Pawn(BLACK, 1, col)
            self.grid[6][col] = Pawn(WHITE, 6, col)

        # Place back row pieces
        back_row = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        for col, piece_class in enumerate(back_row):
            # Black pieces (top row)
            self.grid[0][col] = piece_class(BLACK, 0, col)
            if piece_class == King:
                self.black_king_pos = (0, col)
            # White pieces (bottom row)
            self.grid[7][col] = piece_class(WHITE, 7, col)
            if piece_class == King:
                self.white_king_pos = (7, col)

        # Place the Mage pieces (custom piece)
        # Replace one bishop with a Mage on each side for variety
        # Black Mage replaces c-file bishop (col 2)
        self.grid[0][2] = Mage(BLACK, 0, 2)
        # White Mage replaces f-file bishop (col 5)
        self.grid[7][5] = Mage(WHITE, 7, 5)

    def draw(self, screen):
        """Draw the chess board and pieces."""
        # Draw squares
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                color = BOARD_LIGHT if (row + col) % 2 == 0 else BOARD_DARK
                x = col * SQUARE_SIZE + BOARD_OFFSET_X
                y = row * SQUARE_SIZE + BOARD_OFFSET_Y
                pygame.draw.rect(screen, color,
                               (x, y, SQUARE_SIZE, SQUARE_SIZE))

        # Draw pieces
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                piece = self.grid[row][col]
                if piece:
                    piece.draw(screen)

    def get_piece(self, row, col):
        """Get the piece at the specified position."""
        if 0 <= row < BOARD_ROWS and 0 <= col < BOARD_COLS:
            return self.grid[row][col]
        return None

    def set_piece(self, piece, row, col):
        """Set a piece at the specified position."""
        if 0 <= row < BOARD_ROWS and 0 <= col < BOARD_COLS:
            self.grid[row][col] = piece
            if piece:
                piece.row = row
                piece.col = col

    def remove_piece(self, piece):
        """Remove a piece from the board."""
        if piece and 0 <= piece.row < BOARD_ROWS and 0 <= piece.col < BOARD_COLS:
            self.grid[piece.row][piece.col] = None

    def move_piece(self, piece, row, col):
        """Move a piece to a new position."""
        # Clear old position
        self.grid[piece.row][piece.col] = None
        # Set new position
        self.grid[row][col] = piece
        piece.row = row
        piece.col = col

        # Update king positions if needed
        if isinstance(piece, King):
            if piece.color == WHITE:
                self.white_king_pos = (row, col)
            else:
                self.black_king_pos = (row, col)

    def is_valid_position(self, row, col):
        """Check if a position is within board bounds."""
        return 0 <= row < BOARD_ROWS and 0 <= col < BOARD_COLS

    def is_square_attacked(self, row, col, color):
        """
        Check if a square is under attack by pieces of the given color.
        Used for checking if king is in check.
        """
        # Check all squares for pieces of the given color
        for r in range(BOARD_ROWS):
            for c in range(BOARD_COLS):
                piece = self.get_piece(r, c)
                if piece and piece.color != color:  # Opponent's piece
                    # Check if this piece can attack the target square
                    if (row, col) in piece.get_attacking_moves(self):
                        return True
        return False