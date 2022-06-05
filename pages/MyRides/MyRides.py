from flask import Blueprint, render_template, redirect, url_for,request, session
from utilities.db.db_Drives import *
# from flask_mail import Mail, Message


# MyRides blueprint definition
MyRides = Blueprint('MyRides', __name__, static_folder='static', static_url_path='/MyRides', template_folder='templates')
# mail = Mail(MyRides)

# Routes
@MyRides.route('/MyRides',methods=['GET','POST'])
def index():
    session['search'] = False
    drivers_drive= db_Drives.find_all_drivers_drives(session['user_id'])
    passenger_drive= db_Drives.find_all_passenger_drives(session['user_id'])
    if request.method == 'POST':
        drive_id = request.form['drive_id']
        if request.form['req'] == "remove_passenger":
                db_Drives.remove_passenger_from_drive(drive_id,session['user_id']);
                db_Drives.set_free_seats(drive_id,"remove");
                drivers_drive = db_Drives.find_all_drivers_drives(session['user_id'])
                passenger_drive = db_Drives.find_all_passenger_drives(session['user_id'])
                # driver_email = db_Drives.find_driver_email(drive_id);
                # print(driver_email)
                # msg = Message("TREMPLUS",sender='tremplus@outlook.com', recipients=[driver_email] )
                # msg.body = "שלום, נוסע נמחק מנסיעה"
                # mail.send(msg)
                return render_template('MyRides.html', message='ההסרה בוצעה בהצלחה!' , drivers_drive=drivers_drive, passenger_drive=passenger_drive)
        if request.form['req'] == "remove_drive":
            db_Drives.remove_all_passengers_from_drive(drive_id);
            db_Drives.remove_drive(drive_id);
            drivers_drive = db_Drives.find_all_drivers_drives(session['user_id'])
            passenger_drive = db_Drives.find_all_passenger_drives(session['user_id'])
            return render_template('MyRides.html', message='ההסרה בוצעה בהצלחה!', drivers_drive=drivers_drive,
                                   passenger_drive=passenger_drive)
    return render_template('MyRides.html',drivers_drive=drivers_drive,passenger_drive=passenger_drive)

