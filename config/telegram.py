from dataclasses import dataclass
import os
from dotenv import load_dotenv
import emoji


load_dotenv()


@dataclass
class TelegramConfig:
    BOT_TOKEN: str = os.getenv("BOT_TOKEN")
    TUTOR_ID: int = os.getenv("TUTOR_ID")


@dataclass
class TelegramTexts:
    START_MESSAGE: str = emoji.emojize("🔎👤 Вас приветствует ПСО САЛЬВАР. Пожалуйста, введите своё имя:")
