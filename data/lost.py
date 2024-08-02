from config import con, cur


class Lost:
    @staticmethod
    def add_lost(user_id, lost_name_id, born, regions, description, feature, spec_feature, clothes, items, photo):
        req = """
            INSERT 
            INTO lost (user_id, lost_name_id, born, regions, description, feature, spec_feature, clothes, items, photo)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        cur.execute(req, (user_id, lost_name_id,
                          born, regions, description, feature, spec_feature, clothes, items, photo))
        con.commit()

    @staticmethod
    def get_lost(lost_name_id):
        req = """
            SELECT user_id, lost_name_id, born, regions, description, feature, spec_feature, clothes, items, photo 
            FROM lost
            WHERE lost_name_id = ?
        """
        result = cur.execute(req, (lost_name_id,)).fetchone()
        return result

    @staticmethod
    def delete_lost(lost_id):
        req = """
            DELETE 
            FROM lost
            WHERE lost_name_id = ?
        """
        cur.execute(req, (lost_id,))
        con.commit()

    @staticmethod
    def get_all_lost():
        req = """
            SELECT user_id, lost_name_id, born, regions, description, feature, spec_feature, clothes, items, photo 
            FROM lost
        """
        result = cur.execute(req).fetchall()
        return result
