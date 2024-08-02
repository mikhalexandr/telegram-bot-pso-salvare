from config import DatabaseConfig


class Teams:
    @staticmethod
    def create_team(lost):
        req = """
            INSERT INTO teams(lost, user_id) 
            VALUES (?, NULL)
        """
        DatabaseConfig.cur.execute(req, (lost,))
        DatabaseConfig.con.commit()

    @staticmethod
    def is_in_team(user_id):
        req = """
            SELECT * 
            FROM teams 
            WHERE user_id = ?
        """
        res = DatabaseConfig.cur.execute(req, (user_id,)).fetchone()
        return res

    @staticmethod
    def delete_team(lost_id):
        req = """
            DELETE 
            FROM teams 
            WHERE lost = ?
        """
        DatabaseConfig.cur.execute(req, (lost_id,))
        DatabaseConfig.con.commit()

    @staticmethod
    def add_teammate(mate, lost):
        req2 = """
            INSERT INTO teams(lost, user_id) 
            VALUES (?, ?) 
            ON CONFLICT (user_id) DO NOTHING
        """
        DatabaseConfig.cur.execute(req2, (lost, mate))
        DatabaseConfig.con.commit()

    @staticmethod
    def delete_teammate(user_id):
        req = """
            DELETE 
            FROM teams 
            WHERE user_id = ?
        """
        DatabaseConfig.cur.execute(req, (user_id,))
        DatabaseConfig.con.commit()

    @staticmethod
    def get_teams():
        req = """
            SELECT lost 
            FROM teams
        """
        result = DatabaseConfig.cur.execute(req).fetchall()
        return [i[0] for i in result]

    @staticmethod
    def get_teammates(user_id):
        req = """
            SELECT user_id 
            FROM teams 
            WHERE lost = (
                SELECT lost 
                FROM teams 
                WHERE user_id = ?
            ) AND user_id != ?
        """
        return DatabaseConfig.cur.execute(req, (user_id, user_id)).fetchall()

    @staticmethod
    def get_teammates_by_lost(lost):
        req = """
            SELECT user_id 
            FROM teams 
            WHERE lost = ?
        """
        return DatabaseConfig.cur.execute(req, (lost,)).fetchall()
