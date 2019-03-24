from Question import Question
question_prompts = [
    "Do you love me?\n(a) Yes\n(b) No\n(c) Maybe\n\n",
    "Do you really like me?\n(a) Yes\n(b) No\n(c) Maybe\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "a"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + "correct")

run_test(questions)