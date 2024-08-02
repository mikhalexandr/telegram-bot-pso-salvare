from config import con, cur


class Alarm:
    @staticmethod
    def add_alarm(user_id, cords, number, name, charge, look, situation, photo=None):
        req = """
                INSERT INTO alarm (user_id, cords, number, name, charge, look, situation, photo_id)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        cur.execute(req, (user_id, cords, number, name, charge, look, situation, photo))
        con.commit()

    @staticmethod
    def get_alarm(user_id):
        req = """
            SELECT * 
            FROM alarm 
            WHERE user_id = %s
        """
        cur.execute(req, (user_id,))
        return cur.fetchone()

    @staticmethod
    def delete_alarm(user_id):
        req = """
            DELETE 
            FROM alarm
            WHERE user_id = %s
        """
        cur.execute(req, (user_id,))
        con.commit()
