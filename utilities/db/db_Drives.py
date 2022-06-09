from utilities.db.db_manager import dbManager

class DBdrives:
    @staticmethod
    def check_if_drive_is_exists(user_id_driver,drive_date,departure_hour):
        check_drive = dbManager.fetch(f"SELECT user_id_driver,drive_date,departure_hour FROM all_future_drives WHERE user_id_driver='{user_id_driver}' and drive_date='{drive_date}' and departure_hour='{departure_hour}'")
        if len(check_drive) == 0:
            return True
        else:
            return False

    @staticmethod
    def add_drive(user_id_driver, origin, destination, drive_date, departure_hour, max_seats, free_seats):
        return dbManager.commit(
            f"INSERT INTO all_future_drives (user_id_driver, origin, destination, drive_date, departure_hour, max_seats, free_seats) VALUES ('{user_id_driver}', '{origin}', '{destination}', '{drive_date}', '{departure_hour}','{max_seats}','{free_seats}')")

    @staticmethod
    def find_all_drivers_drives(user_id_driver):
        return dbManager.fetch(
        f"SELECT drive_id, user_id_driver, origin, destination, DATE_FORMAT(drive_date, '%d/%m/%y') as d_date, DATE_FORMAT(departure_hour, '%H:%i') as d_hour, max_seats, free_seats FROM all_future_drives WHERE user_id_driver='{user_id_driver}' and  drive_date>= CURRENT_DATE ORDER BY drive_date,departure_hour");

    @staticmethod
    def find_all_passenger_drives(user_id_passenger):
        return dbManager.fetch(
        f"SELECT t1.drive_id, t1.user_id_driver, t1.origin, t1.destination, DATE_FORMAT(t1.drive_date, '%d/%m/%y') as d_date,  DATE_FORMAT(t1.departure_hour, '%H:%i') as d_hour,t1.max_seats, t1.free_seats, t2.user_id_passenger, t2.seat_quantity FROM all_future_drives AS t1 JOIN participents_in_drive AS t2 ON t1.drive_id = t2.drive_id WHERE user_id_passenger='{user_id_passenger}'and  t1.drive_date>= CURRENT_DATE ORDER BY t1.drive_date,t1.departure_hour ");

    @staticmethod
    def find_all_past_passenger_drives(user_id_passenger):
        return dbManager.fetch(
        f"SELECT t1.drive_id, t1.user_id_driver, t1.origin, t1.destination, DATE_FORMAT(t1.drive_date, '%d/%m/%y') as d_date,  DATE_FORMAT(t1.departure_hour, '%H:%i') as d_hour, t2.user_id_passenger, t3.user_serial_num , t3.user_id FROM all_future_drives AS t1 JOIN participents_in_drive AS t2 ON t1.drive_id = t2.drive_id JOIN drivers AS t3 ON t1.user_id_driver=t3.user_id  WHERE user_id_passenger='{user_id_passenger}'and  t1.drive_date< CURRENT_DATE  ORDER BY t1.drive_date DESC ,t1.departure_hour ");

    @staticmethod
    def search_drive():
        return dbManager.fetch(
        f"SELECT drive_id, user_id_driver, origin, destination, DATE_FORMAT(drive_date, '%d/%m/%y') as d_date, DATE_FORMAT(departure_hour, '%H:%i') as d_hour, max_seats, free_seats FROM all_future_drives WHERE free_seats > 0 and  drive_date>= CURRENT_DATE ORDER BY drive_date,departure_hour ");

    @staticmethod
    def search_drive_by_origin_destination_drive_date(origin,destination,drive_date):
        return dbManager.fetch(
        f"SELECT drive_id, user_id_driver, origin, destination, DATE_FORMAT(drive_date, '%d/%m/%y') as d_date, DATE_FORMAT(departure_hour, '%H:%i') as d_hour, max_seats, free_seats FROM all_future_drives WHERE origin='{origin}' and destination='{destination}' and drive_date='{drive_date}' and free_seats > 0 and  drive_date>= CURRENT_DATE ORDER BY drive_date,departure_hour ");

    @staticmethod
    def search_drive_by_origin_destination(origin, destination):
        return dbManager.fetch(
            f"SELECT drive_id, user_id_driver, origin, destination, DATE_FORMAT(drive_date, '%d/%m/%y') as d_date, DATE_FORMAT(departure_hour, '%H:%i') as d_hour, max_seats, free_seats FROM all_future_drives WHERE origin='{origin}' and destination='{destination}' and free_seats > 0 and  drive_date>= CURRENT_DATE ORDER BY drive_date,departure_hour ");

    @staticmethod
    def search_drive_by_origin_drive_date(origin,drive_date):
        return dbManager.fetch(
        f"SELECT drive_id, user_id_driver, origin, destination, DATE_FORMAT(drive_date, '%d/%m/%y') as d_date, DATE_FORMAT(departure_hour, '%H:%i') as d_hour, max_seats, free_seats FROM all_future_drives WHERE origin='{origin}' and drive_date='{drive_date}' and free_seats > 0 and  drive_date>= CURRENT_DATE ORDER BY drive_date,departure_hour ");

    @staticmethod
    def search_drive_by_destination_drive_date(destination,drive_date):
        return dbManager.fetch(
        f"SELECT drive_id, user_id_driver, origin, destination, DATE_FORMAT(drive_date, '%d/%m/%y') as d_date, DATE_FORMAT(departure_hour, '%H:%i') as d_hour, max_seats, free_seats FROM all_future_drives WHERE destination='{destination}' and drive_date='{drive_date}' and free_seats > 0 and  drive_date>= CURRENT_DATE ORDER BY drive_date,departure_hour ");

    @staticmethod
    def search_drive_by_origin(origin):
        return dbManager.fetch(
        f"SELECT drive_id, user_id_driver, origin, destination, DATE_FORMAT(drive_date, '%d/%m/%y') as d_date, DATE_FORMAT(departure_hour, '%H:%i') as d_hour, max_seats, free_seats FROM all_future_drives WHERE origin='{origin}' and free_seats > 0 and  drive_date>= CURRENT_DATE ORDER BY drive_date,departure_hour ");

    @staticmethod
    def search_drive_by_destination(destination):
        return dbManager.fetch(
        f"SELECT drive_id, user_id_driver, origin, destination, DATE_FORMAT(drive_date, '%d/%m/%y') as d_date, DATE_FORMAT(departure_hour, '%H:%i') as d_hour, max_seats, free_seats FROM all_future_drives WHERE destination='{destination}' and free_seats > 0 and  drive_date>= CURRENT_DATE ORDER BY drive_date,departure_hour ");

    @staticmethod
    def search_drive_by_drive_date(drive_date):
        return dbManager.fetch(
        f"SELECT drive_id, user_id_driver, origin, destination, DATE_FORMAT(drive_date, '%d/%m/%y') as d_date, DATE_FORMAT(departure_hour, '%H:%i') as d_hour, max_seats, free_seats FROM all_future_drives WHERE drive_date='{drive_date}' and free_seats > 0 and  drive_date>= CURRENT_DATE ORDER BY drive_date,departure_hour");

    @staticmethod
    def search_drive_details_by_drive_id(drive_id):
        return dbManager.fetch(
        f"SELECT t1.drive_id, t1.user_id_driver, t1.origin, t1.destination, DATE_FORMAT(t1.drive_date, '%d/%m/%y') as d_date, DATE_FORMAT(t1.departure_hour, '%H:%i') as d_hour,t1.max_seats,t1.free_seats,t2.user_id, t2.Fname, t2.Lname,t2.license_plate, t2.car_company, t2.car_color, t3.profile_pic, t3.user_serial_num  FROM all_future_drives as t1 JOIN drivers as t2 ON t1.user_id_driver = t2.user_id JOIN users as t3 ON t2.user_id=t3.user_id WHERE drive_id='{drive_id}'");

    @staticmethod
    def check_participents_in_drive(drive_id):
        check_participents = dbManager.fetch(f"SELECT *  FROM participents_in_drive WHERE drive_id='{drive_id}'");
        if len(check_participents) == 0:
            return False
        else:
            return True

    @staticmethod
    def search_participents_details_by_drive_id(drive_id):
        return dbManager.fetch(
        f"SELECT t1.drive_id, t1.user_id_passenger,t2.user_id, t2.Fname, t2.Lname,t2.nickname, t2.phone, t2.profile_pic, t2.user_serial_num  FROM participents_in_drive as t1 JOIN users as t2 ON t1.user_id_passenger = t2.user_id WHERE drive_id='{drive_id}'");

    @staticmethod
    def get_driver_details_by_drive_id(drive_id):
        return dbManager.fetch(
        f"SELECT t1.drive_id, t1.user_id_driver, t2.user_id, t2.license_plate ,t2.car_company, t2.car_color, t3.Fname, t3.Lname, t3.nickname, t3.phone, t3.profile_pic, t3.kibutz, t3.user_serial_num FROM all_future_drives as t1 JOIN drivers as t2 ON t1.user_id_driver = t2.user_id JOIN users as t3 ON t2.user_id=t3.user_id WHERE drive_id='{drive_id}'");

    @staticmethod
    def get_driver_details_by_user_id(user_id):
        return dbManager.fetch(
        f"SELECT * FROM  drivers  WHERE user_id='{user_id}'");


    @staticmethod
    def check_if_passenger_is_also_driver(user_id):
        check_passenger = dbManager.fetch(f"SELECT *  FROM drivers WHERE user_id='{user_id}'");
        if len(check_passenger) == 0:
            return False
        else:
            return True

    @staticmethod
    def get_passenger_details_by_passenger_serial_num(passenger_serial_num):
        return dbManager.fetch(
        f"SELECT *  FROM users WHERE user_serial_num='{passenger_serial_num}'");


    @staticmethod
    def check_if_user_is_driver_in_this_ride(drive_id,user_id_driver):
        if_user_is_driver= dbManager.fetch(f"SELECT * FROM all_future_drives WHERE drive_id='{drive_id}' AND user_id_driver='{user_id_driver}'");
        if len(if_user_is_driver)==0:
            return False
        else:
            return True

    @staticmethod
    def check_if_user_in_drive(drive_id,user_id_passenger ):
        if_exist= dbManager.fetch(f"SELECT * FROM participents_in_drive WHERE drive_id='{drive_id}' AND user_id_passenger='{user_id_passenger}'");
        if len(if_exist)==0:
            return False
        else:
            return True

    @staticmethod
    def add_passenger_to_drive(drive_id,user_id_passenger,user_serial_num,seat_quantity):
        return dbManager.commit(
            f"INSERT INTO participents_in_drive (drive_id, user_id_passenger,user_serial_num, seat_quantity) VALUES ('{drive_id}', '{user_id_passenger}', '{user_serial_num}', '{seat_quantity}')")

    @staticmethod
    def set_free_seats(drive_id,act):
        if act=="add":
            return dbManager.commit(f"UPDATE all_future_drives SET free_seats=free_seats-1  WHERE drive_id='{drive_id}'")
        if act =="remove":
            return dbManager.commit(f"UPDATE all_future_drives SET free_seats=free_seats+1  WHERE drive_id='{drive_id}'")

    @staticmethod
    def remove_passenger_from_drive(drive_id,user_id_passenger):
        return dbManager.commit(
            f"DELETE FROM participents_in_drive WHERE drive_id='{drive_id}' AND user_id_passenger={user_id_passenger}");

    @staticmethod
    def remove_all_passengers_from_drive(drive_id):
        return dbManager.commit(
            f"DELETE FROM participents_in_drive WHERE drive_id='{drive_id}'");

    @staticmethod
    def remove_drive(drive_id):
        return dbManager.commit(
            f"DELETE FROM all_future_drives WHERE drive_id='{drive_id}'");

    @staticmethod
    def find_driver_name_email(drive_id):
        table= dbManager.fetch(
            f"SELECT t1.user_email, t1.Fname, t1.Lname, t2.user_id_driver  FROM users as t1 join all_future_drives as t2 on t2.user_id_driver = t1. user_id  WHERE drive_id='{drive_id}'");
        return table[0]

    @staticmethod
    def find_drive_details(drive_id):
        table= dbManager.fetch(
            f"SELECT origin, destination, DATE_FORMAT(drive_date, '%d/%m/%y') as d_date, DATE_FORMAT(departure_hour, '%H:%i') as d_hour  FROM all_future_drives WHERE drive_id='{drive_id}'");
        return table[0]

    @staticmethod
    def find_participents_name_email(drive_id):
        return dbManager.fetch(
        f"SELECT t2.user_email, t2.Fname, t2.Lname, t2.user_id, t1.user_id_passenger  FROM participents_in_drive as t1 JOIN users as t2 ON t1.user_id_passenger = t2.user_id WHERE drive_id='{drive_id}'");


db_Drives = DBdrives()