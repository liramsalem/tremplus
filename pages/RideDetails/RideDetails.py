from flask import Blueprint, render_template,redirect,request,session, url_for
from utilities.db.db_Drives import *
from utilities.db.db_Ranking import *

# RideDetails blueprint definition
RideDetails = Blueprint('RideDetails', __name__, static_folder='static', static_url_path='/RideDetails', template_folder='templates')


# Routes
@RideDetails.route('/RideDetails')
def index():
    session['details_for_driver'] = False
    drive_id= request.args.get("drive_id")
    res= db_Drives.search_drive_details_by_drive_id(drive_id)[0]
    print(res)
    driver_id = res[1]
    print(driver_id)
    a=db_Ranking.get_avg_total(driver_id)
    print(a)
    rank_avg_votes = db_Ranking.get_avg_total(driver_id)[0]
    print(rank_avg_votes)
    round_avg = round((float(rank_avg_votes[0])), 2)
    total_votes = rank_avg_votes[1]
    return render_template('RideDetails.html',res=res,drive_id=drive_id,round_avg=round_avg,total_votes=total_votes)
