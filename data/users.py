from config import DatabaseConfig


class Users:
    @staticmethod
    def add_user(user_id, name):
        req1 = """
            SELECT * 
            FROM people 
            WHERE user_id = ?
        """
        req2 = """
            UPDATE people
            SET name = ? 
            WHERE user_id = ?
        """
        req3 = """
            INSERT INTO people (user_id, name) 
            VALUES (?, ?)
        """
        if DatabaseConfig.cur.execute(req1, (user_id,)).fetchone():
            DatabaseConfig.cur.execute(req2, (name, user_id))
        else:
            DatabaseConfig.cur.execute(req3, (user_id, name))
        DatabaseConfig.con.commit()

    @staticmethod
    def get_user(user_id):
        req = """
            SELECT name 
            FROM people 
            WHERE user_id = ?
        """
        return DatabaseConfig.con.execute(req, (str(user_id),)).fetchone()[0]

    @staticmethod
    def update_user_name(user_id, name):
        req = """
            UPDATE people 
            SET name = ?
            WHERE user_id = ?
        """
        DatabaseConfig.cur.execute(req, (name, user_id))
        DatabaseConfig.con.commit()

    @staticmethod
    def check_user_id(user_id):
        req = """
            SELECT EXISTS(
                SELECT 1 
                FROM users 
                WHERE user_id = ?
            ) as id_exists
        """
        return DatabaseConfig.cur.execute(req, (str(user_id),)).fetchone()[0]

    @staticmethod
    def get_user_info(user_id):
        req = """
            SELECT lost_count, team_count, alarm_count 
            FROM users
            WHERE user_id = ?
        """
        res = list(DatabaseConfig.cur.execute(req, (user_id,)).fetchone())
        return res

    @staticmethod
    def update_lost_count(user_id):
        req = """
            UPDATE users 
            SET lost_count = lost_count + 1
            WHERE user_id = ?
        """
        DatabaseConfig.cur.execute(req, (user_id,))
        DatabaseConfig.con.commit()

    @staticmethod
    def update_team_count(user_id):
        req = """
            UPDATE users
            SET team_count = team_count + 1
            WHERE user_id = ?
        """
        DatabaseConfig.cur.execute(req, (user_id,))
        DatabaseConfig.con.commit()

    @staticmethod
    def update_alarm_count(user_id):
        req = """
            UPDATE users 
            SET alarm_count = alarm_count + 1
            WHERE user_id = ?
        """
        DatabaseConfig.cur.execute(req, (user_id,))
        DatabaseConfig.con.commit()

    @staticmethod
    def get_users():
        req = """
            SELECT user_id 
            FROM users
        """
        result = DatabaseConfig.cur.execute(req).fetchall()
        return [i[0] for i in result]
