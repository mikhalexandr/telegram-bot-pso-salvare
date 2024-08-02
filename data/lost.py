from config import DatabaseConfig


class Lost:
    @staticmethod
    def add_lost(user_id, lost_name_id, born, regions, description, feature, spec_feature, clothes, items, photo):
        req = """
            INSERT 
            INTO lost (user_id, lost_name_id, born, regions, description, feature, spec_feature, clothes, items, photo)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        DatabaseConfig.cur.execute(req, (user_id, lost_name_id,
                                         born, regions, description, feature, spec_feature, clothes, items, photo))
        DatabaseConfig.con.commit()

    @staticmethod
    def get_lost(lost_name_id):
        req = """
            SELECT user_id, lost_name_id, born, regions, description, feature, spec_feature, clothes, items, photo 
            FROM lost
            WHERE lost_name_id = ?
        """
        result = DatabaseConfig.cur.execute(req, (lost_name_id,)).fetchone()
        return result

    @staticmethod
    def delete_lost(lost_id):
        req = """
            DELETE 
            FROM lost
            WHERE lost_name_id = ?
        """
        DatabaseConfig.cur.execute(req, (lost_id,))
        DatabaseConfig.con.commit()

    @staticmethod
    def get_all_lost():
        req = """
            SELECT user_id, lost_name_id, born, regions, description, feature, spec_feature, clothes, items, photo 
            FROM lost
        """
        result = DatabaseConfig.cur.execute(req).fetchall()
        return result
