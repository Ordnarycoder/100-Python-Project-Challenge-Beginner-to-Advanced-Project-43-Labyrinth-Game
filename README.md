# Labyrinth Game

## Description
The **Labyrinth Game** is a simple maze-solving game created using Python and the Pygame library. Players control a blue square and navigate through a maze to reach the green goal square. The game is designed to be a fun and engaging introduction to game development with Python.

---

## Features
- A static maze with walls and paths.
- Player movement using the arrow keys.
- A visual indicator for the goal.
- Simple and intuitive design for all age groups.

---

## Installation

### Prerequisites
- Python 3.8 or later.
- Pygame library.

### Steps to Install
1. Clone this repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd labyrinth-game
   ```
3. Install the required dependencies:
   ```bash
   pip install pygame
   ```

---

## How to Play
1. Run the game:
   ```bash
   python labyrinth.py
   ```
2. Use the **Arrow Keys** to move the player (blue square).
3. Navigate through the maze and reach the **green goal square**.
4. If you reach the goal, the game will display a winning message and exit.

---

## Project Structure
```
labyrinth-game/
├── labyrinth.py    # Main game file
├── README.md       # Project documentation
└── requirements.txt # Optional: Dependencies file
```

---

## Customization
- **Maze Layout**: You can modify the `maze` variable in `labyrinth.py` to create your own maze.
  - `1` represents walls.
  - `0` represents paths.
- **Player and Goal**: Change the colors or positions by editing the `player_pos` and `goal_pos` variables.

---

## Future Enhancements
Here are some ideas to expand the project:
- Add a timer to challenge players to solve the maze quickly.
- Randomly generate mazes using maze generation algorithms.
- Introduce obstacles or collectibles for added difficulty.
- Add multiple levels with increasing complexity.

---

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it as per the license terms.

---

## Acknowledgments
- Thanks to the Python and Pygame communities for making game development accessible and fun!

