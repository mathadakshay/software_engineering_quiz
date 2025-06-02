# 🧠 Software Engineering Quiz App

A Python-based multiple-choice quiz game built with **Pygame** to test software engineering fundamentals interactively. This project helped strengthen my Python skills, GUI understanding, and debugging abilities—valuable for software development roles involving logic, prototyping, and system integration.

---

## 🚀 Features

- 15 software engineering questions with 4 options each
- Clickable buttons using Pygame's event handling
- Real-time feedback for each selected answer
- Final score display at the end of the quiz
- Logic separated from GUI (text-based version also included)

---

## 🛠️ Technologies Used

- **Python 3.x**
- **Pygame** (for GUI)
- **Modular programming** (separate logic and UI)

---

## ✅ My Contributions & Fixes

### 🔧 Fixed Issue: Mouse Click Not Working

- **Problem:** Mouse clicks weren’t registering because button creation (`buttons = []`) happened *after* the click check.
- **Fix:** Moved the button drawing and creation *above* the mouse event check.
- **Result:** Clicks now correctly select answers, and results display as expected.

### 🧪 Learning Through `test_quiz.py`

- Practiced and verified core quiz logic (scoring, flow, answer check) in a **text-only** version.
- Helped understand **logic-first development** before GUI implementation.

---

## 💡 Key Learnings

- Gained confidence in **event-driven programming** with Pygame
- Learned to separate logic from UI (important for scalable software)
- Improved **debugging** and **problem-solving** skills in Python
- Practiced writing **clean, readable, and modular code**
- Developed a hands-on project that simulates **real-world frontend/backend thinking**

---

## 🔗 How to Run the App

```bash
# 1. Install Pygame
pip install pygame

# 2. Run the game
python software_engineering_quiz.py
