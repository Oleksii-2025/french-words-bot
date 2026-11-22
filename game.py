from words import get_random_word, check_answer


def play_round():
    french, russian = get_random_word()
    answer = input(f"Переведи слово «{french}»: ")
    if check_answer(answer, russian):
        print("Верно!")
        return True
    print(f"Неверно. Правильный ответ: {russian}")
    return False


def main():
    rounds = 5
    score = 0
    for _ in range(rounds):
        if play_round():
            score += 1
    print(f"Результат: {score} из {rounds}")


if __name__ == "__main__":
    main()