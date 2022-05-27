from flask import Blueprint, render_template, redirect, url_for,request, session
from utilities.db.db_Profile import db_Profile
from utilities.db.db_UpdateProfile import db_UpdateProfile
from utilities.db.db_Register import *
from utilities.db.db_Ranking import *

# Edit_Profile blueprint definition
Edit_Profile = Blueprint('Edit_Profile', __name__, static_folder='static', static_url_path='/Edit_Profile', template_folder='templates')

# Routes
@Edit_Profile.route('/Edit_Profile')
def index():
    res_user_details= db_Profile.get_user_details(session['user_id'])
    print(res_user_details)
    res_driver_details = db_Profile.get_driver_details(session['user_id'])
    print(res_driver_details)
    return render_template('Edit_Profile.html', res_user_details=res_user_details, res_driver_details=res_driver_details)

@Edit_Profile.route('/update_details',methods=['GET','POST'])
def update():
    if request.method == 'POST':
        nickname = request.form['nickname']
        user_email = request.form['email']
        phone = request.form['phone']
        kibutz = request.form.get("kibutz")
        profile_pic = request.files["profile_img"]
        profile_pic_db = f"../../static/media/img/users_profile_pic/{session['user_id'] }.jpg"
        if session['driver'] == True:
            license_plate = request.form['license_plate']
            car_company = request.form['car_company']
            car_color = request.form['car_color']
            licence_driver_pic = request.files["licence_driver_img"]
            licence_driver_pic_db = f"../../static/media/img/users_driver_licence_pic/{session['user_id'] }_dl.jpg"
        flag= False
        if len(nickname) >0:
            db_UpdateProfile.change_nickname(nickname,session['user_id'])
            flag= True
        if len(user_email) >0:
            db_UpdateProfile.change_user_email(user_email,session['user_id'])
            flag= True
        if len(phone) >0:
            db_UpdateProfile.change_user_phone(phone,session['user_id'])
            flag= True
        if kibutz != 1:
            Belongs_to_shaar_hanegev = db_Register.check_if_belongs(session['user_id'], kibutz)
            if Belongs_to_shaar_hanegev:
                db_UpdateProfile.change_user_kibutz(kibutz,session['user_id'])
                flag= True
        if profile_pic.filename!='':
            db_UpdateProfile.change_user_profile_pic(profile_pic_db,session['user_id'])
            profile_pic.save(f"static/media/img/users_profile_pic/{session['user_id'] }.jpg")
            session['profile_pic'] = f"static/media/img/users_profile_pic/{session['user_id'] }.jpg"
            flag= True
        if session['driver'] == True:
            if len(license_plate) >0:
                db_UpdateProfile.change_user_license_plate(license_plate,session['user_id'])
                flag= True
            if len(car_company) >0:
                db_UpdateProfile.change_user_car_company(car_company,session['user_id'])
                flag= True
            if len(car_color) >0:
                db_UpdateProfile.change_user_car_color(car_color,session['user_id'])
                flag= True
            if licence_driver_pic.filename != '':
                db_UpdateProfile.change_user_licence_driver_pic(licence_driver_pic_db, session['user_id'])
                licence_driver_pic.save(f"static/media/img/users_driver_licence_pic/{session['user_id'] }_dl.jpg")
                flag = True
        if flag== True:
            res_user_details = db_Profile.get_user_details(session['user_id'])
            if session['driver'] == True:
                res_driver_details = db_Profile.get_driver_details(session['user_id'])
                rank_avg_votes = db_Ranking.get_avg_total(session['user_id'])
                round_avg = round((float(rank_avg_votes[0][0])), 2)
                total_votes = rank_avg_votes[0][1]
                return render_template('Profile.html',message="הפרטים עודכנו בהצלחה!", res_user_details=res_user_details,
                                   res_driver_details=res_driver_details,round_avg=round_avg,total_votes=total_votes)
            else:
                return render_template('Profile.html', message="הפרטים עודכנו בהצלחה!",
                                       res_user_details=res_user_details)
        else:
            return redirect(url_for('Edit_Profile.index'))

