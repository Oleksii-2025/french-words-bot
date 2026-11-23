import pytest
from words import check_answer, format_score, get_hint, get_random_word
from words import check_answer, get_random_word, format_score
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

def test_format_score_no_answers():
    assert format_score(0, 0) == "Ты ещё не отвечал на слова."


def test_format_score_percent():
    assert format_score(3, 4) == "Правильных ответов: 3 из 4 (75%)"


@pytest.mark.parametrize(
    "user_answer, correct_answer, expected",
    [
        ("chat", "chat", True),
        ("CHAT", "chat", True),
        ("chien", "chat", False),
        ("", "chat", False),
        ("  chat  ", "chat", True),
        ("Кот", "кот", True),
        ("собака", "кот", False),
    ],
)
def test_check_answer_cases(user_answer, correct_answer, expected):
    assert check_answer(user_answer, correct_answer) is expected


def test_get_hint_shows_first_letter():
    assert get_hint("кот") == "к__"


def test_get_hint_one_letter():
    assert get_hint("я") == "я"


def test_get_hint_empty_word():
    assert get_hint("") == ""

