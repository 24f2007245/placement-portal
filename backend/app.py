import os
from flask import Flask      # pyright: ignore[reportMissingImports]
from dotenv import load_dotenv      # pyright: ignore[reportMissingImports]



from models import db, User, Role
from flask_jwt_extended import JWTManager    # pyright: ignore[reportMissingImports]
from flask_cors import CORS  
from paths import api, cache     

jwt=JWTManager()
load_dotenv()

def create_app():
    app= Flask(__name__)
    app.config["JWT_SECRET_KEY"]='XYCHHORANADANPASSHAICOMPLEX'
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
    app.config["CACHE_TYPE"]='RedisCache'
    app.config["CACHE_REDIS_URL"]='redis://localhost:6379'

    CORS(app,origin=["http://localhost:5173"])


    db.init_app(app)
    cache.init_app(app)         #cache initialize ho raha h flask app ke saath
    api.init_app(app)           # api initialise ho raha h flask app ke saath
    jwt.init_app(app)

    with app.app_context():
        db.create_all()

        admin_role= Role.query.filter_by(name='admin').first()
        company_role= Role.query.filter_by(name='company').first()
        student_role= Role.query.filter_by(name='student').first()

        # creating all roles in db if not exist
        if not admin_role:
            db.session.add(Role(name='admin'))

        if not company_role:
            db.session.add(Role(name='company'))

        if not student_role:
            db.session.add(Role(name='student'))
        
        db.session.commit()

        is_admin=User.query.filter_by(user_email='admin@admin.com').first()
        if not is_admin:
            
            admin=User(
                user_email='admin@admin.com',
                user_password=os.getenv("PASSWORD"), 
                role=admin_role,
                user_name='Admin' )
            
            db.session.add(admin)
            db.session.commit()

    return app




# importing api and cache 
# from paths.py

#__________ye app ko run karne ke liye h_________________________

if __name__=='__main__':


    create_app().run(debug=True)

