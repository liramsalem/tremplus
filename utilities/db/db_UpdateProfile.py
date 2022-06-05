from utilities.db.db_manager import dbManager

class DBupdate_profile:

    def change_nickname(self, nickname, user_id):
        query = "update tremplus_db.users set nickname='%s' where user_id='%s';" % (nickname, user_id)
        dbManager.commit(query=query)
        return

    def change_user_email(self, user_email, user_id):
        query = "update tremplus_db.users set user_email='%s' where user_id='%s';" % (user_email, user_id)
        dbManager.commit(query=query)
        return

    def change_user_phone(self, phone, user_id):
        query = "update tremplus_db.users set phone='%s' where user_id='%s';" % (phone, user_id)
        dbManager.commit(query=query)
        return

    def change_user_kibutz(self, kibutz, user_id):
        query = "update tremplus_db.users set kibutz='%s' where user_id='%s';" % (kibutz, user_id)
        dbManager.commit(query=query)
        return

    def change_user_profile_pic(self, profile_pic, user_id):
        query = "update tremplus_db.users set profile_pic='%s' where user_id='%s';" % (profile_pic, user_id)
        dbManager.commit(query=query)
        return

    def change_user_license_plate(self, license_plate, user_id):
        query = "update tremplus_db.drivers set license_plate='%s' where user_id='%s';" % (license_plate, user_id)
        dbManager.commit(query=query)
        return

    def change_user_car_company(self, car_company, user_id):
        query = "update tremplus_db.drivers set car_company='%s' where user_id='%s';" % (car_company, user_id)
        dbManager.commit(query=query)
        return

    def change_user_car_color(self, car_color, user_id):
        query = "update tremplus_db.drivers set car_color='%s' where user_id='%s';" % (car_color, user_id)
        dbManager.commit(query=query)
        return

    def change_user_licence_driver_pic(self, licence_driver_pic, user_id):
        query = "update tremplus_db.drivers set licence_driver_pic='%s' where user_id='%s';" % (licence_driver_pic, user_id)
        dbManager.commit(query=query)
        return

    @staticmethod
    def change_user_password(newpsw, user_id):
        return dbManager.commit(f"UPDATE users SET password=newpsw  WHERE user_id='{user_id}'")


db_UpdateProfile = DBupdate_profile()