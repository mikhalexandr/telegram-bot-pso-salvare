import psycopg2
import os


class DatabaseConfig:
    con = psycopg2.connect(os.getenv("DATABASE_URL"))
    cur = con.cursor()
