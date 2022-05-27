from flask import Blueprint, render_template, redirect, url_for,request, session
from utilities.db.db_SignIn import db_SignIn

# SignIn blueprint definition
SignIn = Blueprint('SignIn', __name__, static_folder='static', static_url_path='/SignIn', template_folder='templates')


# Routes
@SignIn.route('/SignIn')
def index():
    return render_template('SignIn.html')

@SignIn.route('/SignIn_form',methods=['GET','POST'])
def sign_req():
    if request.method == 'POST':
        user_email = request.form.get('email')
        password = request.form.get('psw')
        found = db_SignIn.check_user(user_email, password)
        if found and len(found):
            session['logged_in'] = True
            session['user_email'] = found[0].user_email
            session['user_name'] = found[0].Fname
            session['user_Lname'] = found[0].Lname
            session['user_id'] = found[0].user_id
            session['profile_pic'] = found[0].profile_pic
            session['user_serial_num'] = found[0].user_serial_num
            driver = db_SignIn.check_if_user_is_driver(session['user_id'])
            if driver:
                session['driver'] = True
            else:
                session['driver'] = False
            return redirect(url_for('Home.index'))
        else:
            return render_template('SignIn.html', message="האימייל או הסיסמה שהזנת שגויים ! נא לנסות שוב")

@SignIn.route('/LogOut')
def log_out_func():
    session['logged_in'] = False
    session['user_email']= ''
    session['user_name']= ''
    session['user_id'] = ''
    return redirect(url_for('OpenScreen.index'))

