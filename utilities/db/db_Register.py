from utilities.db.db_manager import dbManager

class DBregister:

    @staticmethod
    def check_user_exists(user_id):
        check_id = dbManager.fetch(f"SELECT user_id FROM users WHERE user_id='{user_id}'")
        if len(check_id) == 0:
            return False
        else:
            return True

    @staticmethod
    def check_if_belongs(id_Number, kibutz):
        belongs = dbManager.fetch(
            f"SELECT id_Number,kibutz FROM ResidentRegistration_table WHERE kibutz='{kibutz}'and id_Number='{id_Number}'")
        if len(belongs) == 0:
            return False
        else:
            return True

    @staticmethod
    def insert_user(Fname, Lname, nickname, kibutz, user_id, phone, user_email, password, profile_pic):
        return dbManager.commit(
            f"INSERT INTO users (Fname, Lname, nickname, kibutz, user_id, phone, user_email, password, profile_pic) VALUES ('{Fname}', '{Lname}', '{nickname}', '{kibutz}', '{user_id}', '{phone}','{user_email}', '{password}', '{profile_pic}')")

    @staticmethod
    def get_user_serial_num(user_id):
        serial= dbManager.fetch(
            f"SELECT user_serial_num FROM users WHERE user_id='{user_id}'")
        a=serial[0]
        b = serial[0][0]
        print(serial)
        print(serial[0])
        return serial[0][0]

    @staticmethod
    def insert_driver(user_id,Fname, Lname, license_plate, car_company, car_color, licence_driver_pic,user_serial_num):
        return dbManager.commit(
            f"INSERT INTO drivers (user_id, Fname, Lname, license_plate, car_company, car_color, licence_driver_pic, user_serial_num) VALUES ('{user_id}','{Fname}', '{Lname}', '{license_plate}', '{car_company}', '{car_color}', '{licence_driver_pic}', '{user_serial_num}')")

    @staticmethod
    def insert_driver_to_ranking(driver_id):
        return dbManager.commit(
            f"INSERT INTO ranking (driver_id) VALUES ('{driver_id}')")

db_Register = DBregister()