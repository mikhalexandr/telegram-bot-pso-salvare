from dotenv import load_dotenv
import emoji
import os


load_dotenv()


class TelegramConfig:
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    TUTOR_ID = int(os.getenv("TUTOR_ID"))


class TelegramTexts:
    START_MESSAGE = emoji.emojize("🔎👤 Вас приветствует ПСО САЛЬВАР. Пожалуйста, введите своё имя:")
