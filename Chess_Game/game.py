"""
Core game logic and main loop for Chess Arcana.
Handles game state, turns, and coordination between components.
"""

import pygame
from board import Board
from pieces import *
from constants import *

class Game:
    def __init__(self):
        """Initialize the game with board, pieces, and game state."""
        self.board = Board()
        self.selected_piece = None
        self.valid_moves = []
        self.turn = WHITE  # White starts
        self.score = {WHITE: 0, BLACK: 0}
        self.captured_pieces = {WHITE: [], BLACK: []}
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)

        # Game modes
        self.mode = "SELECTING"  # SELECTING, MOVING, GAME_OVER
        self.ai_mode = False  # Set to True for vs AI
        self.ai_thinking = False

    def run(self):
        """Main game loop."""
        screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Chess Arcana")
        clock = pygame.time.Clock()

        running = True
        while running:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_mouse_click(event.pos)
                elif event.type == pygame.KEYDOWN:
                    self.handle_keypress(event.key)

            # AI turn logic
            if self.ai_mode and self.turn == BLACK and not self.ai_thinking:
                self.ai_thinking = True
                pygame.time.set_timer(USEREVENT + 1, 500)  # AI thinks for 500ms

            # Update AI timer
            if self.ai_thinking:
                for event in pygame.event.get():
                    if event.type == USEREVENT + 1:
                        self.make_ai_move()
                        self.ai_thinking = False
                        pygame.time.set_timer(USEREVENT + 1, 0)

            # Draw everything
            self.draw(screen)
            pygame.display.flip()
            clock.tick(FPS)

    def handle_mouse_click(self, pos):
        """Handle mouse clicks on the board."""
        # Convert mouse position to board coordinates
        x, y = pos
        if x < BOARD_OFFSET_X or x > BOARD_OFFSET_X + BOARD_SIZE or \
           y < BOARD_OFFSET_Y or y > BOARD_OFFSET_Y + BOARD_SIZE:
            # Click outside board - check for UI clicks
            self.handle_ui_click(pos)
            return

        col = (x - BOARD_OFFSET_X) // SQUARE_SIZE
        row = (y - BOARD_OFFSET_Y) // SQUARE_SIZE

        if 0 <= row < BOARD_ROWS and 0 <= col < BOARD_COLS:
            piece = self.board.get_piece(row, col)

            if self.mode == "SELECTING":
                if piece and piece.color == self.turn:
                    self.select_piece(row, col)
            elif self.mode == "MOVING":
                if piece and piece.color == self.turn:
                    # Selecting a different piece
                    self.select_piece(row, col)
                elif (row, col) in self.valid_moves:
                    # Moving to a valid square
                    self.move_piece(row, col)
                else:
                    # Clicked invalid square - deselect
                    self.deselect_piece()

    def handle_keypress(self, key):
        """Handle keyboard shortcuts."""
        if key == pygame.K_ESCAPE:
            self.deselect_piece()
        elif key == pygame.K_r:
            self.reset_game()
        elif key == pygame.K_t:
            self.toggle_ai_mode()

    def handle_ui_click(self, pos):
        """Handle clicks on UI elements (revive buttons, etc.)."""
        # This would handle clicks on the sidebar for reviving pieces
        # Implementation depends on the UI layout
        pass

    def select_piece(self, row, col):
        """Select a piece and show its valid moves."""
        self.selected_piece = self.board.get_piece(row, col)
        self.valid_moves = self.selected_piece.get_valid_moves(self.board)
        self.mode = "MOVING"

    def deselect_piece(self):
        """Deselect the current piece."""
        self.selected_piece = None
        self.valid_moves = []
        self.mode = "SELECTING"

    def move_piece(self, row, col):
        """Move the selected piece to the target position."""
        target_piece = self.board.get_piece(row, col)
        start_row, start_col = self.selected_piece.row, self.selected_piece.col

        # Handle captures
        if target_piece:
            self.handle_capture(target_piece)

        # Move the piece
        self.board.move_piece(self.selected_piece, row, col)

        # Check for pawn promotion (simplified)
        self.check_promotion()

        # Switch turns
        self.switch_turn()
        self.deselect_piece()

    def handle_capture(self, piece):
        """Handle when a piece is captured."""
        # Add to captured pieces
        self.captured_pieces[piece.color].append(piece)

        # Add score based on piece value
        piece_value = self.get_piece_value(piece)
        self.score[self.turn] += piece_value

        # Remove from board
        self.board.remove_piece(piece)

    def get_piece_value(self, piece):
        """Get the point value of a piece."""
        values = {
            PAWN: 10,
            KNIGHT: 30,
            BISHOP: 30,
            ROOK: 50,
            QUEEN: 90,
            KING: 900,  # King is invaluable
            MAGE: 40    # Custom Mage piece value
        }
        return values.get(type(piece), 0)

    def check_promotion(self):
        """Check if a pawn should be promoted (simplified implementation)."""
        # In a full implementation, this would promote pawns reaching the back rank
        pass

    def switch_turn(self):
        """Switch turns between players."""
        self.turn = BLACK if self.turn == WHITE else WHITE

    def make_ai_move(self):
        """Make a move for the AI (simplified implementation)."""
        # Simple AI: look for captures, otherwise make random valid move
        import random

        # Get all black pieces and their valid moves
        black_pieces = []
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                piece = self.board.get_piece(row, col)
                if piece and piece.color == BLACK:
                    valid_moves = piece.get_valid_moves(self.board)
                    if valid_moves:
                        black_pieces.append((piece, valid_moves))

        if not black_pieces:
            return  # No valid moves

        # Prioritize captures
        capturing_moves = []
        for piece, moves in black_pieces:
            for move in moves:
                target_piece = self.board.get_piece(*move)
                if target_piece and target_piece.color == WHITE:
                    capturing_moves.append((piece, move))

        if capturing_moves:
            # Choose a random capturing move
            piece, move = random.choice(capturing_moves)
            self.selected_piece = piece
            self.valid_moves = [move]
            self.move_piece(*move)
        else:
            # Choose a random valid move
            piece, moves = random.choice(black_pieces)
            move = random.choice(moves)
            self.selected_piece = piece
            self.valid_moves = [move]
            self.move_piece(*move)

    def reset_game(self):
        """Reset the game to initial state."""
        self.board = Board()
        self.selected_piece = None
        self.valid_moves = []
        self.turn = WHITE
        self.score = {WHITE: 0, BLACK: 0}
        self.captured_pieces = {WHITE: [], BLACK: []}
        self.mode = "SELECTING"

    def toggle_ai_mode(self):
        """Toggle between 1-player and 2-player modes."""
        self.ai_mode = not self.ai_mode
        if not self.ai_mode:
            self.ai_thinking = False
            pygame.time.set_timer(USEREVENT + 1, 0)

    def draw(self, screen):
        """Draw the game state to the screen."""
        screen.fill(BG_COLOR)

        # Draw board
        self.board.draw(screen)

        # Draw selected piece highlight
        if self.selected_piece:
            self.draw_selection(screen)

        # Draw valid moves
        self.draw_valid_moves(screen)

        # Draw UI panels
        self.draw_score_panel(screen)
        self.draw_captured_panels(screen)
        self.draw_info_panel(screen)

    def draw_selection(self, screen):
        """Draw highlight around selected piece."""
        size = SQUARE_SIZE
        offset = BOARD_OFFSET_X
        y_offset = BOARD_OFFSET_Y

        x = self.selected_piece.col * size + offset
        y = self.selected_piece.row * size + y_offset

        pygame.draw.rect(screen, HIGHLIGHT_COLOR,
                        (x, y, size, size), 4)

    def draw_valid_moves(self, screen):
        """Draw circles on valid move squares."""
        radius = SQUARE_SIZE // 6
        for row, col in self.valid_moves:
            x = col * SQUARE_SIZE + BOARD_OFFSET_X + SQUARE_SIZE // 2
            y = row * SQUARE_SIZE + BOARD_OFFSET_Y + SQUARE_SIZE // 2
            pygame.draw.circle(screen, VALID_MOVE_COLOR, (x, y), radius)

    def draw_score_panel(self, screen):
        """Draw the score panel."""
        # This would draw the score information in the sidebar
        pass

    def draw_captured_panels(self, screen):
        """Draw panels showing captured pieces for each side."""
        # This would show captured pieces that can be revived
        pass

    def draw_info_panel(self, screen):
        """Draw game information and instructions."""
        # This would show current turn, game mode, instructions, etc.
        pass