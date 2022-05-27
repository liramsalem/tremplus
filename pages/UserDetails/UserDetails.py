from flask import Blueprint, render_template,redirect,request,session, url_for
from utilities.db.db_Drives import *
from utilities.db.db_Ranking import *

# UserDetails blueprint definition
UserDetails = Blueprint('UserDetails', __name__, static_folder='static', static_url_path='/UserDetails', template_folder='templates')


# Routes
@UserDetails.route('/UserDetails')
def index():
    drive_id= request.args.get("drive_id")
    passenger_serial_num= request.args.get("passenger_serial_num")
    print(drive_id)
    print(passenger_serial_num)
    if passenger_serial_num==None:
        passenger_details= False;
        driver_details=True;
        res= db_Drives.get_driver_details_by_drive_id(drive_id)[0]
        driver_id= res[1]
        print(driver_id)
        rank_avg_votes = db_Ranking.get_avg_total(driver_id)[0]
        round_avg = round((float(rank_avg_votes[0])), 2)
        total_votes = rank_avg_votes[1]
        return render_template('UserDetails.html',passenger_details=passenger_details,driver_details=driver_details, res=res, drive_id=drive_id,round_avg=round_avg,total_votes=total_votes)
    else:
        passenger_details= True;
        driver_details=False;
        res_p = db_Drives.get_passenger_details_by_passenger_serial_num(passenger_serial_num)[0]
        passenger_id= res_p[4]
        if_passenger_is_also_driver= db_Drives.check_if_passenger_is_also_driver(passenger_id)
        if if_passenger_is_also_driver:
            passenger_also_driver = True;
            res_p_d= db_Drives.get_driver_details_by_user_id(passenger_id)[0]
            driver_id= res_p_d[0]
            print(driver_id)
            rank_avg_votes = db_Ranking.get_avg_total(driver_id)[0]
            round_avg = round((float(rank_avg_votes[0])), 2)
            total_votes = rank_avg_votes[1]
            return render_template('UserDetails.html', passenger_details=passenger_details,
                                   driver_details=driver_details, res_p=res_p,res_p_d=res_p_d,passenger_also_driver=passenger_also_driver, passenger_id=passenger_id ,drive_id=drive_id, round_avg=round_avg,
                                   total_votes=total_votes,)
        else:
            return render_template('UserDetails.html', passenger_details=passenger_details, driver_details=driver_details, res_p=res_p, passenger_id=passenger_id,drive_id=drive_id)



