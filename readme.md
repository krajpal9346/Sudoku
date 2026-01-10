# 🧩 Sudoku AI – Intelligent Puzzle Game

A fully interactive **Sudoku web application** built using **Flask, HTML, CSS, and JavaScript**, featuring an AI-powered solver, multiple difficulty levels, real-time validation, and a clean, user-friendly interface.

This project demonstrates **algorithmic problem solving (backtracking)** combined with **frontend UX design**, making it suitable for **AI/ML, Web Development, and Software Engineering portfolios**.



## 🚀 Features

### 🎯 Gameplay
- 9×9 Sudoku board
- Three difficulty levels:
  - **Easy** – more predefined cells
  - **Medium** – moderate predefined cells
  - **Hard** – very few predefined cells
- Multiple predefined puzzles per difficulty (randomized)

### 🤖 AI Solver
- Uses **backtracking algorithm** to solve Sudoku
- Can instantly solve any valid puzzle

### ✅ Intelligent Validation
- **Check button** to validate user input
- Correct entries → highlighted in **green**
- Incorrect entries → highlighted in **red**
- If solved correctly → 🎉 **popup modal congratulates the user**
- If errors exist → clear guidance message shown

### 🎨 User Interface
- Bold borders separating 3×3 blocks
- Modern, responsive UI
- Clean button layout and color consistency
- Digits restricted to **1–9 only**



## 🛠️ Tech Stack

Backend - Flask (Python) 
Algorithm - Backtracking (Sudoku Solver)
Frontend - HTML, CSS, JavaScript
Styling - Custom CSS (modern UI)



## 📁 Project Structure

Sudoku/
- app.py
- requirements.txt
- readme.md
- static/
  - style.css
- templates/
  - index.html



## ⚙️ Installation & Setup

### 1. Clone the Repository
git clone https://github.com/your-username/sudoku-ai.git
cd sudoku-ai

### 2. Create Virtual Environment (Optional but Recommended)
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Run the Application
python app.py

### 5. Open in Browser
http://127.0.0.1:5000/



## 🧠 How It Works

🔹 Puzzle Generation
A predefined set of valid Sudoku puzzles is stored for each difficulty
A random puzzle is selected every time the game starts

🔹 Solver Logic
Uses recursive backtracking
Tries numbers 1–9 in empty cells
Ensures Sudoku constraints:
Row uniqueness
Column uniqueness
3×3 grid uniqueness

🔹 Validation System
On clicking Check:
User entries are compared with the solved board
Incorrect entries are highlighted
If all entries are correct, a success popup appears



## 📸 Screenshots
![Home](screenshots/home.png)
![Gameplay](screenshots/gameplay.png)
![Success](screenshots/success.png)
![Failure](screenshots/failure.png)



## 🔮 Future Enhancements
- Timer & score calculation
- Confetti animation on success
- New Game button
- Difficulty-based performance analytics
- Keyboard navigation support
- Deploy on cloud (Render / Vercel / Railway)