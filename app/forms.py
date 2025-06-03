from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, TextAreaField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class ToiletForm(FlaskForm):
    name = StringField('Toilet Name', validators=[DataRequired()])
    location = StringField('Address')
    lat = FloatField('Latitude', validators=[DataRequired()])
    lon = FloatField('Longitude', validators=[DataRequired()])
    submit = SubmitField('Add Toilet')

class ReviewForm(FlaskForm):
    cleanliness = IntegerField('Cleanliness (1-5)', validators=[NumberRange(min=1, max=5)])
    safety = IntegerField('Safety (1-5)', validators=[NumberRange(min=1, max=5)])
    smell = IntegerField('Smell (1-5)', validators=[NumberRange(min=1, max=5)])
    comment = TextAreaField('Comment')
    submit = SubmitField('Submit Review')

class PoopStoryForm(FlaskForm):
    title = StringField('Story Title', validators=[DataRequired()])
    content = TextAreaField('What happened?', validators=[DataRequired()])
    submit = SubmitField('Share Story')
