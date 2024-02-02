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
    result = cur.execute(req, (lost_name_id,)).fetchall()
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
