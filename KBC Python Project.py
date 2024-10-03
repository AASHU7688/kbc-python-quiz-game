import random

questions = [
    {
        "question": "Who is the President of the United States?",
        "options": ["A) Joe Biden", "B) Donald Trump", "C) Barack Obama", "D) George Bush"],
        "answer": "A"
    },
    {
        "question": "What is the capital of France?",
        "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Lisbon"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Venus"],
        "answer": "B"
    },
    {
        "question": "Which element has the chemical symbol 'O'?",
        "options": ["A) Gold", "B) Oxygen", "C) Osmium", "D) Zinc"],
        "answer": "B"
    },
    {
        "question": "What is the tallest mountain in the world?",
        "options": ["A) K2", "B) Kangchenjunga", "C) Lhotse", "D) Everest"],
        "answer": "D"
    },
    {
        "question": "Who wrote 'Hamlet'?",
        "options": ["A) William Wordsworth", "B) William Shakespeare", "C) Charles Dickens", "D) Jane Austen"],
        "answer": "B"
    },
    {
        "question": "Which is the largest ocean on Earth?",
        "options": ["A) Atlantic Ocean", "B) Indian Ocean", "C) Arctic Ocean", "D) Pacific Ocean"],
        "answer": "D"
    },
    {
        "question": "Who developed the theory of relativity?",
        "options": ["A) Isaac Newton", "B) Galileo Galilei", "C) Nikola Tesla", "D) Albert Einstein"],
        "answer": "D"
    },
    {
        "question": "Which country is known as the Land of the Rising Sun?",
        "options": ["A) China", "B) Japan", "C) South Korea", "D) Thailand"],
        "answer": "B"
    },
    {
        "question": "What is the capital of Australia?",
        "options": ["A) Sydney", "B) Melbourne", "C) Canberra", "D) Brisbane"],
        "answer": "C"
    }
]


prize_money = [1000, 2000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000]
lifelines = {"1": "50-50", "2": "Phone a Friend", "3": "Ask the Audience"}
lifelines_available = {"50-50": True, "Phone a Friend": True, "Ask the Audience": True}

print("Welcome to Kaun Banega Crorepati!\n")
prize_index = 0

for i, q in enumerate(questions):
    print(f"Question {i + 1} for Rs. {prize_money[prize_index]}:")
    print(q["question"])
    for option in q["options"]:
        print(option)

    while True:
        print("Available lifelines:")
        for num, lifeline in lifelines.items():
            if lifelines_available[lifeline]:
                print(f"{num}) {lifeline}")
        print()

        use_lifeline_input = input("Do you want to use a lifeline? (yes/no): ").strip().lower()
        if use_lifeline_input == "yes":
            chosen_lifeline_num = input("Which lifeline would you like to use? (1/2/3): ").strip()
            if chosen_lifeline_num in lifelines and lifelines_available[lifelines[chosen_lifeline_num]]:
                chosen_lifeline = lifelines[chosen_lifeline_num]
                if chosen_lifeline == "50-50":
                    options = ["A", "B", "C", "D"]
                    options.remove(q["answer"])
                    wrong_option = random.choice(options)  # Only select one wrong option
                    lifeline_options = [q["answer"], wrong_option]
                elif chosen_lifeline == "Phone a Friend":
                    lifeline_options = [q["answer"]]
                elif chosen_lifeline == "Ask the Audience":
                    lifeline_options = [q["answer"]]  # Only the correct answer is shown

                lifelines_available[chosen_lifeline] = False
                print("Lifeline used! The available options are:")
                for option in lifeline_options:
                    print(next(opt for opt in q["options"] if opt.startswith(option)))
                break
            else:
                print("Invalid lifeline or lifeline already used. Please choose another lifeline or proceed without using one.")
        else:
            break

    answer = input("Your answer (A/B/C/D): ").strip().upper()

    if answer == q["answer"]:
        print("Correct!\n")
        prize_index += 1
        if prize_index == len(prize_money):
            print(f"Congratulations! You've won the maximum prize of Rs. {prize_money[-1]}!")
            break
    else:
        print("Incorrect! Game over.")
        if prize_index > 0:
            print(f"You've won Rs. {prize_money[prize_index - 1]}.")
        else:
            print("You didn't win any money.")
        break
