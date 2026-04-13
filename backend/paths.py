from flask_restful import Resource, Api        # pyright: ignore[reportMissingImports]
from flask import request, jsonify, send_file                # pyright: ignore[reportMissingImports]
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity      # pyright: ignore[reportMissingImports]
from werkzeug.security import generate_password_hash, check_password_hash      # pyright: ignore[reportMissingImports]

from models import db, User, Role, PlacementsDrives, StudentProfile, Applications, CompanyProfile

from datetime import datetime
import os
from flask_caching import Cache             # pyright: ignore[reportMissingImports]

# from mail_server import send_email

api=Api()
cache= Cache()


#UNIQUE STRING__________________
def unique_str():
    str=datetime.now().strftime('%Y%m%d%H%M%S%f')
    return str


# ________________________________________________________________________

# IMPORTANT ALL API ENDPOINTS HERE

# GET /
# POST /register
# POST /login

# POST /drives
# GET /drives
# GET /drives/<int:drive_id>
# POST /apply_drive/<int:drive_id>
# PATCH /approve_drive/<int:drive_id>
# DELETE /admin/remove_drive/<int:drive_id>

# GET /company_profile/<int:company_id>
# POST /company/profile
# GET /company/drives

# GET /company/dashboard_stats
# GET /company/drive_applications/<int:drive_id>
# PATCH /company/application_status/<int:application_id>
# GET /company/application_resume/<int:application_id>
# GET /company/shortlisted_students
# GET /company_application
# GET /admin/registered_company
# DELETE /admin/remove_company/<int:company_id>
# GET /admin/registered_students
# GET /admin/student_applications
# DELETE /admin/remove_student/<int:student_id>
# GET /student_profile
# PUT /student_profile
# GET /student_profile/resume
# GET /student/applications
# PATCH /approve_application/<int:company_id>
# GET /admin/dashboard_stats
# GET /admin/hired_students
# GET /admin/drive_applications/<int:drive_id>




# END OF LISTING API ENDPOINTS
# ______________________________________________________________________________________



#decorder for Admin

# def admin(fun):
#     # @wraps(fun)
#     def wrapper(*args,**kwargs):
#         email=get_jwt_identity()
        
#         user=User.query.filter_by(user_email=email).first()

#         if not user:
#             return {"message":"no user"},404

#         if user.role.name=='admin':
#             fun()
#         else:
#             return {"message":"unauthorised access"},403
        
        

#     return wrapper




# home ___________________

class Home(Resource):
    def get(self):
        return {"message":"connection successful"}, 200
    
api.add_resource(Home,"/") 


# Auth logic______________________________

class Register(Resource):           #abhi registration risky h, logic will add later
    def post(self):
        data=request.get_json()
        if not data:
            return {"message":"invalid request body"},400
        is_user_exist=User.query.filter_by(user_email=data['email']).first()
        # print(is_user_exist)
        if is_user_exist:
            return {"message":"user exist"},409
        
        role=Role.query.filter_by(name=data['role']).first()
        if not role:
            return {"message":"invalid role"},400
        

        
        if data['role'] =='student' :
            user=User(user_name=data['name'],user_email=data['email'],user_password=generate_password_hash(data['password']),role=role)
            db.session.add(user)
            db.session.commit()
            return {"message":"user registered successfully"},200
        else :
            user=User(user_name=data['name'],user_email=data['email'],user_password=generate_password_hash(data['password']),role=role, status=2)
            db.session.add(user)
            db.session.commit()
            return {"message":"registration successful, wait for your application to be approved by the admin"},200
        
api.add_resource(Register,'/register')


class Login(Resource):
    def post(self):
        data=request.get_json()

        is_user=User.query.filter_by(user_email=data['email']).first()
        if not is_user:
            return {'message':'invalid email or password'},401
        if not check_password_hash(is_user.user_password, data['password']):
            return {'message':'invalid email or password'},401
        if is_user and is_user.status==2:
            return {'message':'your application is not approved yet, once it approved you can login'},401

            # IMPORTANT TOKEN CREATION KIYA H
        access_token=create_access_token(identity=is_user.user_email)
        return {"message": "user logged in successfully","access_token":access_token,"user_id":is_user.user_id,"email":is_user.user_email,"role":is_user.role.name,"user_name":is_user.user_name},200
    
