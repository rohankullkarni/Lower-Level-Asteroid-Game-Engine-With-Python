# Lower-Level-Asteroid-Game-Engine-With-Python
Algorithm based Asteroid-Rock game using Pygame and Numpy on Python



🎮 Gameplay
Control a spaceship at the bottom of the screen

Rocks fall from random positions at the top

Avoid collisions for as long as possible

When a collision occurs:

The game ends

Final survival time is displayed for 3 seconds

The window then closes automatically

🕹️ Controls
Key	Action

A	Move left

D	Move right

ESC / Close Window	Quit game


🧠 Game Logic Overview

Rock spawning uses a timer (pygame.time.get_ticks)

Movement & physics are frame-rate independent

Collision detection uses pygame.Rect.colliderect()

Score is calculated from survival time (seconds alive)

Game-over state keeps the window open for 3 seconds to display final score

📁 Project Structure

space-survival/

│
├── asteroids.py

├── spaceship.png

├── OIP.jpg

└── README.md

⚙️ Requirements

Python 3.8+

Pygame

NumPy

Install dependencies:

pip install pygame numpy

▶️ How to Run
python main.py


Make sure spaceship.png and OIP.jpg are in the same directory as main.py.

🧪 Features Implemented

✅ Random rock spawning

✅ Smooth movement using delta time

✅ Rect-based collision detection

✅ Survival-time scoring system

✅ Game-over screen with delayed exit

🚧 Possible Improvements

Increasing difficulty over time

Sound effects and background music

Explosion animations

High-score saving

Restart option instead of auto-exit

📜 License

This project is open-source and free to use for learning and experimentation.

👤 Author

Rohan Kulkarni
