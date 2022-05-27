from flask import Blueprint, render_template, redirect, url_for,request, session
from utilities.db.db_Profile import db_Profile
from utilities.db.db_UpdateProfile import db_UpdateProfile

# ChangePassword blueprint definition
ChangePassword = Blueprint('ChangePassword', __name__, static_folder='static', static_url_path='/ChangePassword', template_folder='templates')


# Routes
@ChangePassword.route('/ChangePassword')
def index():
    return render_template('ChangePassword.html')

@ChangePassword.route('/update_password',methods=['GET','POST'])
def update_psw():
    if request.method == 'POST':
        current_psw= request.form['current_psw']
        new_psw= request.form['new_psw']
        confirm_psw= request.form['confirm_psw']
        db_psw= db_Profile.get_user_psw(session['user_id'])
        if db_psw[0].password==current_psw:
            if new_psw==confirm_psw:
                db_UpdateProfile.change_user_password(new_psw, session['user_id'])
                return render_template('ChangePassword.html', message="הסיסמא שונתה בהצלחה!")
            else:
                return render_template('ChangePassword.html', message="אימות הסיסמאות אינו צלח, אנא נסה/י שנית")
        else:
            return render_template('ChangePassword.html',message="הסיסמא אינה נכונה")


