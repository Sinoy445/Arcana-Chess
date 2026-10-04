"""
Chess piece classes for Chess Arcana.
Includes all standard pieces plus the custom Mage piece.
"""

import pygame
from constants import *

class Piece:
    def __init__(self, color, row, col):
        """Initialize a piece with color and position."""
        self.color = color  # WHITE or BLACK
        self.row = row
        self.col = col
        self.has_moved = False
        self.image = None
        self.load_image()

    def load_image(self):
        """Load the piece image from assets."""
        # This would load the appropriate PNG image
        # For now, we'll draw shapes or use placeholder
        pass

    def draw(self, screen):
        """Draw the piece on the screen."""
        # Draw a circle or use the loaded image
        x = self.col * SQUARE_SIZE + BOARD_OFFSET_X + SQUARE_SIZE // 2
        y = self.row * SQUARE_SIZE + BOARD_OFFSET_Y + SQUARE_SIZE // 2

        # Choose color based on piece type
        if self.color == WHITE:
            color = (250, 250, 250)  # Off-white
        else:
            color = (20, 20, 20)     # Dark gray

        # Draw piece as a circle with border
        pygame.draw.circle(screen, color, (x, y), SQUARE_SIZE // 2 - 4)
        pygame.draw.circle(screen, (50, 50, 50), (x, y), SQUARE_SIZE // 2 - 4, 2)

        # Draw piece symbol in the center
        font = pygame.font.Font(None, SQUARE_SIZE // 2)
        text = font.render(self.get_symbol(), True,
                          (255, 255, 255) if self.color == BLACK else (0, 0, 0))
        text_rect = text.get_rect(center=(x, y))
        screen.blit(text, text_rect)

    def get_symbol(self):
        """Get the text symbol for this piece."""
        symbols = {
            PAWN: '♙' if self.color == WHITE else '♟︎',
            KNIGHT: '♘' if self.color == WHITE else '♞',
            BISHOP: '♗' if self.color == WHITE else '♝',
            ROOK: '♖' if self.color == WHITE else '♜',
            QUEEN: '♕' if self.color == WHITE else '♛',
            KING: '♔' if self.color == WHITE else '♚',
            MAGE: '♜' if self.color == WHITE else '♜'  # Using rook symbol for Mage for now
        }
        return symbols.get(self.type, '?')

    def get_valid_moves(self, board):
        """Get all valid moves for this piece."""
        # This should be overridden by each piece type
        return []

    def get_attacking_moves(self, board):
        """Get all squares this piece is attacking (regardless of own pieces)."""
        # Similar to valid moves but doesn't consider own pieces as blockers
        # for sliding pieces, etc.
        return self.get_valid_moves(board)

class Pawn(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.type = PAWN
        self.direction = -1 if color == WHITE else 1  # White moves up (-1), Black moves down (+1)

    def get_valid_moves(self, board):
        """Get valid moves for a pawn."""
        moves = []
        row, col = self.row, self.col

        # Forward move
        new_row = row + self.direction
        if board.is_valid_position(new_row, col) and not board.get_piece(new_row, col):
            moves.append((new_row, col))

            # Double move from starting position
            start_row = 6 if self.color == WHITE else 1
            if row == start_row:
                new_row2 = row + 2 * self.direction
                if board.is_valid_position(new_row2, col) and not board.get_piece(new_row2, col):
                    moves.append((new_row2, col))

        # Captures
        for dc in [-1, 1]:
            new_row = row + self.direction
            new_col = col + dc
            if board.is_valid_position(new_row, new_col):
                target = board.get_piece(new_row, new_col)
                if target and target.color != self.color:
                    moves.append((new_row, new_col))

        return moves

class Knight(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.type = KNIGHT

    def get_valid_moves(self, board):
        """Get valid moves for a knight."""
        moves = []
        row, col = self.row, self.col

        # All possible knight moves
        offsets = [
            (-2, -1), (-2, 1), (-1, -2), (-1, 2),
            (1, -2), (1, 2), (2, -1), (2, 1)
        ]

        for dr, dc in offsets:
            new_row, new_col = row + dr, col + dc
            if board.is_valid_position(new_row, new_col):
                target = board.get_piece(new_row, new_col)
                if not target or target.color != self.color:
                    moves.append((new_row, new_col))

        return moves

class Bishop(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.type = BISHOP

    def get_valid_moves(self, board):
        """Get valid moves for a bishop."""
        moves = []
        row, col = self.row, self.col

        # Diagonal directions
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

        for dr, dc in directions:
            for i in range(1, 8):  # Maximum 7 squares
                new_row, new_col = row + i * dr, col + i * dc
                if not board.is_valid_position(new_row, new_col):
                    break

                target = board.get_piece(new_row, new_col)
                if not target:
                    moves.append((new_row, new_col))
                elif target.color != self.color:
                    moves.append((new_row, new_col))
                    break  # Can't go further after capturing
                else:
                    break  # Blocked by own piece

        return moves

class Rook(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.type = ROOK

    def get_valid_moves(self, board):
        """Get valid moves for a rook."""
        moves = []
        row, col = self.row, self.col

        # Straight directions
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dr, dc in directions:
            for i in range(1, 8):  # Maximum 7 squares
                new_row, new_col = row + i * dr, col + i * dc
                if not board.is_valid_position(new_row, new_col):
                    break

                target = board.get_piece(new_row, new_col)
                if not target:
                    moves.append((new_row, new_col))
                elif target.color != self.color:
                    moves.append((new_row, new_col))
                    break  # Can't go further after capturing
                else:
                    break  # Blocked by own piece

        return moves

class Queen(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.type = QUEEN

    def get_valid_moves(self, board):
        """Get valid moves for a queen."""
        # Queen moves like a rook or bishop
        rook_moves = Rook(self.color, self.row, self.col).get_valid_moves(self.board)
        bishop_moves = Bishop(self.color, self.row, self.col).get_valid_moves(self.board)
        return rook_moves + bishop_moves

class King(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.type = KING

    def get_valid_moves(self, board):
        """Get valid moves for a king."""
        moves = []
        row, col = self.row, self.col

        # All 8 surrounding squares
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue  # Skip current position

                new_row, new_col = row + dr, col + dc
                if board.is_valid_position(new_row, new_col):
                    target = board.get_piece(new_row, new_col)
                    if not target or target.color != self.color:
                        # Additionally, check if moving here would put us in check
                        # (This is simplified - full implementation would be more complex)
                        moves.append((new_row, new_col))

        return moves

class Mage(Piece):
    """Custom Mage piece for Chess Arcana."""
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.type = MAGE
        # The Mage has unique movement - let's say it moves like a bishop
        # but can also jump one square orthogonal (like a king + bishop hybrid)

    def get_valid_moves(self, board):
        """Get valid moves for the Mage piece."""
        moves = []
        row, col = self.row, self.col

        # Bishop-like diagonal moves
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dr, dc in directions:
            for i in range(1, 8):  # Maximum 7 squares
                new_row, new_col = row + i * dr, col + i * dc
                if not board.is_valid_position(new_row, new_col):
                    break

                target = board.get_piece(new_row, new_col)
                if not target:
                    moves.append((new_row, new_col))
                elif target.color != self.color:
                    moves.append((new_row, new_col))
                    break  # Can't go further after capturing
                else:
                    break  # Blocked by own piece

        # King-like orthogonal moves (one square)
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue

                new_row, new_col = row + dr, col + dc
                if board.is_valid_position(new_row, new_col):
                    target = board.get_piece(new_row, new_col)
                    if not target or target.color != self.color:
                        moves.append((new_row, new_col))

        return moves

# Aliases for easier reference
PAWN = 0
KNIGHT = 1
BISHOP = 2
ROOK = 3
QUEEN = 4
KING = 5
MAGE = 6

WHITE = 0
BLACK = 1