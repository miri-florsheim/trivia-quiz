
def run_quiz(questions):
	score = 0
	for questions in questions:
		print(questions["prompt"])
		for optin in questions["options"]:
			print(optin)
		answer = input("Enter your answer (A, B, C, or D): ").upper()
		if answer == questions["answer"]:
			print("Very good!!\n")
			score += 1
		else:
			print('Wrong! The correct answer was", question["answer"], "\n')

	print(f"You got {score} out of {len(questions)} questions correct.")


# List of quiz questions. Each question is a dictionary.
questions = [
	{
		"prompt": "What is the capital city of France?",
		"options": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
		"answer": "A"
	},
	{
		"prompt": "Where is Big Ben?",
		"options": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
		"answer": "B"
	},
	{
		"prompt": "Where is the Tower of Pisa?",
		"options": ["A. London", "B. Paris", "C. Berlin", "D. Madrid"],
		"answer": "B"
	},
	{
		"prompt": "What is the capital city of Germany?",
		"options": ["A. Berlin", "B. London", "C. Paris", "D. Madrid"],
		"answer": "A"
	}
]

# Run the quiz
run_quiz(questions)