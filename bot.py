import os

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

from database import add_result, get_score, init_db, reset_score
from words import check_answer, format_score, get_hint, get_random_word

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

# Only new messages: edited messages have update.message set to None,
# and an edited answer should not be counted a second time.
NEW_MESSAGES = filters.UpdateType.MESSAGE


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Я помогаю учить французские слова.\n"
        "/word даёт французское слово, его нужно перевести на русский.\n"
        "/back даёт русское слово, его нужно перевести на французский.\n"
        "/hint даёт подсказку, /score показывает результат.\n"
        "/reset обнуляет твой счёт."
    )


async def word(update: Update, context: ContextTypes.DEFAULT_TYPE):
    french, russian = get_random_word()
    context.user_data["answer"] = russian
    await update.message.reply_text(f"Переведи слово: {french}")


async def back(update: Update, context: ContextTypes.DEFAULT_TYPE):
    russian, french = get_random_word(reverse=True)
    context.user_data["answer"] = french
    await update.message.reply_text(f"Переведи на французский: {russian}")


async def handle_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    correct = context.user_data.get("answer")
    if correct is None:
        await update.message.reply_text("Сначала напиши /word или /back.")
        return
    is_correct = check_answer(update.message.text, correct)
    add_result(update.effective_user.id, is_correct)
    if is_correct:
        await update.message.reply_text("Верно!")
    else:
        await update.message.reply_text(f"Неверно. Правильный ответ: {correct}")
    context.user_data.pop("answer")


async def hint(update: Update, context: ContextTypes.DEFAULT_TYPE):
    correct = context.user_data.get("answer")
    if correct is None:
        await update.message.reply_text("Сначала напиши /word или /back.")
        return
    await update.message.reply_text(f"Подсказка: {get_hint(correct)}")


async def score(update: Update, context: ContextTypes.DEFAULT_TYPE):
    correct, total = get_score(update.effective_user.id)
    await update.message.reply_text(format_score(correct, total))


async def reset(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reset_score(update.effective_user.id)
    context.user_data.pop("answer", None)
    await update.message.reply_text(
        "Счёт обнулён. Напиши /word или /back, чтобы начать заново."
    )


def main():
    if not TOKEN:
        raise SystemExit(
            "BOT_TOKEN is not set.\n"
            "Create a file named .env next to bot.py with the line:\n"
            "BOT_TOKEN=your_token_here\n"
            "Get the token from @BotFather in Telegram."
        )
    init_db()
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start, filters=NEW_MESSAGES))
    app.add_handler(CommandHandler("word", word, filters=NEW_MESSAGES))
    app.add_handler(CommandHandler("back", back, filters=NEW_MESSAGES))
    app.add_handler(CommandHandler("hint", hint, filters=NEW_MESSAGES))
    app.add_handler(CommandHandler("score", score, filters=NEW_MESSAGES))
    app.add_handler(CommandHandler("reset", reset, filters=NEW_MESSAGES))
    app.add_handler(
        MessageHandler(
            NEW_MESSAGES & filters.TEXT & ~filters.COMMAND, handle_answer
        )
    )
    app.run_polling()


if __name__ == "__main__":
    main()