api.add_resource(Login ,'/login')

# __________________________END auth logic
    


# POST and GET for placement drives_________________

class PlacementDrive(Resource):
    @jwt_required()
    def post(self):
        data=request.get_json()
        if not data:
            return {"message": "invalid request body"}, 400

        user_email = get_jwt_identity()
        current_user = User.query.filter_by(user_email=user_email).first()
        if not current_user or current_user.role.name != 'company':
            return {"message": "not authorized"}, 403
        
        deadline_str = data.get("application_deadline")
        if not deadline_str:
            return {"message": "application_deadline is required"}, 400

        try:
            deadline_date = datetime.strptime(deadline_str, "%Y-%m-%d").date()
        except ValueError:
            return {"message": "application_deadline must be in YYYY-MM-DD format"}, 400

        drive_data=PlacementsDrives(
            company_id=current_user.user_id,
            job_title=data['job_title'],
            job_description=data['job_description'],
            branch=data['branch'],
            cgpa=data['cgpa'],
            year=data['year'],
            application_deadline=deadline_date
        )
        db.session.add(drive_data)
        db.session.commit()
        return {'message':'added successfully'}
    

    @jwt_required()
    # @cache.cached(timeout=10)
    def get(self, drive_id=None):
        if drive_id is not None:
            drive = PlacementsDrives.query.get(drive_id)
            if not drive:
                return {"message": "drive not found"}, 404
            return {
                "drive_id": drive.drive_id,
                "company_id": drive.company_id,
                "job_title": drive.job_title,
                "job_description": drive.job_description,
                "branch": drive.branch,
                "cgpa": drive.cgpa,
                "year": drive.year,
                "application_deadline": drive.application_deadline.isoformat(),
                "status": drive.status
            }, 200

        data = PlacementsDrives.query.all()
        result = []
        for drive in data:
            result.append({
                "drive_id": drive.drive_id,
                "company_id": drive.company_id,
                "job_title": drive.job_title,
                "job_description": drive.job_description,
                "branch": drive.branch,
                "cgpa": drive.cgpa,
                "year": drive.year,
                "application_deadline": drive.application_deadline.isoformat(),
                "status": drive.status
            })
        
        search = request.args.get('search', '').strip().lower()
        if search:
            result = [
                row for row in result
                if search in str(row.get('drive_id', '')).lower()
                or 
                # search in str(row.get('company_id', '')).lower()
                # or 
                search in str(row.get('job_title', '')).lower()
                or 
                search in str(row.get('job_description','')).lower()
                or
                search in str(row.get('branch','')).lower()
                or
                search in str(row.get('cgpa','')).lower()
                or
                search in str(row.get('year','')).lower()
                or
                search in str(row.get('application_deadline','')).lower()

                
            ]
        
        return jsonify(result)
api.add_resource(PlacementDrive,'/drives','/drives/<int:drive_id>')


class ApplyPlacementDrive(Resource):
    @jwt_required()
    def post(self, drive_id):
        user_email = get_jwt_identity()
        current_user = User.query.filter_by(user_email=user_email).first()
        if not current_user or current_user.role.name != 'student':
            return {"message": "not authorized"}, 403

        drive = PlacementsDrives.query.get(drive_id)
        if not drive:
            return {"message": "drive not found"}, 404

        if drive.status != 1:
            return {"message": "drive is not approved yet"}, 400

        if drive.application_deadline and drive.application_deadline < datetime.now().date():
            return {"message": "application deadline is over"}, 400

        if not current_user.sp:
            return {"message": "update student profile before applying"}, 400

        is_already_applied = Applications.query.filter_by(
            student_id=current_user.user_id,
            drive_id=drive_id
        ).first()
        if is_already_applied:
            return {"message": "already applied"}, 409

        app_data = Applications(
            student_id=current_user.user_id,
            drive_id=drive_id,
            application_date=datetime.now().date(),
        )
        db.session.add(app_data)
        db.session.commit()
        return {"message": "applied successfully"}, 200


