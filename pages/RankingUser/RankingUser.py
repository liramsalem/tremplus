from flask import Blueprint, render_template,redirect,request,session, url_for
from utilities.db.db_Drives import *
from utilities.db.db_Ranking import *

# RankingUser blueprint definition
RankingUser = Blueprint('RankingUser', __name__, static_folder='static', static_url_path='/RankingUser', template_folder='templates')

# Routes
@RankingUser.route('/RankingUser',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        drive_id = request.form["drive_id"]
        driver_serial_num = request.form["driver_serial_num"]
        star_value = request.form.get("rate")
        driver_id = db_Ranking.get_user_id_by_serial_num(driver_serial_num)
        if not star_value:
            res = db_Drives.search_drive_details_by_drive_id(drive_id)
            rank_avg_votes = db_Ranking.get_avg_total(driver_id)
            round_avg = round((float(rank_avg_votes[0][0])), 2)
            total_votes = rank_avg_votes[0][1]
            return render_template('RankingUser.html', message="נא לבחור דירוג!", res=res, drive_id=drive_id,
                                   round_avg=round_avg, total_votes=total_votes)
        db_Ranking.add_vote(star_value, driver_id)
        db_Ranking.calc_avg(driver_id)
        db_Ranking.update_participent_bool_rank(session['user_id'],drive_id)
        res = db_Drives.search_drive_details_by_drive_id(drive_id)
        rank_avg_votes = db_Ranking.get_avg_total(driver_id)
        round_avg = round((float(rank_avg_votes[0][0])), 2)
        total_votes = rank_avg_votes[0][1]
        return redirect(url_for('MsgToUser.index'))
    drive_id = request.args.get("drive_id")
    this_drive_is_already_ranked = db_Ranking.participent_bool_rank(session['user_id'], drive_id)
    driver_serial_num = request.args.get("driver_serial_num")
    driver_id = db_Ranking.get_user_id_by_serial_num(driver_serial_num)
    res = db_Drives.search_drive_details_by_drive_id(drive_id)
    rank_avg_votes = db_Ranking.get_avg_total(driver_id)
    round_avg = round((float(rank_avg_votes[0][0])), 2)
    total_votes= rank_avg_votes[0][1]
    return render_template('RankingUser.html', res=res, drive_id=drive_id,
                           round_avg=round_avg, total_votes=total_votes,
                           this_drive_is_already_ranked=this_drive_is_already_ranked)
