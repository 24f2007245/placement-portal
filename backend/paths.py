from flask_restful import Resource, Api        # pyright: ignore[reportMissingImports]
from flask import request, jsonify, send_file                # pyright: ignore[reportMissingImports]
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity      # pyright: ignore[reportMissingImports]
from models import db, User, Role, PlacementsDrives, StudentProfile 
from datetime import datetime
import os
api=Api()


#UNIQUE STRING__________________
def unique_str():
    str=datetime.now().strftime('%Y%m%d%H%M%S%f')
    return str


def serialize_drive(drive):
    return {
        "drive_id": drive.drive_id,
        "company_id": drive.company_id,
        "job_title": drive.job_title,
        "job_description": drive.job_description,
        "branch": drive.branch,
        "cgpa": drive.cgpa,
        "year": drive.year,
        "application_deadline": drive.application_deadline.isoformat() if drive.application_deadline else None,
        "status": drive.status
    }

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
            user=User(user_name=data['name'],user_email=data['email'],user_password=data['password'],role=role)
            db.session.add(user)
            db.session.commit()
            return {"message":"user registered successfully"},200
        else :
            user=User(user_name=data['name'],user_email=data['email'],user_password=data['password'],role=role, status=2)
            db.session.add(user)
            db.session.commit()
            return {"message":"registration successful, wait for your application to be approved by the admin"},200
        
api.add_resource(Register,'/register')


class Login(Resource):
    def post(self):
        data=request.get_json()
        is_user=User.query.filter_by(user_email=data['email'], user_password=data['password']).first()
        if not is_user:
            return {'message':'invalid email or password'},401
        if is_user and is_user.status==2:
            return {'message':'your application is not approved yet, once it approved you can login'},401
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
            deadline_date = datetime.strptime(deadline_str, "%d/%m/%Y").date()
        except ValueError:
            return {"message": "application_deadline must be in DD/MM/YYYY format"}, 400

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
    def get(self, drive_id=None):
        if drive_id is not None:
            drive = PlacementsDrives.query.get(drive_id)
            if not drive:
                return {"message": "drive not found"}, 404
            return serialize_drive(drive), 200

        data = PlacementsDrives.query.all()
        result = [serialize_drive(drive) for drive in data]
        return jsonify(result)
api.add_resource(PlacementDrive,'/drives','/drives/<int:drive_id>')


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

#____________________________END of placement drive section







# Company ___________________________

class CompanyDrives(Resource):
    @jwt_required()
    def get(self):
        user_email = get_jwt_identity()
        current_user = User.query.filter_by(user_email=user_email ).first()
        if not current_user or current_user.role.name != 'company':
            return {"message": "not authorized"}, 403

        data = PlacementsDrives.query.filter_by(company_id=current_user.user_id).all()
        result = [serialize_drive(drive) for drive in data]
        return jsonify(result)


api.add_resource(CompanyDrives, '/company/drives')


class CompanyApplication(Resource):
    @jwt_required()
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


#______________________END of Company




# STUDENT__________________________



class Students(Resource):
    @jwt_required()
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
    
api.add_resource(Students,'/students/all')


 
    
class StudentProfileAction(Resource): 

    @jwt_required()
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
                return {"message":"user updated profile not found"}

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




