# Telegram-bot PSO SALVARE

![License](https://img.shields.io/github/license/dmhd6219/sdamgia-solver)
![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)
![Version](https://img.shields.io/badge/version-1.0-green)

Telegram bot for [the search and rescue team "Salvar"](https://vk.com/wall-29141239_27643), which consists of:
  * a user part, where people can send messages about missing persons, join search groups, send emergency requests for help, and receive newsletters about various incidents
  * an admin panel, where the organizer can moderate incoming bot-generated questionnaires about missing persons, requests for help and commands  

There is also a panel for moderating the database, implemented using a third-party program [Adminer](https://www.adminer.org/)
    
> [!NOTE]
> You can find Telegram-bot [here](https://t.me/psosalvarebot)

## 📺 Preview
![](https://github.com/mikhalexandr/telegram-bot-pso-salvare/blob/main/assets/design/preview.png)

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
git clone https://github.com/mikhalexandr/telegram-bot-pso-salvare.git
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

* Run this command in terminal (don't forget to run [Docker Desktop](https://www.docker.com/products/docker-desktop/) before this):
```
docker-compose up
```

## 🏆 Awards
  * [Absolute winner in the regional track of the All-Russian competition of scientific and technological projects "Big Challenges. Smolensk-2024" in the nomination "Smart City and Security"](https://vk.com/wall-189705382_4434)
  * [1 degree diploma in the city School Science Week "First Steps in Science"](https://vk.com/wall-189705382_4415)
  * [Prize-winning place in the hackathon "Game of Detective"](https://vk.com/itcube.smolensk?z=photo-189705382_457267230%2Fwall-189705382_4142)
