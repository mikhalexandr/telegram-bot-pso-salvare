from config import DatabaseConfig


class AlarmIds:
    @staticmethod
    def add_alarm_id(user_id):
        req = """
            INSERT INTO alarm_ids (user_id) 
            VALUES (?)
        """
        DatabaseConfig.cur.execute(req, (user_id,))
        DatabaseConfig.con.commit()

    @staticmethod
    def get_alarm_id():
        req = """
            SELECT user_id 
            FROM alarm_ids
        """
        return DatabaseConfig.cur.execute(req).fetchone()
