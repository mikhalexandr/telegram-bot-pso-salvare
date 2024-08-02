from config import con, cur


class AlarmIds:
    @staticmethod
    def add_alarm_id(user_id):
        req = """
            INSERT INTO alarm_ids (user_id) 
            VALUES (?)
        """
        cur.execute(req, (user_id,))
        con.commit()

    @staticmethod
    def get_alarm_id():
        req = """
            SELECT user_id 
            FROM alarm_ids
        """
        return cur.execute(req).fetchone()
