from flask import Flask
# from flask_mail import Mail, Message

###### App setup
app = Flask(__name__)
app.config.from_pyfile('settings.py')
# app.config['MAIL_SERVER'] = 'smtp.outlook.com'
# app.config['MAIL_PORT'] = 587
# app.config['MAIL_USERNAME'] = 'tremplus@outlook.com'
# app.config['MAIL_PASSWORD'] = 'Tt123456789'
# app.config['MAIL_USE_TLS'] = False
# app.config['MAIL_USE_SSL'] = True
# mail = Mail(app)

###### Pages

##OpenScreen
from pages.OpenScreen.OpenScreen import OpenScreen
app.register_blueprint(OpenScreen)

## Homepage
from pages.Home.Home import Home
app.register_blueprint(Home)

## SignIn
from pages.SignIn.SignIn import SignIn
app.register_blueprint(SignIn)

## Register
from pages.Register.Register import Register
app.register_blueprint(Register)

## Profile
from pages.Profile.Profile import Profile
app.register_blueprint(Profile)

## Edit_Profile
from pages.Edit_Profile.Edit_Profile import Edit_Profile
app.register_blueprint(Edit_Profile)

## ChangePassword
from pages.ChangePassword.ChangePassword import ChangePassword
app.register_blueprint(ChangePassword)

## NewDrive
from pages.NewDrive.NewDrive import NewDrive
app.register_blueprint(NewDrive)

## Search
from pages.Search.Search import Search
app.register_blueprint(Search)

## MyRides
from pages.MyRides.MyRides import MyRides
app.register_blueprint(MyRides)

## ImportantPhones
from pages.ImportantPhones.ImportantPhones import ImportantPhones
app.register_blueprint(ImportantPhones)

## RideDetails
from pages.RideDetails.RideDetails import RideDetails
app.register_blueprint(RideDetails)

## UserDetails
from pages.UserDetails.UserDetails import UserDetails
app.register_blueprint(UserDetails)

## RideDetailsForDriver
from pages.RideDetailsForDriver.RideDetailsForDriver import RideDetailsForDriver
app.register_blueprint(RideDetailsForDriver)

## DrivesHistory
from pages.DrivesHistory.DrivesHistory import DrivesHistory
app.register_blueprint(DrivesHistory)

## RankingUser
from pages.RankingUser.RankingUser import RankingUser
app.register_blueprint(RankingUser)

## MsgToUser
from pages.MsgToUser.MsgToUser import MsgToUser
app.register_blueprint(MsgToUser)


## Page error handlers
from pages.page_error_handlers.page_error_handlers import page_error_handlers
app.register_blueprint(page_error_handlers)


###### Components
## header
from components.header.header import header
app.register_blueprint(header)

## SideNavigation
from components.SideNavigation.SideNavigation import SideNavigation
app.register_blueprint(SideNavigation)


