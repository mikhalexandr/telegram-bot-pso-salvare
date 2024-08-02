from config import con, cur


class Checking:
    @staticmethod
    def add_checking(user_id, lost_name_id, born, regions, description, feature, spec_feature, clothes, items,
                     photo):
        req = """
            INSERT 
            INTO checking (user_id, lost_name_id, born, regions, description, feature, spec_feature, clothes, items, 
            photo)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cur.execute(req, (user_id, lost_name_id, born, regions, description, feature, spec_feature,
                          clothes, items, photo))
        con.commit()

    @staticmethod
    def get_checking(req_id):
        req = f"""
            SELECT *
            FROM checking
            WHERE lost_name_id = %s
        """
        cur.execute(req, (req_id,))
        return cur.fetchone()

    @staticmethod
    def delete_checking(lost_name_id):
        req = """
            DELETE 
            FROM checking
            WHERE lost_name_id = %s
        """
        cur.execute(req, (lost_name_id,))
        con.commit()
