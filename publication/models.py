from publication import db, bcrypt, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

class Districts(db.Model):
  id = db.Column(db.Integer(), primary_key=True)
  name = db.Column(db.String(), nullable=False)
  # type
  user = db.relationship('Users', backref='district_owned_user', lazy=True)

class Agencies(db.Model):
  id = db.Column(db.Integer(), primary_key=True)
  name = db.Column(db.String(), nullable=False)
  # type
  user = db.relationship('Users', backref='agencies_owned_user', lazy=True)

class Users(db.Model, UserMixin):
  id = db.Column(db.Integer(), primary_key=True)
  email = db.Column(db.String(), unique=True, nullable=False)
  password_hash = db.Column(db.String(), nullable=False)
  name = db.Column(db.String(), nullable=False)
  role = db.Column(db.String(), nullable=False)
  officer_of_district = db.Column(db.Integer(), db.ForeignKey('districts.id'), nullable=True)
  officer_of_agency = db.Column(db.Integer(), db.ForeignKey('agencies.id'), nullable=True)

  @property
  def password(self):
    return self.password
  
  @password.setter
  def password(self, plain_text_password):
    self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')
    
  def check_password_correction(self, attempted_password):
    return bcrypt.check_password_hash(self.password_hash, attempted_password)

class DinasA(db.Model):
  id = db.Column(db.Integer(), primary_key=True)
  tahun = db.Column(db.String(length=4), nullable=False)
  col1 = db.Column(db.Integer())
  col2 = db.Column(db.Integer())
  col3 = db.Column(db.Integer())
  district_id = db.Column(db.Integer(), db.ForeignKey('districts.id'), nullable=True)

class DinasB(db.Model):
  id = db.Column(db.Integer(), primary_key=True)
  tahun = db.Column(db.String(length=4), nullable=False)
  col1 = db.Column(db.Integer())
  col2 = db.Column(db.Integer())
  col3 = db.Column(db.Integer())
  district_id = db.Column(db.Integer(), db.ForeignKey('districts.id'), nullable=True)
