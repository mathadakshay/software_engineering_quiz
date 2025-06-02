import random

# Welcome message
intro_message = "Welcome to Quiz. You have 15 questions in total without any time limit."

# 15 Software Engineering Questions
quiz_data = [
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
        "question": "Which programming language is known for its use in web development alongside HTML and CSS?",
        "options": ["Python", "Java", "JavaScript", "C++"],
        "answer": "JavaScript"
    },
    {
        "question": "What is the main purpose of version control systems like Git?",
        "options": [
            "To speed up the processor",
            "To control who can log into your system",
            "To track and manage changes to code",
            "To deploy code to production"
        ],
        "answer": "To track and manage changes to code"
    },
    {
        "question": "Which of the following is a popular Python web framework?",
        "options": ["Django", "Spring", "React", "Laravel"],
        "answer": "Django"
    },
    {
        "question": "What does 'OOP' stand for in software development?",
        "options": [
            "Open Operational Protocol",
            "Object-Oriented Programming",
            "Optimal Output Processing",
            "Overloaded Object Pattern"
        ],
        "answer": "Object-Oriented Programming"
    },
    {
        "question": "Which of these is NOT a software development life cycle model?",
        "options": ["Waterfall", "Agile", "Spiral", "Convolutional"],
        "answer": "Convolutional"
    },
    {
        "question": "Which HTTP method is typically used to update data on a server?",
        "options": ["GET", "POST", "PUT", "DELETE"],
        "answer": "PUT"
    },
    {
        "question": "What does 'CI/CD' stand for?",
        "options": [
            "Code Integration / Code Deployment",
            "Continuous Integration / Continuous Delivery",
            "Computer Interface / Central Debugging",
            "Code Input / Code Distribution"
        ],
        "answer": "Continuous Integration / Continuous Delivery"
    },
    {
        "question": "Which of the following is a relational database management system?",
        "options": ["MongoDB", "MySQL", "Redis", "Cassandra"],
        "answer": "MySQL"
    },
    {
        "question": "What symbol is used for comments in Python?",
        "options": ["//", "#", "/* */", "<!-- -->"],
        "answer": "#"
    },
    {
        "question": "Which one of these is a NoSQL database?",
        "options": ["MySQL", "Oracle", "MongoDB", "PostgreSQL"],
        "answer": "MongoDB"
    },
    {
        "question": "What is 'debugging' in software development?",
        "options": [
            "Adding new features",
            "Testing the UI design",
            "Removing errors from code",
            "Designing the database schema"
        ],
        "answer": "Removing errors from code"
    },
    {
        "question": "Which tool is commonly used for project management in software teams?",
        "options": ["Excel", "Slack", "Jira", "Outlook"],
        "answer": "Jira"
    },
    {
        "question": "In Python, what does the 'len()' function do?",
        "options": [
            "Returns the type of a variable",
            "Counts the number of lines in a file",
            "Returns the length of an object",
            "Converts data to lowercase"
        ],
        "answer": "Returns the length of an object"
    },
    {
        "question": "Which data structure uses FIFO (First In First Out)?",
        "options": ["Stack", "Queue", "Tree", "HashMap"],
        "answer": "Queue"
    }
]

def run_quiz():
    print(intro_message)

    score = 0
    questions = random.sample(quiz_data, 15)

    for i, q in enumerate(questions):
        print(f"\nQuestion {i+1}: {q['question']}")
        for idx, option in enumerate(q['options'], start=1):
            print(f"{idx}. {option}")

        while True:
            try:
                answer = int(input("Your answer (1-4): "))
                if answer < 1 or answer > 4:
                    raise ValueError
                break
            except ValueError:
                print("⚠️ Please enter a valid number between 1 and 4.")

        selected = q['options'][answer - 1]
        if selected == q['answer']:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was: {q['answer']}")

    print("\n🎯 Quiz Over!")
    print(f"Your final score: {score} out of 15")

    replay = input("Do you want to play again? (yes/no): ").lower()
    if replay == "yes":
        run_quiz()

# Start the quiz
run_quiz()