api.add_resource(ApplyPlacementDrive, '/apply_drive/<int:drive_id>')


class ApproveDrive(Resource):
    @jwt_required()
    # @admin
    def patch(self,drive_id):
        data=request.get_json()
        if not data:
            return {'message': 'invalid request body'}, 400

        user_email = get_jwt_identity()
        current_user = User.query.filter_by(user_email=user_email).first()
        if not current_user or current_user.role.name != 'admin':
            return {'message': 'not authorized'}, 403

        drive=PlacementsDrives.query.get(drive_id)
        if not drive:
            return {'message':'drive does not exist'},404

        if 'status' not in data:
            return {'message': 'status is required'}, 400

        if data['status'] not in [0, 1]:
            return {'message': 'invalid status'}, 400

        drive.status=data['status']
        db.session.commit()

        return {'message':'drive updated successfully'},200
api.add_resource(ApproveDrive,'/approve_drive/<int:drive_id>')


class RemoveDrive(Resource):
    @jwt_required()
    def delete(self, drive_id):
        user_email = get_jwt_identity()
        current_user = User.query.filter_by(user_email=user_email).first()
        if not current_user or current_user.role.name != 'admin':
            return {'message': 'not authorized'}, 403

        drive = PlacementsDrives.query.get(drive_id)
        if not drive:
            return {'message': 'drive not found'}, 404

        Applications.query.filter_by(drive_id=drive_id).delete()
        db.session.delete(drive)
        db.session.commit()
        return {'message': 'drive removed successfully'}, 200


api.add_resource(RemoveDrive, '/admin/remove_drive/<int:drive_id>')

#____________________________END of placement drive section







# Company ___________________________




class ComProfile(Resource):
    @jwt_required()
    def get(self,company_id):
        # email=get_jwt_identity()
        # curr_usr= User.query.filter_by(user_email=)
        # NOT RESTRICTED TO ONLY FOR COMPANY OTHER ROLES ALSO BE ABLE TO GET COMPANY PROFILE
        company=CompanyProfile.query.get(company_id)
        if company:
            return {
                "company_id":company.company_id,
                "company_description":company.company_description,
                "hr_no":company.hr_contact,
                "website":company.website
            }
        return {"message":"not found"}


    @jwt_required()
    def put(self):
        email = get_jwt_identity()
        curr_usr = User.query.filter_by(user_email=email).first()

        if not curr_usr or curr_usr.role.name != 'company':
            return {"message": "not authorized"}, 403

        data = request.get_json()

        profile = CompanyProfile.query.filter_by(company_id=curr_usr.user_id).first()

        if not profile:
            profile = CompanyProfile(company_id=curr_usr.user_id)
            db.session.add(profile)

        profile.company_description = data.get('company_description')
        profile.hr_contact = data.get('hr_no')
        profile.website = data.get('website')

        db.session.commit()

        return {"message": "update successful"}, 200
    

api.add_resource(ComProfile,'/company_profile/<int:company_id>','/company/profile')








class CompanyDrives(Resource):
    @jwt_required()
    # @cache.cached(timeout=10)
    def get(self):
        user_email = get_jwt_identity()
        current_user = User.query.filter_by(user_email=user_email ).first()
        if not current_user or current_user.role.name != 'company':
            return {"message": "not authorized"}, 403

        data = PlacementsDrives.query.filter_by(company_id=current_user.user_id).all()
        result = []
        for drive in data:
            result.append({
                "drive_id": drive.drive_id,
                "company_id": drive.company_id,
                "job_title": drive.job_title,
                "job_description": drive.job_description,
                "branch": drive.branch,
                "cgpa": drive.cgpa,
                "year": drive.year,
                "application_deadline": drive.application_deadline.isoformat(),
                "status": drive.status
            })

        search = request.args.get('search', '').strip().lower()
        if search:
            result = [
                row for row in result
                if search in str(row.get('drive_id', '')).lower()
                or 
                search in str(row.get('job_title', '')).lower()
                or 
                search in str(row.get('job_description', '')).lower()
                
            ]

        return jsonify(result)


