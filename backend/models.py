
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

    cp=db.relationship('CompanyProfile', backref='usr_c',uselist=False,cascade="all, delete-orphan")
    sp=db.relationship('StudentProfile', backref='usr_s',uselist=False,cascade="all, delete-orphan")

class Role(db.Model):
    __tablename__='role'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)


class PlacementsDrives(db.Model):
    __tablename__='placements_drives'
    drive_id=db.Column(db.Integer,nullable=False, primary_key=True, autoincrement=True)
    company_id=db.Column(db.Integer,db.ForeignKey('company_profile.company_id', ondelete='CASCADE') ,nullable=False)
    job_title=db.Column(db.String(200), nullable=False)
    job_description=db.Column(db.String(2000))
    branch=db.Column(db.String(50))
    cgpa=db.Column(db.Integer)
    year=db.Column(db.Integer)
    application_deadline=db.Column(db.Date)
    status=db.Column(db.Integer, default=0)        #0 / 1 approved / 0 waiting for admin action

    company=db.relationship('CompanyProfile', backref='drives')
    applications=db.relationship('Applications', backref='drive_p', cascade="all, delete-orphan")





class Applications(db.Model):
    __tablename__='applications'
    application_id=db.Column(db.Integer, primary_key=True,autoincrement=True)
    student_id=db.Column(db.Integer, db.ForeignKey('student_profile.student_id', ondelete='CASCADE'),nullable=False)
    drive_id=db.Column(db.Integer,db.ForeignKey('placements_drives.drive_id', ondelete='CASCADE'), nullable=False)
    application_date=db.Column(db.Date)
    status=db.Column(db.Integer, default=0)        #0 Applied / 1 Shortlisted / 2 Selected / 3 Rejected

class StudentProfile(db.Model):
    __tablename__='student_profile'
    student_id=db.Column(db.Integer,db.ForeignKey('user.user_id'),primary_key=True)
    resume_path=db.Column(db.String)
    phone_no=db.Column(db.String(14))
    address=db.Column(db.String(100))
    social_profile=db.Column(db.String(200))

    application=db.relationship('Applications', backref='student_p', cascade="all, delete-orphan")


class CompanyProfile(db.Model):
    __tablename__='company_profile'
    company_id=db.Column(db.Integer,db.ForeignKey('user.user_id'),primary_key=True)
    # company_name=db.Column(db.String(100))
    company_description=db.Column(db.String(1000))
    hr_contact=db.Column(db.String(20))
    website=db.Column(db.String(100))
    # approval_status=db.Column(db.Integer, default=0)  

    # drive=db.relationship('PlacementsDrives', backref='company_p')


