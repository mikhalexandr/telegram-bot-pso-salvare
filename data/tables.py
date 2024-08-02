from config import con, cur


class Tables:
    @staticmethod
    def create_tables():
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
            users (user_id TEXT, name TEXT, lost_count INT DEFAULT 0, team_count INT DEFAULT 0, 
            alarm_count INT DEFAULT 0)
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS
            teams (id INTEGER PRIMARY KEY AUTOINCREMENT, lost TEXT, user_id TEXT UNIQUE)
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS
            alarm (user_id TEXT, cords TEXT, number TEXT, name TEXT, charge TEXT, look TEXT, situation TEXT, 
            photo_id TEXT)
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS
            alarm_ids(user_id TEXT)
        """)
        con.commit()
