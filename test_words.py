from words import check_answer


def test_correct_answer():
    assert check_answer("chat", "chat") is True


def test_ignores_case_and_spaces():
    assert check_answer("  Chat ", "chat") is True


def test_wrong_answer():
    assert check_answer("chien", "chat") is False