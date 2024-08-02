import os
import psycopg2


con = psycopg2.connect(os.getenv("DATABASE_URL"))
cur = con.cursor()
