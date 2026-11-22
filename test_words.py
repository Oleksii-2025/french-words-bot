from words import check_answer, get_random_word

from words import check_answer

def test_correct_answer():
    assert check_answer("chat", "chat") is True


def test_ignores_case_and_spaces():
    assert check_answer("  Chat ", "chat") is True


def test_wrong_answer():
    assert check_answer("chien", "chat") is False

def test_random_word_is_from_dictionary():
    words = {"chat": "кот", "chien": "собака"}
    french, russian = get_random_word(words)
    assert french in words
    assert words[french] == russian


def test_random_word_with_single_entry():
    assert get_random_word({"eau": "вода"}) == ("eau", "вода")

def test_russian_answer():
    assert check_answer("Кот ", "кот") is True

