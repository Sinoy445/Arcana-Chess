#!/usr/bin/env python3
"""
Chess Arcana - A Python-based chess game built with PyGame
featuring a custom Mage piece, score system, piece revival, and AI mode.
"""

import sys
import pygame
from game import Game

def main():
    """Main entry point for the Chess Arcana game."""
    # Initialize PyGame
    pygame.init()

    # Create and run the game
    game = Game()
    game.run()

    # Clean up
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()