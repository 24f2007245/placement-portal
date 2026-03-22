from flask_restful import Resource, Api        # pyright: ignore[reportMissingImports]
from flask import request                 # pyright: ignore[reportMissingImports]
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity      # pyright: ignore[reportMissingImports]
from models import db, User, Role

api=Api()


class Home(Resource):
    def get(self):
        return {"message":"connection successful"}, 200
    
api.add_resource(Home,"/") 

class Register(Resource):           #abhi registration risky h, logic will add later
    def post(self):
        data=request.get_json()
        if not data:
            return {"message":"invalid request body"},400
        is_user_exist=User.query.filter_by(user_email=data['email']).first()
        print(is_user_exist)
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
        return {"message": "user logged in successfully","access_token":access_token,"user_id":is_user.user_id,"email":is_user.user_email,"role":is_user.role.name},200
    
api.add_resource(Login ,'/login')
    
class PlacementsDrives(Resource):
    @jwt_required
    def post():
        data=request.get_json()
        drive_data=PlacementsDrives(company_id=data['user_id'],job_title=data['job_title'],job_description=data['job_description'],branch=data['branch'],cgpa=data['cgpa'],year=data['year'],application_deadline=data['application_deadline'])
        db.session.add(drive_data)
        db.session.commit()
        return {'message':'added successfully'}



