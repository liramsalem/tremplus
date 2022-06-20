from flask import Blueprint, render_template,redirect,request,session, url_for
from utilities.db.db_Drives import *
from utilities.db.db_Ranking import *

# RideDetailsForDriver blueprint definition
RideDetailsForDriver = Blueprint('RideDetailsForDriver', __name__, static_folder='static', static_url_path='/RideDetailsForDriver', template_folder='templates')


# Routes
@RideDetailsForDriver.route('/RideDetailsForDriver')
def index():
    session['details_for_driver'] = True
    drive_id = request.args.get("drive_id")
    res_drive_details = db_Drives.search_drive_details_by_drive_id(drive_id)[0]
    driver_id = res_drive_details[1]
    rank_avg_votes = db_Ranking.get_avg_total(driver_id)[0]
    round_avg = round((float(rank_avg_votes[0])), 2)
    total_votes = rank_avg_votes[1]
    if db_Drives.check_participents_in_drive(drive_id):
        res_participents_details= db_Drives.search_participents_details_by_drive_id(drive_id)
        return render_template('RideDetailsForDriver.html', res_drive_details=res_drive_details, drive_id=drive_id,res_participents_details=res_participents_details,round_avg=round_avg,total_votes=total_votes)
    else:
        return render_template('RideDetailsForDriver.html', res_drive_details=res_drive_details, drive_id=drive_id,message="עדייו לא נוספו נוסעים לנסיעה זו!",round_avg=round_avg,total_votes=total_votes)
