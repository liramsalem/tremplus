from utilities.db.db_manager import dbManager

class DBprofile:

    @staticmethod
    def get_user_details(user_id):
        return dbManager.fetch(
        f"SELECT *  FROM users WHERE user_id='{user_id}'");


    @staticmethod
    def get_driver_details(user_id):
        return dbManager.fetch(
        f"SELECT *  FROM drivers WHERE user_id='{user_id}'");

    @staticmethod
    def get_user_psw(user_id):
        return dbManager.fetch(
        f"SELECT password  FROM users WHERE user_id='{user_id}'");




db_Profile = DBprofile()