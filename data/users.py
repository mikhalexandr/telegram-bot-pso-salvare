from config import con, cur


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
        if cur.execute(req1, (user_id,)).fetchone():
            cur.execute(req2, (name, user_id))
        else:
            cur.execute(req3, (user_id, name))
        con.commit()

    @staticmethod
    def get_user(user_id):
        req = """
            SELECT name 
            FROM people 
            WHERE user_id = ?
        """
        return con.execute(req, (str(user_id),)).fetchone()[0]

    @staticmethod
    def update_user_name(user_id, name):
        req = """
            UPDATE people 
            SET name = ?
            WHERE user_id = ?
        """
        cur.execute(req, (name, user_id))
        con.commit()

    @staticmethod
    def check_user_id(user_id):
        req = """
            SELECT EXISTS(
                SELECT 1 
                FROM users 
                WHERE user_id = ?
            ) as id_exists
        """
        return cur.execute(req, (str(user_id),)).fetchone()[0]

    @staticmethod
    def get_user_info(user_id):
        req = """
            SELECT lost_count, team_count, alarm_count 
            FROM users
            WHERE user_id = ?
        """
        res = list(cur.execute(req, (user_id,)).fetchone())
        return res

    @staticmethod
    def update_lost_count(user_id):
        req = """
            UPDATE users 
            SET lost_count = lost_count + 1
            WHERE user_id = ?
        """
        cur.execute(req, (user_id,))
        con.commit()

    @staticmethod
    def update_team_count(user_id):
        req = """
            UPDATE users
            SET team_count = team_count + 1
            WHERE user_id = ?
        """
        cur.execute(req, (user_id,))
        con.commit()

    @staticmethod
    def update_alarm_count(user_id):
        req = """
            UPDATE users 
            SET alarm_count = alarm_count + 1
            WHERE user_id = ?
        """
        cur.execute(req, (user_id,))
        con.commit()

    @staticmethod
    def get_users():
        req = """
            SELECT user_id 
            FROM users
        """
        result = cur.execute(req).fetchall()
        return [i[0] for i in result]
