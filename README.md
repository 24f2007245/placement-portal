# placement-portal
Institutes require efficient systems to manage campus recruitment activities involving companies and students. Currently, many institutes rely on spreadsheets, emails, or manual coordination, which makes it difficult to manage company approvals, placement drives, student registrations, and application tracking.

git - track changes of our code
github - store our code in the cloud for colaboration

## Placement Application Module (Implemented)

This section documents what is already implemented for placement applications.

### What is implemented

1. Student can apply to approved placement drives.
2. Company can view applications received for each drive.
3. Company can update application status as Shortlisted or Rejected.
4. Student can view own applications and current status.

### Application Status Mapping

1. `0` = Applied
2. `1` = Shortlisted
3. `2` = Selected
4. `3` = Rejected

### Backend APIs

#### Apply for drive (Student)

- Method: `POST`
- Endpoint: `/apply_drive/<int:drive_id>`
- Auth: `@jwt_required()`
- Role: `student`
- Validations:
	- drive exists
	- drive is approved
	- deadline not over
	- student profile exists
	- duplicate application not allowed
- Success response:
	- `{ "message": "applied successfully" }`

#### View applicants for a drive (Company)

- Method: `GET`
- Endpoint: `/company/drive_applications/<int:drive_id>`
- Auth: `@jwt_required()`
- Role: `company`
- Validations:
	- drive exists
	- drive belongs to current company
- Response includes:
	- `application_id`
	- `drive_id`
	- `student_id`
	- `student_name`
	- `student_email`
	- `resume_path`
	- `application_date`
	- `status`

#### Update application status (Company)

- Method: `PATCH`
- Endpoint: `/company/application_status/<int:application_id>`
- Auth: `@jwt_required()`
- Role: `company`
- Payload:
	- `{ "status": 1 }` for Shortlisted
	- `{ "status": 3 }` for Rejected
- Validations:
	- application exists
	- related drive exists
	- drive belongs to current company

#### View own applications (Student)

- Method: `GET`
- Endpoint: `/student/applications`
- Auth: `@jwt_required()`
- Role: `student`
- Response includes:
	- `application_id`
	- `drive_id`
	- `job_title`
	- `company_id`
	- `application_date`
	- `status`

### Frontend Integration

#### Student side

1. In drives list, approved drives show an `apply` button for student role.
2. New page `My_Applications` shows all student applications with status text.

#### Company side

1. In company drives page, each approved drive has `view applications` button.
2. Company can click `shortlist` or `reject` for each application.

### Updated Files

#### Backend

1. `backend/paths.py`
	 - added apply drive API
	 - added company view applications API
	 - added company status update API
	 - added student applications API

#### Frontend

1. `frontend/src/components/Drives.vue`
	 - student apply action
2. `frontend/src/components/ViewDrives.vue`
	 - company view applications
	 - company shortlist/reject actions
3. `frontend/src/components/StudentApplications.vue`
	 - new component for student application status list
4. `frontend/src/router/index.js`
	 - route for `/student/applications`
5. `frontend/src/views/Student/StuDashView.vue`
	 - navigation link `My_Applications`

### Notes

1. APIs follow existing simple Flask-RESTful style used in this project.
2. All endpoints use JWT role checks similar to current coding pattern.
3. Frontend uses simple axios + token from localStorage as in existing components.
