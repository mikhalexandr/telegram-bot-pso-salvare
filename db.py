import sqlite3

con = sqlite3.connect(r"data\db.sqlite")
cur = con.cursor()


def create_table():
    cur.execute("""
        CREATE TABLE IF NOT EXISTS
        lost (user_id TEXT, lost_name_id TEXT, born TEXT, regions TEXT, description TEXT, feature TEXT, 
        spec_feature TEXT, clothes TEXT, items TEXT, photo TEXT)
    """)
    cur.execute("""
            CREATE TABLE IF NOT EXISTS
            checking (user_id TEXT, lost_name_id TEXT, born TEXT, regions TEXT, description TEXT, feature TEXT, 
            spec_feature TEXT, clothes TEXT, items TEXT, photo TEXT)
        """)
    cur.execute("""
                CREATE TABLE IF NOT EXISTS
                people (user_id TEXT, name TEXT)
            """)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS
    teams (id INTEGER PRIMARY KEY AUTOINCREMENT, loser TEXT, human TEXT)
    """)


def push_lost_info(user_id, lost_name_id, born, regions, description, feature, spec_feature, clothes, items, photo):
    req = """
        INSERT INTO lost (user_id, lost_name_id, born, regions, description, feature, spec_feature, clothes, items, photo)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    cur.execute(req, (user_id, lost_name_id, born, regions, description, feature, spec_feature, clothes, items, photo))
    con.commit()


def push_checking_info(user_id, lost_name_id, born, regions, description, feature, spec_feature, clothes, items, photo):
    req = """
        INSERT INTO checking (user_id, lost_name_id, born, regions, description, feature, spec_feature, clothes, items, photo)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    cur.execute(req, (user_id, lost_name_id, born, regions, description, feature, spec_feature, clothes, items, photo))
    con.commit()


def get_lost_info(lost_name_id):
    req = """
        SELECT user_id, lost_name_id, born, regions, description, feature, spec_feature, clothes, items, photo 
        FROM lost
        WHERE lost_name_id = ?
    """
    result = cur.execute(req, (lost_name_id,)).fetchone()
    return result


def get_all_lost_info():
    req = """
        SELECT user_id, lost_name_id, born, regions, description, feature, spec_feature, clothes, items, photo 
        FROM lost
    """
    result = cur.execute(req).fetchall()
    return result


def get_checking_info():
    req = """
        SELECT user_id, lost_name_id, born, regions, description, feature, spec_feature, clothes, items, photo 
        FROM checking
    """
    result = cur.execute(req,).fetchone()
    return result


def delete_checking(lost_name_id):
    req = """
    DELETE FROM checking
    WHERE lost_name_id = ?"""
    cur.execute(req, (lost_name_id,))
    con.commit()


def add_human(user_id, name):
    req1 = """SELECT * FROM people WHERE user_id = ?"""
    req2 = """UPDATE people
    SET name = ? WHERE user_id = ?"""
    req3 = """INSERT INTO people (user_id, name) VALUES (?, ?)"""
    if cur.execute(req1, (user_id,)).fetchone():
        cur.execute(req2, (name, user_id))
    else:
        cur.execute(req3, (user_id, name))
    con.commit()


def get_all():
    req = """SELECT user_id FROM people"""
    result = cur.execute(req).fetchall()
    return [i[0] for i in result]


def create_team(loser):
    req = """INSERT INTO teams(loser, human) VALUES (?, NULL)"""
    cur.execute(req, (loser,))
    con.commit()


def add_team_member(member, loser):
    req1 = """SELECT * FROM teams WHERE human = NULL"""
    req2 = """INSERT INTO teams(loser, human) VALUES (?, ?)"""
    if cur.execute(req1).fetchone() is None:
        cur.execute("""UPDATE teams SET human = ?""", (member,))
    else:
        cur.execute(req2, (loser, member))
    con.commit()
