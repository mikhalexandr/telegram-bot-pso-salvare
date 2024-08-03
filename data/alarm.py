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
    def get_alarm(user_geo, user_name):
        req = """
            SELECT * 
            FROM alarm 
            WHERE cords = %s AND name = %s
        """
        cur.execute(req, (user_geo, user_name,))
        return cur.fetchone()

    @staticmethod
    def delete_alarm(user_geo, user_name):
        req = """
            DELETE 
            FROM alarm
            WHERE cords = %s AND name = %s
        """
        cur.execute(req, (user_geo, user_name,))
        con.commit()
