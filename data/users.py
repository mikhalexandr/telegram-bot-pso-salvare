from config import con, cur


class Users:
    @staticmethod
    def add_user(user_id, name):
        req1 = """
            SELECT * 
            FROM users 
            WHERE user_id = %s
        """
        req2 = """
            UPDATE users
            SET name = %s 
            WHERE user_id = %s
        """
        req3 = """
            INSERT INTO users (user_id, name) 
            VALUES (%s, %s)
        """
        if cur.execute(req1, (user_id,)):
            cur.execute(req2, (name, user_id))
        else:
            cur.execute(req3, (user_id, name))
        con.commit()

    @staticmethod
    def get_user(user_id):
        req = """
            SELECT name 
            FROM users 
            WHERE user_id = %s
        """
        cur.execute(req, (user_id,))
        return cur.fetchone()[0]

    @staticmethod
    def update_user_name(user_id, name):
        req = """
            UPDATE users 
            SET name = %s
            WHERE user_id = %s
        """
        cur.execute(req, (name, user_id))
        con.commit()

    @staticmethod
    def check_user_id(user_id):
        req = """
            SELECT EXISTS(
                SELECT 1
                FROM users
                WHERE user_id = %s
            )
        """
        cur.execute(req, (user_id,))
        result = cur.fetchone()
        return result[0] if result else None

    @staticmethod
    def get_user_info(user_id):
        req = """
            SELECT lost_count, team_count, alarm_count 
            FROM users
            WHERE user_id = %s
        """
        cur.execute(req, (user_id,))
        result = list(cur.fetchone())
        return result

    @staticmethod
    def update_lost_count(user_id):
        req = """
            UPDATE users 
            SET lost_count = lost_count + 1
            WHERE user_id = %s
        """
        cur.execute(req, (user_id,))
        con.commit()

    @staticmethod
    def update_team_count(user_id):
        req = """
            UPDATE users
            SET team_count = team_count + 1
            WHERE user_id = %s
        """
        cur.execute(req, (user_id,))
        con.commit()

    @staticmethod
    def update_alarm_count(user_id):
        req = """
            UPDATE users 
            SET alarm_count = alarm_count + 1
            WHERE user_id = %s
        """
        cur.execute(req, (user_id,))
        con.commit()

    @staticmethod
    def get_users():
        req = """
            SELECT user_id 
            FROM users
        """
        cur.execute(req)
        result = cur.fetchall()
        return [i[0] for i in result]
