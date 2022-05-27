from utilities.db.db_manager import dbManager


class UsersClass:

    @staticmethod
    def check_user_in_db(user_email,password):
        check_email = dbManager.fetch(f"SELECT user_email FROM users WHERE user_email='{user_email}'")
        if len(check_email)==0:
            return False
        else:
            check_password = dbManager.fetch(f"SELECT password FROM users WHERE user_email='{user_email}'")
            if password ==  check_password[0][0]:
                 return True
            else:
                  return False

    @staticmethod
    def get_user_name(user_email):
        name= dbManager.fetch(f"SELECT Fname FROM users WHERE user_email='{user_email}'")
        return name[0][0]

    @staticmethod
    def check_user_exists(user_id):
        check_id = dbManager.fetch(f"SELECT user_id FROM users WHERE user_id='{user_id}'")
        a= check_id
        if len(check_id)==0:
            return False
        else:
            return True

    @staticmethod
    def check_if_belongs(user_id,kibutz_name):
        belongs = dbManager.fetch(f"SELECT user_id,kibutz FROM ResidentRegistration_table WHERE kibutz_name='{kibutz_name}'and user_id='{user_id}'")
        if belongs[0]>0:
            return True
        else:
            return False

    @staticmethod
    def insert_user(Fname, Lname, kibutz, user_id, phone, user_email, password):
        return dbManager.commit(
            f"INSERT INTO users (Fname, Lname, kibutz, user_id, phone, user_email, password) VALUES ('{Fname}', '{Lname}', '{kibutz}', '{user_id}', '{phone}','{user_email}', '{password}')")



# Creates an instance for the DBManager class for export.
user = UsersClass()


