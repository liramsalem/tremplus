from flask import Blueprint, render_template,redirect,request,session, url_for
from utilities.db.db_Drives import *
from utilities.db.db_Ranking import *

# RankingUser blueprint definition
RankingUser = Blueprint('RankingUser', __name__, static_folder='static', static_url_path='/RankingUser', template_folder='templates')

# Routes
@RankingUser.route('/RankingUser',methods=['GET','POST'])
def index():
    # not_ranked_yet= False
    if request.method == 'POST':
        drive_id = request.form["drive_id"]
        print(drive_id)
        driver_serial_num = request.form["driver_serial_num"]
        print(driver_serial_num)
        print("form")
        star_value = request.form.get("rate")
        print(star_value)
        driver_id = db_Ranking.get_user_id_by_serial_num(driver_serial_num)
        print(driver_id)
        if not star_value:
            res = db_Drives.search_drive_details_by_drive_id(drive_id)
            print("res_form")
            print(res)
            print(db_Drives.search_drive_details_by_drive_id(drive_id))
            rank_avg_votes = db_Ranking.get_avg_total(driver_id)
            round_avg = round((float(rank_avg_votes[0][0])), 2)
            total_votes = rank_avg_votes[0][1]
            return render_template('RankingUser.html', message="נא לבחור דירוג!", res=res, drive_id=drive_id,
                                   round_avg=round_avg, total_votes=total_votes)
            # return render_template('RankingUser.html', message="נא לבחור דירוג!", res=res, drive_id=drive_id,
            #                        round_avg=round_avg, total_votes=total_votes,not_ranked_yet=not_ranked_yet)
        db_Ranking.add_vote(star_value, driver_id)
        db_Ranking.calc_avg(driver_id)
        # not_ranked_yet= True
        db_Ranking.update_participent_bool_rank(session['user_id'],drive_id)
        res = db_Drives.search_drive_details_by_drive_id(drive_id)
        rank_avg_votes = db_Ranking.get_avg_total(driver_id)
        round_avg = round((float(rank_avg_votes[0][0])), 2)
        total_votes = rank_avg_votes[0][1]
        return redirect(url_for('MsgToUser.index'))
        # return render_template('MsgToUser.html',message="הדירוג התקבל בהצלחה!")
        # return render_template('RankingUser.html', res=res, drive_id=drive_id,
        #                        round_avg=round_avg, total_votes=total_votes, star_value=star_value, msg2="הדירוג התקבל בהצלחה!",not_ranked_yet=not_ranked_yet)
    drive_id = request.args.get("drive_id")
    this_drive_is_already_ranked = db_Ranking.participent_bool_rank(session['user_id'], drive_id)
    driver_serial_num = request.args.get("driver_serial_num")
    driver_id = db_Ranking.get_user_id_by_serial_num(driver_serial_num)
    res = db_Drives.search_drive_details_by_drive_id(drive_id)
    print("avf1")
    print(drive_id)
    print(driver_serial_num)
    print(driver_id)
    print(session['user_id'])
    print(this_drive_is_already_ranked)
    print(123)
    print(res)
    rank_avg_votes = db_Ranking.get_avg_total(driver_id)
    print(rank_avg_votes)
    round_avg = round((float(rank_avg_votes[0][0])), 2)
    print(round_avg)
    total_votes= rank_avg_votes[0][1]
    return render_template('RankingUser.html', res=res, drive_id=drive_id,
                           round_avg=round_avg, total_votes=total_votes,
                           this_drive_is_already_ranked=this_drive_is_already_ranked)
    # return render_template('RankingUser.html', res=res, drive_id=drive_id,round_avg=round_avg,total_votes=total_votes,this_drive_is_already_ranked=this_drive_is_already_ranked,not_ranked_yet=not_ranked_yet)

# @RankingUser.route('/ranking_form',methods=['GET','POST'])
# def ranking_form():
#     drive_id = request.form["drive_id"]
#     driver_id = request.form["driver_id"]
#     res = db_Drives.search_drive_details_by_drive_id(drive_id)[0]
#     rank_avg_votes = db_Ranking.get_avg_total(driver_id)
#     round_avg = round((float(rank_avg_votes[0][0])), 2)
#     total_votes = rank_avg_votes[0][1]
#     if flag == False :
#         star_value= request.form["rate"]
#         if star_value== None:
#             return render_template('RankingUser.html', message="נא לבחור דירוג!", res=res, drive_id=drive_id,
#                                    round_avg=round_avg,total_votes=total_votes, flag=flag)
#         db_Ranking.add_vote(star_value, driver_id)
#         db_Ranking.calc_avg(driver_id)
#         star_value = 0
#         flag = True
#         return render_template('RankingUser.html',message="הדירוג התקבל בהצלחה!", res=res, drive_id=drive_id,round_avg=round_avg,total_votes=total_votes, flag=flag,star_value=star_value)
#     return render_template('RankingUser.html', res=res, drive_id=drive_id, round_avg=round_avg,total_votes=total_votes)