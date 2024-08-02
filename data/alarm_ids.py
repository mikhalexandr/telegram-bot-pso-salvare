from config import con, cur


class AlarmIds:
    @staticmethod
    def add_alarm_id(user_id):
        req = """
            INSERT INTO alarm_ids (user_id) 
            VALUES (%s)
        """
        cur.execute(req, (user_id,))
        con.commit()

    @staticmethod
    def get_alarm_id():
        req = """
            SELECT user_id 
            FROM alarm_ids
        """
        cur.execute(req)
        return cur.fetchone()
