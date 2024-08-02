from config import con, cur


class Lost:
    @staticmethod
    def add_lost(user_id, lost_name_id, born, regions, description, feature, spec_feature, clothes, items, photo):
        req = """
            INSERT 
            INTO lost (user_id, lost_name_id, born, regions, description, feature, spec_feature, clothes, items, photo)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cur.execute(req, (user_id, lost_name_id,
                          born, regions, description, feature, spec_feature, clothes, items, photo))
        con.commit()

    @staticmethod
    def get_lost(lost_name_id):
        req = """
            SELECT user_id, lost_name_id, born, regions, description, feature, spec_feature, clothes, items, photo 
            FROM lost
            WHERE lost_name_id = %s
        """
        cur.execute(req, (lost_name_id,))
        return cur.fetchone()

    @staticmethod
    def delete_lost(lost_id):
        req = """
            DELETE 
            FROM lost
            WHERE lost_name_id = %s
        """
        cur.execute(req, (lost_id,))
        con.commit()

    @staticmethod
    def get_all_lost():
        req = """
            SELECT user_id, lost_name_id, born, regions, description, feature, spec_feature, clothes, items, photo 
            FROM lost
        """
        cur.execute(req)
        return cur.fetchall()
