from flask import Blueprint, render_template

# MsgToUser blueprint definition
MsgToUser = Blueprint('MsgToUser', __name__, static_folder='static', static_url_path='/MsgToUser', template_folder='templates')


# Routes
@MsgToUser.route('/MsgToUser')
def index():
    return render_template('MsgToUser.html',message="הדירוג התקבל בהצלחה!")
