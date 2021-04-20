from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, Optional, URL

class CupcakeForm(FlaskForm):
    """Form for adding/updating cupcakes."""

    flavor = StringField('Flavor', validators=[InputRequired()])
    size = StringField('Size', validators=[InputRequired()])
    rating = IntegerField('Rating', validators=[InputRequired()])
    image = StringField('Image URL', validators=[Optional(), URL(message="Invalid image url.")])