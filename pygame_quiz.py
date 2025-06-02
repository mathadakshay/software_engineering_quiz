import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Software Engineering Quiz")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Font
font = pygame.font.SysFont(None, 36)

# ✅ Helper functions
def draw_text(text, x, y, color=BLACK):
    rendered = font.render(text, True, color)
    screen.blit(rendered, (x, y))

def draw_button(text, x, y, w, h, color, hover_color, mouse_pos):
    rect = pygame.Rect(x, y, w, h)
    pygame.draw.rect(screen, hover_color if rect.collidepoint(mouse_pos) else color, rect)
    label = font.render(text, True, WHITE)
    screen.blit(label, (x + 10, y + 10))
    return rect

def welcome_screen():
    waiting = True
    while waiting:
        screen.fill(WHITE)
        draw_text("🎓 Welcome to the Software Engineering Quiz!", 100, 200)
        draw_text("Click anywhere to start...", 250, 300)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                waiting = False

# ✅ Main game loop
def main():
    questions = [
        {
            "question": "What does 'API' stand for?",
            "options": [
                "Application Programming Interface",
                "Applied Protocol Interface",
                "Advanced Program Interface",
                "Automated Programming Integration"
            ],
            "answer": "Application Programming Interface"
        },
        {
            "question": "What is the main goal of software testing?",
            "options": [
                "To write code",
                "To debug hardware",
                "To find and fix bugs",
                "To compile programs"
            ],
            "answer": "To find and fix bugs"
        },
        {
            "question": "Which model is also known as the linear sequential model?",
            "options": [
                "Agile Model",
                "Waterfall Model",
                "Spiral Model",
                "V-Model"
            ],
            "answer": "Waterfall Model"
        },
        {
            "question": "Which SDLC phase involves gathering system requirements?",
            "options": [
                "Design",
                "Implementation",
                "Testing",
                "Requirements Analysis"
            ],
            "answer": "Requirements Analysis"
        },
        {
            "question": "What is the full form of UML?",
            "options": [
                "Unified Markup Language",
                "Universal Modeling Language",
                "Unified Modeling Language",
                "User Mode Logic"
            ],
            "answer": "Unified Modeling Language"
        },
        {
            "question": "Which of the following is not a software development lifecycle model?",
            "options": [
                "Spiral",
                "V-Model",
                "Incremental",
                "Linear Binary"
            ],
            "answer": "Linear Binary"
        },
        {
            "question": "What does version control help with?",
            "options": [
                "Speeding up hardware",
                "Tracking changes to code",
                "Fixing compilation errors",
                "Creating user manuals"
            ],
            "answer": "Tracking changes to code"
        },
        {
            "question": "Which language is commonly used for backend development?",
            "options": [
                "HTML",
                "CSS",
                "JavaScript",
                "Python"
            ],
            "answer": "Python"
        },
        {
            "question": "Agile methodology emphasizes:",
            "options": [
                "Detailed documentation",
                "Rigid planning",
                "Customer collaboration",
                "Fixed contracts"
            ],
            "answer": "Customer collaboration"
        },
        {
            "question": "Which testing is done without executing the code?",
            "options": [
                "White-box Testing",
                "Black-box Testing",
                "Static Testing",
                "Regression Testing"
            ],
            "answer": "Static Testing"
        },
        {
            "question": "What is the purpose of unit testing?",
            "options": [
                "To test the complete system",
                "To test individual components",
                "To test security flaws",
                "To test the database"
            ],
            "answer": "To test individual components"
        },
        {
            "question": "Which of the following is an example of a non-functional requirement?",
            "options": [
                "User login feature",
                "System response time",
                "Search functionality",
                "Report generation"
            ],
            "answer": "System response time"
        },
        {
            "question": "SCRUM is a type of:",
            "options": [
                "Programming language",
                "Database system",
                "Agile framework",
                "Test automation tool"
            ],
            "answer": "Agile framework"
        },
        {
            "question": "Which of these is a CASE tool?",
            "options": [
                "Git",
                "Visual Paradigm",
                "Python",
                "React"
            ],
            "answer": "Visual Paradigm"
        },
        {
            "question": "What is refactoring?",
            "options": [
                "Adding new features",
                "Improving code without changing behavior",
                "Fixing bugs",
                "Running tests"
            ],
            "answer": "Improving code without changing behavior"
        }
    ]

    current_question = 0
    selected = None
    feedback = ""
    show_feedback = False
    feedback_timer = 0
    buttons = []
    score = 0
    quiz_finished = False

    running = True
    clock = pygame.time.Clock()

    while running:
        screen.fill(WHITE)
        mouse_pos = pygame.mouse.get_pos()

        if not quiz_finished:
            question = questions[current_question]
            draw_text(f"Question {current_question + 1} of {len(questions)}", 50, 20)
            draw_text(question["question"], 50, 60)

            buttons = []
            for i, option in enumerate(question["options"]):
                btn = draw_button(option, 100, 150 + i * 70, 600, 50, (0, 120, 215), (30, 144, 255), mouse_pos)
                buttons.append(btn)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                # ✅ Only left-click selects answers
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not show_feedback:
                    for idx, btn in enumerate(buttons):
                        if btn.collidepoint(mouse_pos):
                            selected = question["options"][idx]
                            if selected == question["answer"]:
                                feedback = "✅ Correct!"
                                score += 1
                            else:
                                feedback = f"❌ Wrong! Answer: {question['answer']}"
                            show_feedback = True
                            feedback_timer = pygame.time.get_ticks()

            # Show feedback
            if show_feedback:
                draw_text(feedback, 50, 450)
                if pygame.time.get_ticks() - feedback_timer > 2000:
                    show_feedback = False
                    selected = None
                    if current_question < len(questions) - 1:
                        current_question += 1
                    else:
                        quiz_finished = True
                        finish_time = pygame.time.get_ticks()

        else:
            draw_text("🎉 Quiz Finished!", 250, 200)
            draw_text(f"Your score: {score} / {len(questions)}", 270, 260)
            draw_text("Close the window to exit.", 270, 320)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

# ✅ Run game
welcome_screen()
main()
