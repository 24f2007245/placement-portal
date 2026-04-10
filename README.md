# placement-portal

It is a web application which helps institute, company, and student for campus recruitment. It has role-based dashboards, search options, asynchronous background jobs with Celery (for reminders, reports), and email alerts for important actions. This makes it easier to coordinate work by having everything in one place.


##DB Schema Design

#Relationships

Role ──────── N:1 ──────── User
                              │
               ┌──────────────┤──────────────────┐
               ▼                                  ▼
        StudentProfile (1:1)             CompanyProfile (1:1)
               │                                  │
               │ 1:N                              │ 1:N
               ▼                                  ▼
         Applications ◄──── 1:N ──── PlacementsDrives



##Api Endpoints

GET /
POST /register
POST /login
POST /drives
GET /drives
GET /drives/<int:drive_id>
POST /apply_drive/<int:drive_id>
PATCH /approve_drive/<int:drive_id>
DELETE /admin/remove_drive/<int:drive_id>
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



##Architecture and Features
#Architecture Details-
Platform: Web-based
Architecture: Client-server
Software architecture/Design Pattern: Model-View-Controller(MVC)
#Features - 
Role-based login for admin, company, and student users.
Company registration with admin approval workflow.
Placement drive creation, approval, and management.
Student profile update with resume upload support.
Students can apply to approved drives before deadline.
Company can shortlist, reject, and hire applicants.
Admin can view students, companies, applications, and hired students.
Search available across major dashboard lists.
Automated email notifications for shortlist and reminders.




##useful commands
#To Stop redis-server 'sudo systemctl stop redis'
#redis-server