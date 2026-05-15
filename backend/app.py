from flask import Flask     # pyright: ignore[reportMissingImports]
from dotenv import load_dotenv      # pyright: ignore[reportMissingImports]
from sqlalchemy import create_engine     # pyright: ignore[reportMissingImports]
from sqlalchemy.pool import NullPool
from models import db, User, Role
from flask_jwt_extended import JWTManager    # pyright: ignore[reportMissingImports]
from flask_cors import CORS      # pyright: ignore[reportMissingImports]
from paths import api, cache     
from werkzeug.security import generate_password_hash      # pyright: ignore[reportMissingImports]

import os
load_dotenv()
jwt=JWTManager()


def create_app():
    app= Flask(__name__)
    app.config["JWT_SECRET_KEY"]='JWT_SECRET'
    app.config["JWT_ACCESS_TOKEN_EXPIRES"]=1800
    

    # getting variables
    USER = os.getenv("user")
    PASSWORD = os.getenv("password")
    HOST = os.getenv("host")
    PORT = os.getenv("port")
    DBNAME = os.getenv("dbname")
    
    # Construct the SQLAlchemy connection string
    DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}?sslmode=require"
    
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    engine = create_engine(DATABASE_URL, poolclass=NullPool)

    REDIS_URL=os.getenv("REDIS_URL")
    app.config["CACHE_TYPE"]='RedisCache'
    app.config["CACHE_REDIS_URL"]=REDIS_URL

    CORS(app,origins=["https://placement-portal-omega-red.vercel.app"],supports_credentials=True)


    try:
        with engine.connect() as connection:
            print("Connection successful!")
    except Exception as e:
            print(f"Failed to connect: {e}")

    db.init_app(app)
    cache.init_app(app)         #cache initialize ho raha h flask app ke saath
    api.init_app(app)           # api initialise ho raha h flask app ke saath
    jwt.init_app(app)

    with app.app_context():
        try:
            db.create_all()
        except Exception as e:
            print("DB init failed:", e)
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

        is_admin=User.query.filter_by(user_email='placementcelladmin@gmail.com').first()
        if not is_admin:
            admin_role= Role.query.filter_by(name='admin').first()

            admin_password=os.getenv("ADMIN_PASSWORD")
            if not admin_password:
                raise ValueError("admin_password is not set.. ")
            admin=User(
                user_email='placementcelladmin@gmail.com',
                user_password=generate_password_hash(admin_password),
                role=admin_role,
                user_name='Admin' )
            
            db.session.add(admin)
            db.session.commit()

    return app




# importing api and cache 
# from paths.py

#__________ye app ko run karne ke liye h_________________________
app=create_app()
if __name__=='__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)