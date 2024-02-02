import sqlite3

con = sqlite3.connect(r"data\db.sqlite")
cur = con.cursor()


def create_table():
    cur.execute("""
        CREATE TABLE IF NOT EXISTS
        lost (user_id INT, lost_name_id TEXT PRIMARY KEY, born TEXT, regions TEXT, description TEXT, feature TEXT, 
        spec_feature TEXT, clothes TEXT, items TEXT, photo TEXT)
    """)


def push_info(user_id, lost_name_id, born, regions, description, feature, spec_feature, clothes, items, photo):
    req = f"""
        INSERT INTO lost (user_id, lost_name_id, born, regions, description, feature, spec_feature, clothes, items, photo)
        VALUES ({user_id}, {lost_name_id}, {born}, {regions}, {description}, {feature}, {spec_feature}, {clothes}, {items},
        {photo})
        ON CONFLICT (lost_name_id) DO NOTHING
    """
    cur.execute(req)
    con.commit()


def get_info(lost_name_id):
    req = f"""
        SELECT lost_name_id, born, regions, description, feature, spec_feature, clothes, items, photo 
        WHERE lost_name_id = {lost_name_id}
    """
    result = cur.execute(req).fetchall()
    return result

