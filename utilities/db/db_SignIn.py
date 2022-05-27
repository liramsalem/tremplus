
from utilities.db.db_manager import dbManager

class DBsignIn:
    def check_user(self, user_email, password):
        user = "SELECT * FROM tremplus_db.users WHERE user_email='%s' AND password='%s';" % (user_email, password)
        res = dbManager.fetch(query=user)
        return res

    def check_if_user_is_driver(self, user_id):
        driver = "SELECT * FROM tremplus_db.drivers WHERE user_id='%s';" % (user_id)
        res = dbManager.fetch(query=driver)
        return res

db_SignIn = DBsignIn()