api.add_resource(CompanyDrives, '/company/drives')



# counts____________________________________________________-
# company dashboard ka

class CompanyDashboardStats(Resource):
    @jwt_required()
    def get(self):
        user_email = get_jwt_identity()
        current_user = User.query.filter_by(user_email=user_email).first()
        if not current_user or current_user.role.name != 'company':
            return {"message": "not authorized"}, 403

        company_profile = CompanyProfile.query.get(current_user.user_id)
        drives = PlacementsDrives.query.filter_by(company_id=current_user.user_id).all()

        drives_data = []
        total_applicants = 0
        for drive in drives:
            applicants_count = Applications.query.filter_by(drive_id=drive.drive_id).count()
            total_applicants += applicants_count
            drives_data.append({
                "drive_id": drive.drive_id,
                
                "applicants_count": applicants_count,
            })

        return {
            
            "total_drives": len(drives_data),
            "total_applicants": total_applicants,
            "company_profile": drives_data,
        }, 200


api.add_resource(CompanyDashboardStats, '/company/dashboard_stats')


class CompanyDriveApplications(Resource):
    @jwt_required()
    def get(self, drive_id):
        user_email = get_jwt_identity()
        current_user = User.query.filter_by(user_email=user_email).first()
        if not current_user or current_user.role.name != 'company':
            return {"message": "not authorized"}, 403

        drive = PlacementsDrives.query.get(drive_id)
        if not drive:
            return {"message": "drive not found"}, 404

        if drive.company_id != current_user.user_id:
            return {"message": "not authorized"}, 403

        applications = Applications.query.filter_by(drive_id=drive_id).all()
        result = []
        for app in applications:
            student_user = User.query.get(app.student_id)
            student_profile = StudentProfile.query.get(app.student_id)
            result.append({
                "application_id": app.application_id,
                "drive_id": app.drive_id,
                "student_id": app.student_id,
                "student_name": student_user.user_name if student_user else None,
                "student_email": student_user.user_email if student_user else None,
                "resume_path": student_profile.resume_path if student_profile else None,
                "application_date": app.application_date.isoformat() if app.application_date else None,
                "status": app.status,
            })

        search = request.args.get('search', '').strip().lower()
        if search:
            result = [
                row for row in result
                if search in str(row.get('application_id', '')).lower()
                or 
                search in str(row.get('student_id', '')).lower()
                or 
                search in str(row.get('student_name', '')).lower()
                or 
                search in str(row.get('student_email', '')).lower()
                
            ]

        return jsonify(result)


api.add_resource(CompanyDriveApplications, '/company/drive_applications/<int:drive_id>')


# company is shortlisting student or changing status of student application
# application for drives



# note: celery
# here


class CompanyApplicationStatus(Resource):
    @jwt_required()
    def patch(self, application_id):
        user_email = get_jwt_identity()
        current_user = User.query.filter_by(user_email=user_email).first()
        if not current_user or current_user.role.name != 'company':
            return {"message": "not authorized"},403

        application = Applications.query.get(application_id)
        if not application:
            return {"message": "application not found"},404

        drive = PlacementsDrives.query.get(application.drive_id)
        if not drive:
            return {"message": "getting err while fetching drives"},404

        if drive.company_id != current_user.user_id:
            return {"message": "you are not authorized"},403

         # just checking till here

        # getting json
        # patch request

        data = request.get_json()
        if "status" not in data:
            return {"message": "status is required"},400

        try:
            status = int(data["status"])
        except (TypeError, ValueError):
            return {"message": "status must be an integer"},400

        if status not in (1, 2, 3):
            return {"message": "invalid status"},400

        previous_status = application.status
        application.status = status
        db.session.commit()

# ____________________________________________________________________

#       celery implemented here 
#       importing email_task

# _____________________________________________________________________

        if status == 1 and previous_status != 1:
            
            from mail_server import shortlisted_mail
            shortlisted_mail.delay(application.application_id)
            return {"message":"application status updated to shortlised; sheduled a mail successfully"}
    
        if status==2 and previous_status !=2:
            from mail_server import hire_mail
            hire_mail.delay(application_id)
            return {"message":"applicant hired; mail sending sheduled "}
        return {"message": "application status updated successfully"},200
