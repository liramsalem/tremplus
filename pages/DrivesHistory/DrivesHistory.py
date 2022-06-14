from flask import Blueprint, render_template, redirect, url_for,request, session
from utilities.db.db_Drives import *

# DrivesHistory blueprint definition
DrivesHistory = Blueprint('DrivesHistory', __name__, static_folder='static', static_url_path='/DrivesHistory', template_folder='templates')


# Routes
@DrivesHistory.route('/DrivesHistory')
def index():
    passenger_drive= db_Drives.find_all_past_passenger_drives(session['user_id'])
    if len(passenger_drive)==0:
        return render_template('DrivesHistory.html', message="עדיין לא התרחשה נסיעה!")
    return render_template('DrivesHistory.html',passenger_drive=passenger_drive)
