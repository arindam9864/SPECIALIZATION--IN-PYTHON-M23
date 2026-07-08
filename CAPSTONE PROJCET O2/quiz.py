
class Quiz:
    def __init__(self):

        self.questions = [
            {
                "question": "1. What does CPU stand for?",
                "options": ["A. Central Processing Unit", "B. Computer Power Unit", "C. Central Program Unit", "D. Control Processing Unit"],
                "answer": "A"
            },
            {
                "question": "2. Which device is used to enter data into a computer?",
                "options": ["A. Monitor", "B. Keyboard", "C. Printer", "D. Speaker"],
                "answer": "B"
            },
            {
                "question": "3. Which of the following is an operating system?",
                "options": ["A. Python", "B. Windows", "C. Google", "D. Chrome"],
                "answer": "B"
            },
            {
                "question": "4. Which storage device has the largest capacity?",
                "options": ["A. CD", "B. DVD", "C. Hard Disk", "D. Floppy Disk"],
                "answer": "C"
            },
            {
                "question": "5. Which language is used to create web pages?",
                "options": ["A. HTML", "B. MS Word", "C. Windows", "D. Excel"],
                "answer": "A"
            }
        ]
        self.score = 0

    def start(self):
        print("\n===== COMPUTER BASICS QUIZ =====")

        for q in self.questions:
            print("\n" + q["question"])
            for option in q["options"]:
                print(option)

            user_answer = input("Enter your answer (A/B/C/D): ").upper()

            if user_answer == q["answer"]:
                print("Correct!")
                self.score += 1
            else:
                print("Wrong! Correct Answer:", q["answer"])

        self.result()

    def result(self):
        print("\n===== RESULT =====")
        print("Your Score:", self.score, "/", len(self.questions))

        if self.score == 5:
            print("Excellent!")
        elif self.score >= 3:
            print("Good Job!")
        else:
            print("Keep Practicing!")

while True:
    quiz = Quiz()
    quiz.start()

    again = input("\nDo you want to play again? (yes/no): ").lower()
    if again != "yes":
        print("Thank you for playing!")
        break
