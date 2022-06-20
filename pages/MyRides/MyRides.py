from flask import Blueprint, render_template, redirect, url_for,request, session
from utilities.db.db_Drives import *
from utilities.mail import sendEmail


# MyRides blueprint definition
MyRides = Blueprint('MyRides', __name__, static_folder='static', static_url_path='/MyRides', template_folder='templates')


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
                driver_details_for_email = db_Drives.find_driver_name_email(drive_id);
                drive_details_for_email = db_Drives.find_drive_details(drive_id);
                sendEmail(driver_details_for_email[1],driver_details_for_email[2],driver_details_for_email[0],f"נוסע הוסר מנסיעה החלה בתאריך {drive_details_for_email[2]} בשעה {drive_details_for_email[3]} מ- {drive_details_for_email[0]} ל- {drive_details_for_email[1]}")
                return render_template('MyRides.html', message='ההסרה בוצעה בהצלחה!' , drivers_drive=drivers_drive, passenger_drive=passenger_drive)
        if request.form['req'] == "remove_drive":
            participents_details_for_email = db_Drives.find_participents_name_email(drive_id);
            drive_details_for_email = db_Drives.find_drive_details(drive_id);
            db_Drives.remove_all_passengers_from_drive(drive_id);
            db_Drives.remove_drive(drive_id);
            drivers_drive = db_Drives.find_all_drivers_drives(session['user_id'])
            passenger_drive = db_Drives.find_all_passenger_drives(session['user_id'])
            for i in range(len(participents_details_for_email)):
                sendEmail(participents_details_for_email[i][1], participents_details_for_email[i][2], participents_details_for_email[i][0],
                      f"שימ/י לב!, הנסיעה מ-  {drive_details_for_email[0]} ל- {drive_details_for_email[1]} ב- {drive_details_for_email[2]} בשעה {drive_details_for_email[3]} התבטלה. ")
            return render_template('MyRides.html', message='ההסרה בוצעה בהצלחה!', drivers_drive=drivers_drive,
                                   passenger_drive=passenger_drive)
    return render_template('MyRides.html',drivers_drive=drivers_drive,passenger_drive=passenger_drive)

