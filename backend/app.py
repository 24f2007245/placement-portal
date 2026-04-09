from flask import Flask      # pyright: ignore[reportMissingImports]
from dotenv import load_dotenv      # pyright: ignore[reportMissingImports]
import os
from flask_jwt_extended import JWTManager    # pyright: ignore[reportMissingImports]
from flask_cors import CORS             
load_dotenv()
app= Flask(__name__)

CORS(app,origin="http://localhost:5173")

app.config["JWT_SECRET_KEY"]='XYCHHORANADANPASSHAICOMPLEX'
jwt=JWTManager(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
from models import db, User, Role
db.init_app(app)




# importing api and cache 
# from paths.py

from paths import api, cache

app.config["CACHE_TYPE"]='RedisCache'
app.config["CACHE_REDIS_URL"]='redis://localhost:6379/0'

cache.init_app(app)         #cache initialize ho raha h flask app ke saath
api.init_app(app)           # api initialise ho raha h flask app ke saath

#___________________________________

if __name__=='__main__':
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
            admin_role=Role.query.filter_by(name='admin').first()
            admin=User(
                user_email='admin@admin.com',
                user_password=os.getenv("PASSWORD"), 
                role=admin_role,
                user_name='Admin' )
            
            db.session.add(admin)
            db.session.commit()


    app.run(debug=True)

