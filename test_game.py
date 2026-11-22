import game


def test_play_round_correct(monkeypatch):
    monkeypatch.setattr(game, "get_random_word", lambda: ("chat", "кот"))
    monkeypatch.setattr("builtins.input", lambda _: "кот")
    assert game.play_round() is True


def test_play_round_wrong(monkeypatch):
    monkeypatch.setattr(game, "get_random_word", lambda: ("chat", "кот"))
    monkeypatch.setattr("builtins.input", lambda _: "собака")
    assert game.play_round() is False