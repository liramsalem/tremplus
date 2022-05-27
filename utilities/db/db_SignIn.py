
from utilities.db.db_manager import dbManager

class DBsignIn:
    @staticmethod
    def check_user(user_email, password):
        user = dbManager.fetch(f"SELECT * FROM users WHERE user_email='{user_email}' and password='{password}' ")
        return user

    @staticmethod
    def check_if_user_is_driver(user_id):
        driver = dbManager.fetch(f"SELECT * FROM drivers WHERE user_id='{user_id}'")
        return driver



    # def check_user(self, user_email, password):
    #     user = "SELECT * FROM tremplus_db.users WHERE user_email='%s' AND password='%s';" % (user_email, password)
    #     res = dbManager.fetch(query=user)
    #     return res

    # def check_if_user_is_driver(self, user_id):
    #     driver = "SELECT * FROM tremplus_db.drivers WHERE user_id='%s';" % (user_id)
    #     res = dbManager.fetch(query=driver)
    #     return res

db_SignIn = DBsignIn()