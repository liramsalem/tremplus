from flask import Blueprint, render_template, redirect, url_for,request, session
from utilities.db.db_Register import *
from cloudinary.uploader import upload
from utilities.db.db_UpdateProfile import db_UpdateProfile
from cloudinary.utils import cloudinary_url


# Register blueprint definition
Register = Blueprint('Register', __name__, static_folder='static', static_url_path='/Register', template_folder='templates')


# Routes
@Register.route('/Register')
def index():
    return render_template('Register.html')


@Register.route('/Register_form',methods=['GET','POST'])
def register_form():
    if request.method == 'POST':
        Fname = request.form['firstnm']
        Lname = request.form['lastnm']
        nickname = request.form['nickname']
        kibutz = request.form.get("kibutz")
        user_id = request.form['id']
        phone = request.form['phone']
        user_email = request.form['email']
        password = request.form['psw']
        profile_pic = request.files["img"]
        profile_pic_db = ""
        profile_pic_dif= f"Register/media/profile.png"
        chaked = request.form.get("myCheck")
        license_plate = request.form['license_plate']
        car_company = request.form['car_company']
        car_color = request.form['car_color']
        licence_driver_pic = request.files["licence_driver_img"]
        licence_driver_pic_db = ""
        found = db_Register.check_user_exists(user_id)
        if found:
            return render_template('Register.html',message="הינך כבר רשום במערכת!")
        else:
            # Belongs_to_shaar_hanegev=db_Register.check_if_belongs(user_id,kibutz) #במידה ורוצים להפעיל הגבלת ישובים!!
            # if Belongs_to_shaar_hanegev:
                if chaked == 'on':
                    if profile_pic.filename != '':
                        if db_Register.insert_user(Fname, Lname, nickname, kibutz, user_id, phone, user_email, password, profile_pic_db) > 0:
                            upload_obj = upload(profile_pic, public_id=f"users_profile_pic/{user_id}")
                            db_UpdateProfile.change_user_profile_pic(upload_obj['secure_url'], user_id)
                            return render_template('SignIn.html', message="נרשמת בהצלחה! על מנת להתחיל להשתמש יש להתחבר תחילה")
                        else:
                            return render_template('Register.html', message="חלה שגיאה, אנא נסה/י להירשם מחדש")
                    else:
                        if db_Register.insert_user(Fname, Lname, nickname, kibutz, user_id, phone, user_email, password, profile_pic_dif) > 0:
                            return render_template('SignIn.html', message="נרשמת בהצלחה! על מנת להתחיל להשתמש יש להתחבר תחילה")
                        else:
                            return render_template('Register.html', message="חלה שגיאה, אנא נסה/י להירשם מחדש")
                else:
                        if profile_pic.filename != '':
                            if db_Register.insert_user(Fname, Lname, nickname, kibutz, user_id, phone, user_email, password, profile_pic_db) > 0:
                                upload_obj = upload(profile_pic, public_id=f"users_profile_pic/{user_id}")
                                db_UpdateProfile.change_user_profile_pic(upload_obj['secure_url'],user_id)
                                serial_num= db_Register.get_user_serial_num(user_id)
                                if db_Register.insert_driver(user_id,Fname, Lname, license_plate, car_company, car_color,licence_driver_pic_db,serial_num) > 0 and db_Register.insert_driver_to_ranking(user_id) >0:
                                    upload_obj = upload(licence_driver_pic, public_id=f"users_driver_licence_pic/{user_id}_dl")
                                    db_UpdateProfile.change_user_licence_driver_pic(upload_obj['secure_url'],user_id)
                                    return render_template('SignIn.html', message="נרשמת בהצלחה! על מנת להתחיל להשתמש יש להתחבר תחילה")
                                else:
                                    return redirect(url_for('Home.index'))
                            else:
                                return render_template('Register.html', message="חלה שגיאה, אנא נסה/י להירשם מחדש")
                        else:
                            if db_Register.insert_user(Fname, Lname, nickname, kibutz, user_id, phone, user_email, password,profile_pic_dif) > 0:
                                serial_num= db_Register.get_user_serial_num(user_id)
                                if db_Register.insert_driver(user_id,Fname, Lname, license_plate, car_company, car_color,licence_driver_pic_db,serial_num) > 0 and db_Register.insert_driver_to_ranking(user_id) >0:
                                    upload_obj = upload(licence_driver_pic, public_id=f"users_driver_licence_pic/{user_id}_dl")
                                    db_UpdateProfile.change_user_licence_driver_pic(upload_obj['secure_url'], user_id)
                                    return render_template('SignIn.html', message="נרשמת בהצלחה! על מנת להתחיל להשתמש יש להתחבר תחילה")
                                else:
                                    return redirect(url_for('Home.index'))
                            else:
                                return render_template('Register.html', message="חלה שגיאה, אנא נסה/י להירשם מחדש")

            # else:
            #     return render_template('Register.html', message="אנו מצטערים, TREMPLUS מיועדת לתושבי מועצה אזורית שער הנגב.")


