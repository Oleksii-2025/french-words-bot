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
}


def get_random_word(words=WORDS):
    french = random.choice(list(words))
    return french, words[french]

def check_answer(user_answer, correct_answer):
    return user_answer.strip().lower() == correct_answer.strip().lower()