api.add_resource(CompanyApplicationStatus, '/company/application_status/<int:application_id>')


class CompanyApplicationResume(Resource):
    @jwt_required()
    def get(self, application_id):
        user_email = get_jwt_identity()
        current_user = User.query.filter_by(user_email=user_email).first()
        if not current_user or current_user.role.name != 'company':
            return {"message": "not authorized"}, 403

        application = Applications.query.get(application_id)
        if not application:
            return {"message": "application not found"}, 404

        drive = PlacementsDrives.query.get(application.drive_id)
        if not drive:
            return {"message": "drive not found"}, 404

        if drive.company_id != current_user.user_id:
            return {"message": "not authorized"}, 403

        student_profile = StudentProfile.query.get(application.student_id)
        if not student_profile or not student_profile.resume_path:
            return {"message": "resume not found"}, 404

        resume_path = student_profile.resume_path
        if not os.path.exists(resume_path):
            return {"message": "resume file missing on server"}, 404

        return send_file(
            resume_path,
            mimetype='pdf',
            as_attachment=False,
            download_name=f'resume_{application.student_id}.pdf'
        )


api.add_resource(CompanyApplicationResume, '/company/application_resume/<int:application_id>')


class CompanyShortlistedStudents(Resource):
    @jwt_required()
    # @cache.cached(timeout=10)
    def get(self):
        user_email = get_jwt_identity()
        current_user = User.query.filter_by(user_email=user_email).first()
        if not current_user or current_user.role.name != 'company':
            return {"message": "not authorized"}, 403

        drives = PlacementsDrives.query.filter_by(company_id=current_user.user_id).all()
        drive_ids = [drive.drive_id for drive in drives]
        if not drive_ids:
            return jsonify([])

        apps = Applications.query.filter(
            Applications.drive_id.in_(drive_ids),
            Applications.status == 1
        ).all()

        result = []
        for app in apps:
            drive = PlacementsDrives.query.get(app.drive_id)
            student_user = User.query.get(app.student_id)
            student_profile = StudentProfile.query.get(app.student_id)
            result.append({
                "application_id": app.application_id,
                "drive_id": app.drive_id,
                "job_title": drive.job_title if drive else None,
                "student_id": app.student_id,
                "student_name": student_user.user_name if student_user else None,
                "student_email": student_user.user_email if student_user else None,
                "resume_path": student_profile.resume_path if student_profile else None,
                "application_date": app.application_date.isoformat() if app.application_date else None,
                "status": app.status,
            })

        search = request.args.get('search', '').strip().lower()
        if search:
            result = [
                row for row in result
                if search in str(row.get('application_id', '')).lower()
                or 
                search in str(row.get('drive_id', '')).lower()
                or 
                search in str(row.get('job_title', '')).lower()
                or 
                search in str(row.get('student_id', '')).lower()
                or 
                search in str(row.get('student_name', '')).lower()
                or 
                search in str(row.get('student_email', '')).lower()
            ]

        return jsonify(result)


api.add_resource(CompanyShortlistedStudents, '/company/shortlisted_students')


class CompanyApplication(Resource):
    @jwt_required()
    @cache.cached(timeout=10)
    def get(self):
        user_email = get_jwt_identity()
        current_user = User.query.filter_by(user_email=user_email).first()
        if not current_user or current_user.role.name != 'admin':
            return {"message": "not authorized"}, 403

        company_role = Role.query.filter_by(name='company').first()
        if not company_role:
            return jsonify([])

        data = User.query.filter_by(status=2, role_id=company_role.id).all()
        result = []
        for user in data:
            result.append({
                "user_id": user.user_id,
                "user_name": user.user_name,
                "user_email": user.user_email,
                # "status": user.status
            })
        
        return jsonify(result)
api.add_resource(CompanyApplication,'/company_application')

