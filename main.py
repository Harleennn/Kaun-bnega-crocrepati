from question import questions



def display_question(question):
    print(question["question"])
    for option in question["options"]:
        print(option)
    answer = input("Enter your answer (A, B, C, or D): ")
    return answer.upper() == question["answer"]


def play_game():
    total_prize = 0
    prize_levels = [1000, 5000, 10000, 50000, 100000, 500000, 1000000]  # Prize levels for each question

    for i, question in enumerate(questions):
        print(f"\nQuestion {i + 1} for Rs. {prize_levels[i]}")
        if display_question(question):
            print("Correct!\n")
            total_prize = prize_levels[i]
        else:
            print("Wrong answer!")
            break

    print(f"Congratulations! You have won Rs. {total_prize}")


if __name__ == "__main__":
    play_game()



