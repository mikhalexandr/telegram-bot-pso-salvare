from dotenv import load_dotenv
import emoji
import os


load_dotenv()

START_MESSAGE = emoji.emojize("🔎👤 Вас приветствует ПСО САЛЬВАР. Пожалуйста, введите своё имя:")
TUTOR_ID = int(os.getenv("TUTOR_ID"))