class RegisteredCompany(Resource):
    @jwt_required()
    @cache.cached(timeout=10)
    def get(self):
        data=User.query.filter_by(status=1,role_id=2).all()
        result = []
        for user in data:
            result.append({
                "user_id": user.user_id,
                "user_name": user.user_name,
                "user_email": user.user_email,
                # "status": user.status
            })
        
        return jsonify(result)
api.add_resource(RegisteredCompany,'/admin/registered_company')


class RemoveCompany(Resource):
    @jwt_required()
    def delete(self, company_id):
        user_email = get_jwt_identity()
        current_user = User.query.filter_by(user_email=user_email).first()
        if not current_user or current_user.role.name != 'admin':
            return {'message': 'not authorized'}, 403

        user = User.query.get(company_id)
        if not user:
            return {'message': 'company not found'}, 404

        company_role = Role.query.filter_by(name='company').first()
        if company_role and user.role_id != company_role.id:
            return {'message': 'invalid company user'}, 400

        company_profile = CompanyProfile.query.get(company_id)
        if company_profile:
            drives = PlacementsDrives.query.filter_by(company_id=company_id).all()
            for drive in drives:
                Applications.query.filter_by(drive_id=drive.drive_id).delete()
                db.session.delete(drive)
            db.session.delete(company_profile)

        db.session.delete(user)
        db.session.commit()
        return {'message': 'company removed successfully'}, 200


api.add_resource(RemoveCompany, '/admin/remove_company/<int:company_id>')


#______________________END of Company




# STUDENT__________________________



class Students(Resource):
    @jwt_required()
    @cache.cached(timeout=10)
    def get(self):
        data=User.query.filter_by(status=1,role_id=3).all()
        
        result = []
        for user in data:
            result.append({
                "user_id": user.user_id,
                "user_name": user.user_name,
                "user_email": user.user_email,

                # "status": user.status
            })
        
        return jsonify(result)
    
api.add_resource(Students,'/admin/registered_students')


class RemoveStudent(Resource):
    @jwt_required()
    def delete(self, student_id):
        user_email = get_jwt_identity()
        current_user = User.query.filter_by(user_email=user_email).first()
        if not current_user or current_user.role.name != 'admin':
            return {'message': 'not authorized'}, 403

        user = User.query.get(student_id)
        if not user:
            return {'message': 'student not found'}, 404

        student_role = Role.query.filter_by(name='student').first()
        if student_role and user.role_id != student_role.id:
            return {'message': 'invalid student user'}, 400

        Applications.query.filter_by(student_id=student_id).delete()
        student_profile = StudentProfile.query.get(student_id)
        if student_profile:
            db.session.delete(student_profile)

        db.session.delete(user)
        db.session.commit()
        return {'message': 'student removed successfully'}, 200


    class AdminStudentApplications(Resource):
        @jwt_required()
        # @cache.cached(timeout=10)
        def get(self):
            user_email = get_jwt_identity()
            current_user = User.query.filter_by(user_email=user_email).first()
            if not current_user or current_user.role.name != 'admin':
                return {"message": "not authorized"}, 403

            apps = Applications.query.all()
            result = []
            for app in apps:
                drive = PlacementsDrives.query.get(app.drive_id)
                student_user = User.query.get(app.student_id)
                result.append({
                    "application_id": app.application_id,
                    "drive_id": app.drive_id,
                    "job_title": drive.job_title if drive else None,
                    "company_id": drive.company_id if drive else None,
                    "student_id": app.student_id,
                    "student_name": student_user.user_name if student_user else None,
                    "student_email": student_user.user_email if student_user else None,
                    "application_date": app.application_date.isoformat() if app.application_date else None,
                    "status": app.status,
                })

            search = request.args.get('search', '').strip().lower()
            if search:
                result = [
                    row for row in result
                    if search in str(row.get('application_id', '')).lower()
                    or search in str(row.get('drive_id', '')).lower()
                    or search in str(row.get('job_title', '')).lower()
                    or search in str(row.get('company_id', '')).lower()
                    or search in str(row.get('student_id', '')).lower()
                    or search in str(row.get('student_name', '')).lower()
                    or search in str(row.get('student_email', '')).lower()
                    or search in str(row.get('application_date', '')).lower()
                    or search in str(row.get('status', '')).lower()
                ]

            return jsonify(result)


    api.add_resource(AdminStudentApplications, '/admin/student_applications')
