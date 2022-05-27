from flask import Blueprint, render_template

# ImportantPhones blueprint definition
ImportantPhones = Blueprint('ImportantPhones', __name__, static_folder='static', static_url_path='/ImportantPhones', template_folder='templates')


# Routes
@ImportantPhones.route('/ImportantPhones')
def index():
    return render_template('ImportantPhones.html')
