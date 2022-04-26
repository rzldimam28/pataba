from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
  email = StringField('User Name', validators=[DataRequired()])
  password = PasswordField('Password', validators=[DataRequired()])
  submit = SubmitField('Sign in')

class EditTableForm(FlaskForm):
  tahun = IntegerField('Tahun', validators=[DataRequired()])
  col1 = IntegerField('Col1')
  col2 = IntegerField('Col2')
  col3 = IntegerField('Col3')
  district_id = SelectField('Kecamatan', choices=[(None, 'Kota Palu'), (1, 'Palu Barat'), (2, 'Palu Selatan'), (3, 'Tatanga'), (4, 'Ulujadi'), (5, 'Mantikulore'), (6, 'Palu Timur'), (7, 'Palu Utara'), (8, 'Tawaili')])
  submit = SubmitField('Submit')
  
