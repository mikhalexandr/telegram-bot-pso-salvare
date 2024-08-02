from aiogram.types import BufferedInputFile
import requests

from config import StaticMapsConfig


def create_map(coords):
    req = "https://static-maps.yandex.ru/v1?"
    params = {
        "apikey": StaticMapsConfig.MAPS_API_KEY,
        "pt": coords + ",pm2rdm1",
        "z": "12"
    }
    response = requests.get(req, params=params)
    if not response:
        return False
    return BufferedInputFile(response.content, filename=f"map{coords}.png")
