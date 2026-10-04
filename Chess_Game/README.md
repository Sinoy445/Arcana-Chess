# ♟️ Chess Arcana

> A Python-based chess game built with PyGame — featuring a custom Mage piece, a score system, piece revival, and a single-player AI mode.

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![PyGame](https://img.shields.io/badge/pygame-2.5%2B-brightgreen)
![License](https://img.shields.io/badge/license-MIT-green)

## 📖 About

**Chess Arcana** enhances the traditional chess experience with new strategic mechanics. Play against a friend locally or challenge the built-in AI — capture pieces to earn points, revive fallen allies, and unleash the power of the custom **Mage** unit.

## 🚀 Features

- 🎮 **Two Game Modes** — 1 Player (vs AI) and 2 Player (local multiplayer)
- 🤖 **AI Opponent** — prioritizes captures, falls back to valid random moves
- 💰 **Score System** — earn points by capturing enemy pieces
- 🔄 **Revive System** — spend score to bring back captured allies (once per piece type per game)
- 🧙 **Mage Piece** — a custom unit with unique movement (bishop + king hybrid)
- 🖼️ **PNG-based sprites** for all chess pieces
- 📊 **Live Sidebar** — tracks turn, scores, game mode, and status messages
- ⌨️ **Keyboard Controls** — intuitive hotkeys for gameplay

## 🛠️ Tech Stack

- **Language:** Python 3.8+
- **Graphics:** PyGame 2.5+
- **Development:** IDE agnostic

## 📁 Project Structure

```
Chess_Arcana/
├── main.py             # Entry point
├── game.py             # Core game logic & main loop
├── board.py            # Board management (8×8 grid)
├── pieces.py           # Piece classes (Pawn, Knight, Bishop, Rook, Queen, King, Mage)
├── constants.py        # Game constants and configuration
├── assets/
│   └── images/         # PNG sprites for all chess pieces
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

## ▶️ Installation & Running

### 1. Clone the repository
```bash
git clone https://github.com/your-username/chess-arcana.git
cd chess-arcana
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```
or
```bash
pip install pygame>=2.5.0
```

### 3. Launch the game
```bash
python main.py
```

## 🎮 How to Play

### Main Menu
Select your mode on launch:
- **1 Player** — play against the AI (you play as White)
- **2 Players** — local multiplayer, White goes first

### Controls

| Key | Action |
|-----|--------|
| **Left Click** | Select and move a piece |
| **F6** | Toggle clicking on / off (for testing) |
| **ESC** | Deselect piece or cancel action |
| **R** | Reset the game |
| **T** | Toggle AI mode on/off |
| **Q** | Quit the game |

### Gameplay
1. Click on a piece to select it (valid moves will be highlighted)
2. Click on a highlighted square to move the piece
3. Capture enemy pieces to earn score points
4. Use your score to revive captured allies (once per piece type)
5. Checkmate your opponent to win!

## 🧙‍♂️ About the Mage Piece

The Mage is a custom chess piece that combines the movement of a Bishop (diagonal) and a King (one square in any direction). This creates a unique hybrid piece that adds new strategic depth to the game.

## 🤖 AI Behaviour

The AI controls the Black pieces in 1 Player mode:

1. **Scan** all valid moves for every Black piece
2. **Priority:** captures any White piece if possible
3. **Fallback:** plays a random valid move
4. **Delay:** thinks for 500ms before moving to simulate deliberation

## 📋 Roadmap

- [ ] Improved AI (Minimax / Alpha-Beta pruning)
- [ ] Sound effects & background music
- [ ] Animated piece movement
- [ ] Online multiplayer
- [ ] Difficulty levels for AI
- [ ] Tournament mode with scoring
- [ ] Move undo/redo functionality
- [ ] Customizable board themes

## 👤 Author

**REKIK Yassine**  
Cycle Ingénieur – 4ᵉ Année

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.