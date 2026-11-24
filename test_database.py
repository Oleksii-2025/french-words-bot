import pytest

from database import add_result, get_score, init_db


@pytest.fixture
def db_path(tmp_path):
    path = str(tmp_path / "test_scores.db")
    init_db(path)
    return path


def test_new_user_has_zero_score(db_path):
    assert get_score(1, db_path) == (0, 0)


def test_add_correct_result(db_path):
    add_result(1, True, db_path)
    assert get_score(1, db_path) == (1, 1)


def test_add_wrong_result(db_path):
    add_result(1, False, db_path)
    assert get_score(1, db_path) == (0, 1)


def test_scores_are_per_user(db_path):
    add_result(1, True, db_path)
    add_result(2, False, db_path)
    assert get_score(1, db_path) == (1, 1)
    assert get_score(2, db_path) == (0, 1)


def test_score_accumulates(db_path):
    add_result(1, True, db_path)
    add_result(1, False, db_path)
    add_result(1, True, db_path)
    assert get_score(1, db_path) == (2, 3)