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

from words import check_answer, get_random_word

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Я помогаю учить французские слова.\n"
        "Напиши /word, чтобы получить слово."
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
    if check_answer(update.message.text, correct):
        await update.message.reply_text("Верно!")
    else:
        await update.message.reply_text(f"Неверно. Правильный ответ: {correct}")
    context.user_data.pop("answer")


def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("word", word))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_answer))
    app.run_polling()


if __name__ == "__main__":
    main()