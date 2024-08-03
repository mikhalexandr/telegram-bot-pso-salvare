from config import con, cur


class Tables:
    @staticmethod
    def create_tables():
        cur.execute("""
            CREATE TABLE IF NOT EXISTS
            lost (user_id BIGINT, lost_name_id TEXT, born TEXT, regions TEXT, description TEXT, feature TEXT, 
            spec_feature TEXT, clothes TEXT, items TEXT, photo TEXT)
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS
            checking (user_id BIGINT, lost_name_id TEXT, born TEXT, regions TEXT, description TEXT, feature TEXT, 
            spec_feature TEXT, clothes TEXT, items TEXT, photo TEXT)
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS
            users (user_id BIGINT, name TEXT, lost_count INT DEFAULT 0, team_count INT DEFAULT 0, 
            alarm_count INT DEFAULT 0)
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS
            teams (id SERIAL PRIMARY KEY , lost TEXT, user_id BIGINT UNIQUE)
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS
            alarm (user_id BIGINT, cords TEXT, number TEXT, name TEXT, charge TEXT, look TEXT, situation TEXT, 
            photo_id TEXT)
        """)
        con.commit()
