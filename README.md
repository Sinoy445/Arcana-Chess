# ♟️ Chess Arcana

> A Python-based chess game built with PyGame — featuring a custom Mage piece, a score system, piece revival, and a single-player AI mode.

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat&logo=python&logoColor=white)
![PyGame](https://img.shields.io/badge/PyGame-2.x-brightgreen?style=flat)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat)
![Status](https://img.shields.io/badge/Status-In%20Development-orange?style=flat)

---

## 📖 About

**Chess Arcana** enhances the traditional chess experience with new strategic mechanics. Play against a friend locally or challenge the built-in AI — capture pieces to earn points, revive fallen allies, and unleash the power of the custom **Mage** unit.

---

## 🚀 Features

- 🎮 **Two Game Modes** — 1 Player (vs AI) and 2 Player (local multiplayer)
- 🤖 **AI Opponent** — prioritizes captures, falls back to valid random moves
- 💰 **Score System** — earn points by capturing enemy pieces
- 🔄 **Revive System** — spend score to bring back captured pieces (once per piece type per game)
- 🧙 **Mage Piece** — a custom unit with unique movement and strategic depth
- 🖼️ **PNG-based sprites** for all chess pieces
- 📊 **Live Sidebar** — tracks turn, scores, game mode, and status messages

---

## 🛠️ Tech Stack

| Technology | Version |
|------------|---------|
| Python     | 3.11    |
| PyGame     | 2.x     |

---

## 📁 Project Structure

```
Chess_Arcana/
│
├── main.py         # Entry point
├── game.py         # Core game logic & main loop
├── board.py        # Board management (8×8 grid)
├── pieces.py       # Piece classes (Pawn, Knight, Bishop, Rook, Queen, King, Mage)
│
└── assets/
    └── images/     # PNG sprites for all chess pieces
```

---

## ▶️ Installation & Running

### 1. Clone the repository

```bash
git clone https://github.com/your-username/chess-arcana.git
cd chess-arcana
```

### 2. Install dependencies

```bash
py -3.11 -m pip install pygame
```

### 3. Launch the game

```bash
py -3.11 main.py
```

---

## 🎮 How to Play

### Main Menu
Select your mode on launch:
- **1 Player** — play against the AI (you play as White)
- **2 Players** — local multiplayer, White goes first

### Controls

| Input | Action |
|-------|--------|
| **Left Click** | Select and move a piece |
| **P** | Revive a Pawn |
| **N** | Revive a Knight |
| **B** | Revive a Bishop |
| **R** | Revive a Rook |
| **Q** | Revive a Queen |
| **M** | Revive a Mage |
| **T** | Reset the game |
| **Backspace** | Return to main menu |
| **ESC** | Quit the game |

### Revive Rules
- Capture enemy pieces to earn score points
- Use your score to revive a captured ally
- Each piece type can only be revived **once per game**

---

## 🤖 AI Behaviour

The AI controls the Black pieces in 1 Player mode:

1. Scans all valid moves for every Black piece
2. **Priority:** captures any White piece if possible
3. **Fallback:** plays a random valid move
4. Passes control back to the human player (White)

---


## 🗺️ Roadmap

- [ ] Improved AI (Minimax / Alpha-Beta pruning)
- [ ] Sound effects & background music
- [ ] Animated piece movement
- [ ] Online multiplayer
- [ ] Difficulty levels for AI

---

## 👤 Author

**REKIK Yassine**
Cycle Ingénieur – 4ᵉ Année

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
