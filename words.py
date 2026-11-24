import random

WORDS = {
    "chat": "кот",
    "chien": "собака",
    "maison": "дом",
    "pain": "хлеб",
    "eau": "вода",
    "livre": "книга",
    "merci": "спасибо",
    "bonjour": "здравствуйте",
    "fromage": "сыр",
    "pomme": "яблоко",
    "chambre": "комната",
    "ami": "друг",
    "soleil": "солнце",
    "lune": "луна",
    "table": "стол",
    "fenetre": "окно",
}


def get_random_word(words=WORDS, reverse=False):
    french = random.choice(list(words))
    russian = words[french]
    if reverse:
        return russian, french
    return french, russian

def check_answer(user_answer, correct_answer):
    return user_answer.strip().lower() == correct_answer.strip().lower()

def format_score(correct, total):
    if total == 0:
        return "Ты ещё не отвечал на слова."
    percent = round(correct / total * 100)
    return f"Правильных ответов: {correct} из {total} ({percent}%)"


def get_hint(word):
    if not word:
        return ""
    return word[0] + "_" * (len(word) - 1)