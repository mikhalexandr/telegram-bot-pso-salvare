import os
from dotenv import load_dotenv


load_dotenv()

START_MESSAGE = "Вас приветствует ПСО САЛЬВАР. Пожалуйста, введите своё имя:"
TUTOR_ID = int(os.getenv("TUTOR_ID"))