api.add_resource(RemoveStudent, '/admin/remove_student/<int:student_id>')


 
    
class StudentProfileAction(Resource): 

    @jwt_required()
    @cache.cached(timeout=10)
    def get(self):
        email=get_jwt_identity()
        student=User.query.filter_by(user_email=email).first()
        try:
            print(student)
            if student.sp:
            
                if student.user_id == student.sp.student_id:
                    data=student.sp
                    
                    return {"student_id":data.student_id,
                            "resume_path":data.resume_path,
                            "phone_no":data.phone_no,
                            "address":data.address,
                            "social_profile":data.social_profile
                            },200
                
                else:
                    return {"message":'user profile is not updated'}
            else:
                return {"message":"user updated profile not found; uploading resume is mandatory for first update; once your profile gets updated only than you will able to apply "}

        except Exception as err:
            return{'message':str(err)}


    @jwt_required()
    def put(self):
        
        email=get_jwt_identity()
        current_user = User.query.filter_by(user_email=email ).first()
        if not current_user or current_user.role.name != 'student':
            return {"message": "not authorized"}, 403
        
            
        file=request.files.get('resume')
        phone_no = request.form.get('phone_no')
        address = request.form.get('address')
        social_profile = request.form.get('social_profile')

        if file:
            # return {'message':'file not found'},400
            if not file.filename.endswith('.pdf'):
                return {'message':'file is not a pdf file'},400
        
            folder = "uploads"
            os.makedirs(folder, exist_ok=True)
            unique_name = unique_str()
            filepath = os.path.join(folder, f"{unique_name}.pdf")

            file.save(filepath)

        student = StudentProfile.query.get(current_user.user_id)
        if student:
            student.resume_path = filepath
            student.phone_no = phone_no
            student.address = address
            student.social_profile = social_profile
        else:
            student = StudentProfile(
                student_id=current_user.user_id,
                resume_path=filepath,
                phone_no=phone_no,
                address=address,
                social_profile=social_profile,
            )
            db.session.add(student)

        db.session.commit()
        
        
        return {"message": "updated successfully", "resume_path": filepath}, 200




api.add_resource(StudentProfileAction,'/student_profile')


class StudentResume(Resource):
    @jwt_required()
    @cache.cached(timeout=10)
    def get(self):
        email = get_jwt_identity()
        current_user = User.query.filter_by(user_email=email).first()
        if not current_user or current_user.role.name != 'student':
            return {"message": "not authorized"}, 403

        if not current_user.sp or not current_user.sp.resume_path:
            return {"message": "resume not found"}, 404

        resume_path = current_user.sp.resume_path
        if not os.path.exists(resume_path):
            return {"message": "resume file missing on server"}, 404

        return send_file(
            resume_path,
            mimetype='application/pdf',
            as_attachment=True,
            download_name=f"resume_{current_user.user_id}.pdf"
        )


api.add_resource(StudentResume, '/student_profile/resume')


class StudentApplications(Resource):
    @jwt_required()
    @cache.cached(timeout=10)
    def get(self):
        user_email = get_jwt_identity()
        current_user = User.query.filter_by(user_email=user_email).first()
        if not current_user or current_user.role.name != 'student':
            return {"message": "not authorized"}, 403

        apps = Applications.query.filter_by(student_id=current_user.user_id).all()
        result = []
        for app in apps:
            drive = PlacementsDrives.query.get(app.drive_id)
            result.append({
                "application_id": app.application_id,
                "drive_id": app.drive_id,
                "job_title": drive.job_title if drive else None,
                "company_id": drive.company_id if drive else None,
                "application_date": app.application_date.isoformat() if app.application_date else None,
                "status": app.status,
            })

        return jsonify(result)


api.add_resource(StudentApplications, '/student/applications')

#______________________END Student




# ADMIN_________________________

