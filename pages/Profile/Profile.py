from flask import Blueprint, render_template, redirect, url_for,request, session
from utilities.db.db_Profile import db_Profile
from utilities.db.db_Ranking import *


# Profile blueprint definition
Profile = Blueprint('Profile', __name__, static_folder='static', static_url_path='/Profile', template_folder='templates')


# Routes
@Profile.route('/Profile')
def index():
    res_user_details= db_Profile.get_user_details(session['user_id'])
    res_driver_details = db_Profile.get_driver_details(session['user_id'])
    rank_avg_votes = db_Ranking.get_avg_total(session['user_id'])
    if len(rank_avg_votes) == 0:
        return render_template('Profile.html', res_user_details=res_user_details, res_driver_details=res_driver_details,)
    else:
        round_avg = round((float(rank_avg_votes[0][0])), 2)
        total_votes = rank_avg_votes[0][1]
        return render_template('Profile.html', res_user_details=res_user_details, res_driver_details=res_driver_details,round_avg=round_avg,total_votes=total_votes)


