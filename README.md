
# Placement-Portal

It is a web application which helps institute, company, and student for campus recruitment. It has role-based dashboards, search options, asynchronous background jobs with Celery (for reminders, reports), and email alerts for important actions. This makes it easier to coordinate work by having everything in one place.


## DB Schema Design

User: user_id,user_email,user_name,user_password,role_id,status\
Role: id, name\
PlacementsDrives: drive_id,company_id,job_title,job_description,branch,cgpa,year,application_deadline,status\
Applications: application_id,student_id,drive_id,application_date,status\
StudentProfile: student_id,resume_path,phone_no,address,social_profile\
CompanyProfile: company_id,company_description,hr_contact,website,approval_status

### Relationships

```
Role ──────── N:1 ──────── User
                              │
               ┌──────────────┤──────────────────┐
               ▼                                  ▼
        StudentProfile (1:1)             CompanyProfile (1:1)
               │                                  │
               │ 1:N                              │ 1:N
               ▼                                  ▼
         Applications ◄──── 1:N ──── PlacementsDrives


```

## Api Endpoints

```
GET /
POST /register
POST /login
POST /drives
GET /drives
GET /drives/<int:drive_id>
POST /apply_drive/<int:drive_id>
PATCH /approve_drive/<int:drive_id>
DELETE /admin/remove_drive/<int:drive_id>
GET /company_profile/<int:company_id>
POST /company/profile
GET /company/drives
GET /company/dashboard_stats
GET /company/drive_applications/<int:drive_id>
PATCH /company/application_status/<int:application_id>
GET /company/application_resume/<int:application_id>
GET /company/shortlisted_students
GET /company_application
GET /admin/registered_company
DELETE /admin/remove_company/<int:company_id>
GET /admin/registered_students
GET /admin/student_applications
DELETE /admin/remove_student/<int:student_id>
GET /student_profile
PUT /student_profile
GET /student_profile/resume
GET /student/applications
PATCH /approve_application/<int:company_id>
GET /admin/dashboard_stats
GET /admin/hired_students
GET /admin/drive_applications/<int:drive_id>

```

## Architecture and Features
### Architecture Details-
Platform: Web-based\
Architecture: Client-server

### Features - 
Role-based login for admin, company, and student users.\
Company registration with admin approval workflow.\
Placement drive creation, approval, and management.\
Student profile update with resume upload support.\
Students can apply to approved drives before deadline.\
Company can shortlist, reject, and hire applicants.\
Admin can view students, companies, applications, and hired students.\
Search available across major dashboard lists.\
Automated email notifications for shortlist and reminders.\
Also work on small devices like mobile phones\


# How To Run 

[port mentioned here is default one]
>For first time setup venv [ensure you are in backend/]

>[create venv]
`python3 -m venv venv`

>[go into venv]
`source venv/bin/activate`

>[install dependencies]
`pip3 install -r requirements.txt`

>To run virtual environment[for linux][make sure you are in backend/] 
`source venv/bin/activate`

To run app [backend] ->[port 5000]
`python app.py`

To install node pakage
`npm install`

To run frontend [frontend][make sure you are in frontend] ->[port 5173]
`npm run dev` 

To run redis-server ye karo shirf command agar pahle se running h to stop command\
[Stop redis-server `sudo systemctl stop redis`] ->[port 6379]  \
[process ko kill karne ke liye `sudo kill -9 PID`] [`sudo lsof -i:6379`]\
`redis-server`

To run mailhog ->[port 8025]
`mailhog`

To run celery worker command [backend/][activate venv ]\
`celery -A celery_thing.celery_app worker --loglevel=info`

To run celery beat command [backend/][activate venv]\
`celery -A celery_thing.celery_app worker --loglevel=info`
