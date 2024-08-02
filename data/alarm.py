from config import DatabaseConfig


class Alarm:
    @staticmethod
    def add_alarm(user_id, cords, number, name, charge, look, situation, photo=None):
        req = """
                INSERT INTO alarm (user_id, cords, number, name, charge, look, situation, photo_id)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """
        DatabaseConfig.cur.execute(req, (user_id, cords, number, name, charge, look, situation, photo))
        DatabaseConfig.con.commit()

    @staticmethod
    def get_alarm(user_id):
        req = """
            SELECT * 
            FROM alarm 
            WHERE user_id = ?
        """
        return DatabaseConfig.cur.execute(req, (user_id,)).fetchone()

    @staticmethod
    def delete_alarm(user_id):
        req = """
            DELETE 
            FROM alarm
            WHERE user_id = ?
        """
        DatabaseConfig.cur.execute(req, (user_id,))
        DatabaseConfig.con.commit()
