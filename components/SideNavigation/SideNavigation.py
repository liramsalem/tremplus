from flask import Blueprint, render_template

# SideNavigation blueprint definition
SideNavigation = Blueprint('SideNavigation', __name__, static_folder='static', static_url_path='/SideNavigation', template_folder='templates')
