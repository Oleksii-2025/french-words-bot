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

from words import check_answer, format_score, get_hint, get_random_word

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Я помогаю учить французские слова.\n"
        "Напиши /word, чтобы получить слово.\n"
        "Команда /hint даёт подсказку, /score показывает результат."
    )


async def word(update: Update, context: ContextTypes.DEFAULT_TYPE):
    french, russian = get_random_word()
    context.user_data["answer"] = russian
    await update.message.reply_text(f"Переведи слово: {french}")


async def handle_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    correct = context.user_data.get("answer")
    if correct is None:
        await update.message.reply_text("Сначала напиши /word.")
        return
    context.user_data["total"] = context.user_data.get("total", 0) + 1
    if check_answer(update.message.text, correct):
        context.user_data["correct"] = context.user_data.get("correct", 0) + 1
        await update.message.reply_text("Верно!")
    else:
        await update.message.reply_text(f"Неверно. Правильный ответ: {correct}")
    context.user_data.pop("answer")


async def hint(update: Update, context: ContextTypes.DEFAULT_TYPE):
    correct = context.user_data.get("answer")
    if correct is None:
        await update.message.reply_text("Сначала напиши /word.")
        return
    await update.message.reply_text(f"Подсказка: {get_hint(correct)}")


async def score(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = format_score(
        context.user_data.get("correct", 0),
        context.user_data.get("total", 0),
    )
    await update.message.reply_text(text)


def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("word", word))
    app.add_handler(CommandHandler("hint", hint))
    app.add_handler(CommandHandler("score", score))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_answer))
    app.run_polling()


if __name__ == "__main__":
    main()