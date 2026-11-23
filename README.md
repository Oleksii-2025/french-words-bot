# french-words-bot
![Bot screenshot](screenshot.png)
A Telegram bot for learning French words, built with Python and tested with pytest.

The bot sends a French word, you reply with the Russian translation, and it tells you if you are right. It keeps a score for each user.

## Features

- `/start` shows a greeting and instructions
- `/word` sends a random French word
- Reply with the translation to get "correct" or "wrong" feedback
- `/score` shows how many answers were correct
- Answers are case-insensitive and ignore extra spaces

## Project structure

- `words.py` is the word list and the main logic (checking answers, random word, score text)
- `bot.py` is the Telegram bot
- `game.py` is a console version of the quiz
- `test_words.py` and `test_game.py` are the pytest tests

## How to run

1. Install dependencies:

```
pip install python-telegram-bot python-dotenv pytest
```

2. Create a bot with @BotFather in Telegram and copy its token.
3. Create a file named `.env` next to `bot.py`:

```
BOT_TOKEN=your_token_here
```

4. Start the bot:

```
python bot.py
```

## Run the tests

```
pytest
```

## What I practiced

Python functions and dictionaries, writing unit tests with pytest (including `monkeypatch`), working with Git and GitHub, keeping secrets out of the repository with `.env` and `.gitignore`.