class ApproveApplication(Resource):
    @jwt_required()
    # @admin
    def patch(self,company_id):
        data=request.get_json()
        user=User.query.get(company_id)
        user_email=get_jwt_identity()
        current_user=User.query.filter_by(user_email=user_email).first()
        if not current_user or current_user.role.name != "admin":
            return {"message":"not a admin"},403

        if not user:
            return {"message":"not exist"},404
        if data and "status" in data:
            user.status=data["status"]
            # company=CompanyProfile(company_id=user.user_id,company_name=user.user_name)
            # db.session.add(company)

        db.session.commit()
        return{"message":"updated successfully"},200

api.add_resource(ApproveApplication,"/approve_application/<int:company_id>")


#________________________________________________________ 
# 
# dashboard showing summary

class AdminDashboardStats(Resource):
    @jwt_required()
    def get(self):
        user_email = get_jwt_identity()
        current_user = User.query.filter_by(user_email=user_email).first()
        if not current_user or current_user.role.name != 'admin':
            return {"message": "not authorized"}, 403

        student_role = Role.query.filter_by(name='student').first()
        company_role = Role.query.filter_by(name='company').first()

        student_count = User.query.filter_by(role_id=student_role.id, status=1).count() if student_role else 0
        company_count = User.query.filter_by(role_id=company_role.id, status=1).count() if company_role else 0
        drive_count = PlacementsDrives.query.count()

        return {
            "total_students": student_count,
            "total_companies": company_count,
            "total_drives": drive_count,
        }, 200


api.add_resource(AdminDashboardStats, '/admin/dashboard_stats')


class AdminHiredStudents(Resource):
    @jwt_required()
    def get(self):
        user_email = get_jwt_identity()
        current_user = User.query.filter_by(user_email=user_email).first()
        if not current_user or current_user.role.name != 'admin':
            return {"message": "not authorized"}, 403

        hired_apps = Applications.query.filter_by(status=2).all()
        result = []
        for app in hired_apps:
            drive = PlacementsDrives.query.get(app.drive_id)
            student_user = User.query.get(app.student_id)
            result.append({
                "application_id": app.application_id,
                "drive_id": app.drive_id,
                "job_title": drive.job_title if drive else None,
                "company_id": drive.company_id if drive else None,
                "student_id": app.student_id,
                "student_name": student_user.user_name if student_user else None,
                "student_email": student_user.user_email if student_user else None,
                "application_date": app.application_date.isoformat() if app.application_date else None,
                "status": app.status,
            })

        search = request.args.get('search', '').strip().lower()
        if search:
            result = [
                row for row in result
                if search in str(row.get('application_id', '')).lower()
                or search in str(row.get('drive_id', '')).lower()
                or search in str(row.get('job_title', '')).lower()
                or search in str(row.get('company_id', '')).lower()
                or search in str(row.get('student_id', '')).lower()
                or search in str(row.get('student_name', '')).lower()
                or search in str(row.get('student_email', '')).lower()
            ]

        return jsonify(result)


api.add_resource(AdminHiredStudents, '/admin/hired_students')


class DriveApplications(Resource):
    @jwt_required()
    @cache.cached(timeout=10)
    def get(self, drive_id):
        user_email = get_jwt_identity()
        current_user = User.query.filter_by(user_email=user_email).first()
        if not current_user or current_user.role.name != 'admin':
            return {"message": "not authorized"}, 403

        drive = PlacementsDrives.query.get(drive_id)
        if not drive:
            return {"message": "drive not found"}, 404

        applications = Applications.query.filter_by(drive_id=drive_id).all()
        result = []
        for app in applications:
            student_user = User.query.get(app.student_id)
            student_profile = StudentProfile.query.get(app.student_id)
            result.append({
                "application_id": app.application_id,
                "drive_id": app.drive_id,
                "student_id": app.student_id,
                "student_name": student_user.user_name if student_user else None,
                "student_email": student_user.user_email if student_user else None,
                "resume_path": student_profile.resume_path if student_profile else None,
                "application_date": app.application_date.isoformat() if app.application_date else None,
                "status": app.status,
            })


api.add_resource(DriveApplications, '/admin/drive_applications/<int:drive_id>')




