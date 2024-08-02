from config import con, cur


class Teams:
    @staticmethod
    def create_team(lost):
        req = """
            INSERT INTO teams(lost, user_id) 
            VALUES (%s, NULL)
        """
        cur.execute(req, (lost,))
        con.commit()

    @staticmethod
    def is_in_team(user_id):
        req = """
            SELECT * 
            FROM teams 
            WHERE user_id = %s
        """
        cur.execute(req, (user_id,))
        return cur.fetchone()

    @staticmethod
    def delete_team(lost_id):
        req = """
            DELETE 
            FROM teams 
            WHERE lost = %s
        """
        cur.execute(req, (lost_id,))
        con.commit()

    @staticmethod
    def add_teammate(mate, lost):
        req2 = """
            INSERT INTO teams(lost, user_id) 
            VALUES (%s, %s) 
            ON CONFLICT (user_id) DO NOTHING
        """
        cur.execute(req2, (lost, mate))
        con.commit()

    @staticmethod
    def delete_teammate(user_id):
        req = """
            DELETE 
            FROM teams 
            WHERE user_id = %s
        """
        cur.execute(req, (user_id,))
        con.commit()

    @staticmethod
    def get_teams():
        req = """
            SELECT lost 
            FROM teams
        """
        cur.execute(req)
        result = cur.fetchall()
        return [i[0] for i in result]

    @staticmethod
    def get_teammates(user_id):
        req = """
            SELECT user_id 
            FROM teams 
            WHERE lost = (
                SELECT lost 
                FROM teams 
                WHERE user_id = %s
            ) AND user_id != %s
        """
        cur.execute(req, (user_id, user_id))
        return cur.fetchall()

    @staticmethod
    def get_teammates_by_lost(lost):
        req = """
            SELECT user_id 
            FROM teams 
            WHERE lost = %s
        """
        cur.execute(req, (lost,))
        return cur.fetchall()
