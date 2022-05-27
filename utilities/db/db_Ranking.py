from utilities.db.db_manager import dbManager

class DBranking:

    @staticmethod
    def add_vote(star_value, driver_id):
        if star_value == "1":
            return dbManager.commit(f"UPDATE ranking SET one_star=one_star+1  WHERE driver_id='{driver_id}'")
        if star_value == "2":
            return dbManager.commit(f"UPDATE ranking SET two_star=two_star+1  WHERE driver_id='{driver_id}'")
        if star_value == "3":
            return dbManager.commit(f"UPDATE ranking SET three_star=three_star+1  WHERE driver_id='{driver_id}'")
        if star_value == "4":
            return dbManager.commit(f"UPDATE ranking SET four_star=four_star+1  WHERE driver_id='{driver_id}'")
        if star_value == "5":
            return dbManager.commit(f"UPDATE ranking SET five_star=five_star+1  WHERE driver_id='{driver_id}'")

    @staticmethod
    def calc_avg(driver_id):
        dbManager.commit(f"UPDATE ranking SET total_votes = one_star+two_star+three_star+four_star+five_star WHERE driver_id='{driver_id}'")
        dbManager.commit(f"UPDATE ranking SET total_stars = one_star*1 + two_star*2 + three_star*3 + four_star*4 + five_star*5 WHERE driver_id='{driver_id}'")
        return dbManager.commit(f"UPDATE ranking SET avg = total_stars/total_votes WHERE driver_id='{driver_id}'")

    @staticmethod
    def get_avg_total(driver_id):
        return dbManager.fetch(f"SELECT avg,total_votes FROM ranking WHERE driver_id='{driver_id}'");


    @staticmethod
    def update_participent_bool_rank(user_id_passenger,drive_id):
        return dbManager.commit(f"UPDATE participents_in_drive SET user_ranking='1' WHERE user_id_passenger='{user_id_passenger}' AND drive_id='{drive_id}'");

    @staticmethod
    def participent_bool_rank(user_id_passenger,drive_id):
        res= dbManager.fetch(f"SELECT user_ranking FROM participents_in_drive WHERE user_id_passenger='{user_id_passenger}' AND drive_id='{drive_id}'");
        if res[0][0] =="0":
            return False
        return True

    @staticmethod
    def get_user_id_by_serial_num(user_serial_num):
        user_id= dbManager.fetch(f"SELECT user_id FROM users WHERE user_serial_num='{user_serial_num}'");
        return user_id[0][0]

db_Ranking = DBranking()