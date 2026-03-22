
# Models

from flask_sqlalchemy import SQLAlchemy      # pyright: ignore[reportMissingImports]
db= SQLAlchemy()

class User(db.Model):
    __tablename__='user'
    user_id=db.Column(db.Integer,primary_key=True, autoincrement=True)
    user_email=db.Column(db.String(200),unique=True, nullable=False)
    user_name= db.Column(db.String(100))
    user_password=db.Column(db.String(200), nullable=False)

    role_id=db.Column(db.Integer, db.ForeignKey('role.id'))
    role=db.relationship('Role', backref='users')
    status=db.Column(db.Integer, default=1)         #   1 active and 0 blacklist 2 pending

class Role(db.Model):
    __tablename__='role'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)


class PlacementsDrives(db.Model):
    __tablename__='placements_drives'
    drive_id=db.Column(db.Integer,nullable=False, primary_key=True, autoincrement=True)
    company_id=db.Column(db.Integer,nullable=False)
    job_title=db.Column(db.String(200), nullable=False)
    job_description=db.Column(db.String(2000))
    branch=db.Column(db.String(50))
    cgpa=db.Column(db.Float)
    year=db.Column(db.Integer)
    applicatin_deadline=db.Column(db.Date)
    status=db.Column(db.Integer, default=1)        #0 / 1 Active / 0 Closed



class Applications(db.Model):
    __tablename__='applications'
    application_id=db.Column(db.Integer, primary_key=True)
    student_id=db.Column(db.Integer,nullable=False)
    drive_id=db.Column(db.Integer,db.ForeignKey('placements_drives.drive_id'))
    application_date=db.Column(db.Date)
    status=db.Column(db.Integer, default=0)        #0 Applied / 1 Shortlisted / 2 Selected / 3 Rejected



class CompanyProfile(db.Model):
    __tablename__='company_profile'
    company_id=db.Column(db.Integer,primary_key=True)
    company_name=db.Column(db.String)
    hr_contact=db.Column(db.Integer)
    website=db.Column(db.String(100))
    approval_status=db.Column(db.Integer, default=0)    

