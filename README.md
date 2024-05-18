# Telegram-bot PSO SALVARE
Telegram-bot that helps send missing persons reports, assemble search teams and search for people. It was developed for [the search and rescue team "Salvar"](https://vk.com/wall-29141239_27643)

> [!NOTE]
> You can find Telegram-bot [here](https://t.me/psosalvarebot)

## 🛠️ Tech Stack
ㅤ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Aiogram](https://img.shields.io/badge/aiogram-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pillow](https://img.shields.io/badge/pillow-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![Yandex Static API](https://img.shields.io/badge/yandex_static_api-FF0000?style=for-the-badge)
![Kandinsky](https://img.shields.io/badge/kandinsky-%23000000.svg?style=for-the-badge)

## 🎯 Quick Start
* Clone the project to your computer from Github using the command:
```
git clone https://github.com/mikhalexandr/TelegramBot-PSO-SALVARE.git
```

* Install all required dependencies from `requirements.txt`:
```
pip install requirements.txt
```

* create `.env` in the project folder and paste these lines there:
```env
PYTHONUNBUFFERED=1;
BOT_TOKEN=your_tg_bot_token;
MAPS_API_KEY=your_yandex_static_api_key;
TUTOR_ID=your_tg_id_for_admin_panel;
KANDINSKY_API_KEY=your_kandinsky_api_key;
KANDINSKY_SECRET_KEY=your_kandinsky_secret_key
```

* Run `main.py`
