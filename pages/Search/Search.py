from flask import Blueprint, render_template, redirect, url_for,request, session
from utilities.db.db_Drives import *
from utilities.mail import sendEmail

# Search blueprint definition
Search = Blueprint('Search', __name__, static_folder='static', static_url_path='/Search', template_folder='templates')


# Routes
@Search.route('/Search')
def index():
    session['search'] = False
    return render_template('Search.html')

@Search.route('/Search_form',methods=['GET','POST'])
def search_req():
    if request.method == 'GET':
        session['search'] = True
        origin = request.args.get('origin')
        destination = request.args.get('destination')
        drive_date = request.args.get('drive_date')
        flag = False;
        if session:
            if not origin and not destination and not drive_date:
                session['search'] = False
                return render_template('Search.html', message="על מנת לבצע חיפוש יש למלא לפחות אחת מהשורות")
            if origin and destination and drive_date:
                res = db_Drives.search_drive_by_origin_destination_drive_date(origin,destination,drive_date)
                if len(res)==0:
                    flag=True
            elif origin and destination:
                res = db_Drives.search_drive_by_origin_destination(origin, destination)
                if len(res)==0:
                    flag=True
            elif origin and drive_date:
                res = db_Drives.search_drive_by_origin_drive_date(origin, drive_date)
                if len(res)==0:
                    flag=True
            elif destination and drive_date:
                res = db_Drives.search_drive_by_destination_drive_date(destination, drive_date)
                if len(res)==0:
                    flag=True
            elif origin:
                res = db_Drives.search_drive_by_origin(origin)
                if len(res)==0:
                    flag=True
            elif destination:
                res = db_Drives.search_drive_by_destination(destination)
                if len(res)==0:
                    flag=True
            elif drive_date:
                res = db_Drives.search_drive_by_drive_date(drive_date)
                if len(res)==0:
                    flag=True
            if flag==True:
                return render_template('Search.html',message="לא נמצאו נסיעות מתאימות!")
            else:
                return render_template('Search.html', res=res)

@Search.route('/Search_all_drive_form',methods=['GET','POST'])
def search_req1():
    if request.method == 'GET':
        session['search'] = True
        if session:
            res = db_Drives.search_drive()
            if len(res) == 0:
                return render_template('Search.html', message="לא נמצאו נסיעות מתאימות!")
            return render_template('Search.html', res=res)



@Search.route('/addToDrive_form',methods=['GET','POST'])
def add_to_drive_req():
    if request.method == 'POST':
        drive_id = request.form['drive_id']
        if request.form['req'] == "add":
            if db_Drives.check_if_user_is_driver_in_this_ride(drive_id,session['user_id']):
                return render_template('Search.html', message='הנך הנהג בנסיעה זו!')
            else:
                if db_Drives.check_if_user_in_drive(drive_id,session['user_id']):
                    return render_template('Search.html', message='הנך כבר רשום לנסיעה זו')
                else:
                    db_Drives.add_passenger_to_drive(drive_id,session['user_id'],session['user_serial_num'],1);
                    db_Drives.set_free_seats(drive_id,"add");
                    # driver_details_for_email = db_Drives.find_driver_name_email(drive_id);
                    # drive_details_for_email = db_Drives.find_drive_details(drive_id);
                    # print(driver_details_for_email)
                    # print(drive_details_for_email)
                    # sendEmail(driver_details_for_email[1], driver_details_for_email[2], driver_details_for_email[0],
                    #           f"נוסע הצטרף לנסיעה החלה בתאריך {drive_details_for_email[2]} בשעה {drive_details_for_email[3]} מ- {drive_details_for_email[0]} ל- {drive_details_for_email[1]}")
                    return render_template('Search.html', message='הצטרפת בהצלחה! נסיעה טובה')




