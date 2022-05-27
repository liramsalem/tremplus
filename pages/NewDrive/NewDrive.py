from flask import Blueprint, render_template, redirect, url_for,request, session
from utilities.db.db_Drives import *
from utilities.db.db_Register import *

# NewDrive blueprint definition
NewDrive = Blueprint('NewDrive', __name__, static_folder='static', static_url_path='/NewDrive', template_folder='templates')


# Routes
@NewDrive.route('/NewDrive')
def index():
    return render_template('NewDrive.html')

@NewDrive.route('/NewDrive_form',methods=['GET','POST'])
def add_new_drive():
    if request.method == 'POST':
        origin = request.form['origin']
        destination = request.form['destination']
        drive_date = request.form['drive_date']
        departure_hour = request.form['departure_hour']
        max_seats = request.form['max_seats']
        if origin==destination:
            return render_template('NewDrive.html', message="שים/י לב, מוצא ויעד חייבים להיות שונים!")
        not_exists= db_Drives.check_if_drive_is_exists(session['user_id'],drive_date,departure_hour)
        if not_exists:
            if db_Drives.add_drive(session['user_id'], origin, destination, drive_date, departure_hour, max_seats,max_seats )>0:
                return render_template('NewDrive.html',message="הנסיעה נוספה בהצלחה!")
            else:
                return render_template('NewDrive.html', message="חלה שגיאה, נא נסה מחדש!")
        else:
            return render_template('NewDrive.html', message="שים/י לב, קיימת לך נסיעה אחרת באותו תאריך ובאותה שעה!")

@NewDrive.route('/NewDriver_form',methods=['GET','POST'])
def add_new_driver():
    if request.method == 'POST':
        license_plate = request.form['license_plate']
        car_company = request.form['car_company']
        car_color = request.form['car_color']
        licence_driver_pic = request.form.get("licence_driver_img")
        if db_Register.insert_driver(session['user_id'],session['user_name'],session['user_Lname'], license_plate, car_company, car_color, licence_driver_pic,session['user_serial_num']) > 0 and db_Register.insert_driver_to_ranking(session['user_id']) > 0:
            session['driver'] = True
            return render_template('NewDrive.html', message="נרשמת בהצלחה!")
        else:
            return render_template('NewDrive.html', message="חלה שגיאה, נא נסה מחדש!")