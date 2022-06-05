from utilities.db.db_manager import dbManager

class DBupdate_profile:

    @staticmethod
    def change_nickname(nickname, user_id):
        query = "update users set nickname='%s' where user_id='%s';" % (nickname, user_id)
        dbManager.commit(query=query)
        return

    @staticmethod
    def change_user_email(user_email, user_id):
        query = "update users set user_email='%s' where user_id='%s';" % (user_email, user_id)
        dbManager.commit(query=query)
        return

    @staticmethod
    def change_user_phone(phone, user_id):
        query = "update users set phone='%s' where user_id='%s';" % (phone, user_id)
        dbManager.commit(query=query)
        return

    @staticmethod
    def change_user_kibutz(kibutz, user_id):
        query = "update users set kibutz='%s' where user_id='%s';" % (kibutz, user_id)
        dbManager.commit(query=query)
        return

    @staticmethod
    def change_user_profile_pic(profile_pic, user_id):
        query = "update users set profile_pic='%s' where user_id='%s';" % (profile_pic, user_id)
        dbManager.commit(query=query)
        return

    @staticmethod
    def change_user_license_plate(license_plate, user_id):
        query = "update drivers set license_plate='%s' where user_id='%s';" % (license_plate, user_id)
        dbManager.commit(query=query)
        return

    @staticmethod
    def change_user_car_company(car_company, user_id):
        query = "update drivers set car_company='%s' where user_id='%s';" % (car_company, user_id)
        dbManager.commit(query=query)
        return

    @staticmethod
    def change_user_car_color(car_color, user_id):
        query = "update drivers set car_color='%s' where user_id='%s';" % (car_color, user_id)
        dbManager.commit(query=query)
        return

    @staticmethod
    def change_user_licence_driver_pic(licence_driver_pic, user_id):
        query = "update drivers set licence_driver_pic='%s' where user_id='%s';" % (licence_driver_pic, user_id)
        dbManager.commit(query=query)
        return

    @staticmethod
    def change_user_password(password, user_id):
        query = "update users set password='%s' where user_id='%s';" % (password, user_id)
        dbManager.commit(query=query)
        return

db_UpdateProfile = DBupdate_profile()