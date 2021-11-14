from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, RadioField
from wtforms.validators import InputRequired
import json

class OrderForm(FlaskForm):
    """
    <!--Full Name-->
    <!--Phone Number-->
    <!--Email-->
    <!--Country-->
    <!--Address-->
    <!--Paying method-->
    """
    fname = StringField('First Name', validators=[ InputRequired()])
    lname = StringField('Last Name', validators=[ InputRequired()])
    email = EmailField('Email', validators=[ InputRequired()])
    phoneNum = StringField('Phone number', validators=[ InputRequired()])
    address = StringField('Address', validators=[ InputRequired()])
    method = RadioField('Payment method', choices=[
        ("cash", "Cash"),
        ("online", "Online"),
    ], default="cash")

    def __jsonify__(self):
        return json.dumps(self.data, indent=4)