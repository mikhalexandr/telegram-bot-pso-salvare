# Telegram-bot PSO SALVARE
Telegram-bot for [the search and rescue team "Salvar"](https://vk.com/wall-29141239_27643) that helps send missing persons reports, assemble search teams and search for people. There is also an admin panel, which is implemented using a third-party program Adminer, allowing organizers to control the data and processes occurring inside the bot

> [!NOTE]
> You can find Telegram-bot [here](https://t.me/psosalvarebot)

## 📺 Preview
![](https://github.com/mikhalexandr/telegram-bot-pso-salvare/blob/main/assets/design/greeting.png)

## 🛠️ Tech Stack
ㅤ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Aiogram](https://img.shields.io/badge/aiogram-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pillow](https://img.shields.io/badge/pillow-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Yandex Static API](https://img.shields.io/badge/yandex_static_api-FF0000?style=for-the-badge)
![Kandinsky](https://img.shields.io/badge/kandinsky-%23000000.svg?style=for-the-badge)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)

## 🎯 Quick Start
* Clone the project to your computer from Github using the command:
```
git clone https://github.com/mikhalexandr/TelegramBot-PSO-SALVARE.git
```

* create `.env.bot` in the `config` directory and paste these lines there:
```env
BOT_TOKEN=your_tg_bot_token
TUTOR_ID=your_tg_id_for_admin_panel
MAPS_API_KEY=your_yandex_static_api_key
KANDINSKY_API_KEY=your_kandinsky_api_key
KANDINSKY_SECRET_KEY=your_kandinsky_secret_key
```

* create `.env.database` in the `config` directory and paste these lines there:
```env
POSTGRES_DB=your_postgres_db_name
POSTGRES_USER=your_postgres_user_name
POSTGRES_PASSWORD=your_postgres_password
```

* Run this command in terminal:
```
docker-compose up
```

## 🏆 Awards
  -
