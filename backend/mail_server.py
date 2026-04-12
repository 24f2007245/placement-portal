
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from datetime import date, timedelta
from celery_thing import celery_app
from models import Applications, PlacementsDrives, User,Role

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{subject}</title>
</head>
<body>
    <div style='background:linear-gradient(45deg, #2980b9,white); color:#f5f5f5; padding:10px;'>
        Placement Cell
    </div>
    <div style='padding:10px;color:gray'>
    <p>{body}</p>
        <p>Best Regards<br>
        Placement Cell<br>
        admin@admin.com</p></div>
    <footer style="padding: 10px; color: gray; background-color: #f5f5f5;">
        <p>All Rights Reserved &copy;, placement cell</p>
    </footer>
</body>
</html>
"""






SMTP_HOST = 'localhost'
SMTP_PORT = 1025
FROM_EMAIL = 'admin@pcell.com'


            # send_email.delay(current_user.email,'Congratulation on geting shortlisted',f"Dear {current_user.name},<br>We had received your application and now your application_id {application.application_id} gets shortlised. Visit the portal there you will find status as shortlised. We are looking forward with your interview; we will inform you later.<br>Thank You")
@celery_app.task()
def shortlisted_mail(application_id):
    from app import db
    

    application= Applications.query.get(application_id)
    if not application:
        return "Application not found"

    applicant =application.student_p.usr_s
    if not applicant:
        return "Applicant not found"

    subject = "Congratulations on getting shortlisted"
    body = f"""
        Dear {applicant.user_name},<br>

        We are pleased to inform you that your application 
        (ID: {application.application_id}) has been <b>shortlisted</b> for in-person interview.<br>
        please, find you interview details- <br>
        you have to reach within 7 days from the date of this email at company brach, and report there .
        <br><br>
        Please log in to the portal to check further details.<br>
        <br><br>
        """

    send_email.delay(applicant.user_email, subject, body)

    return "Shortlisted email sent"


@celery_app.task()
def hire_mail(application_id):
    from app import db
    
    # print('Task received at stage 1',application_id)
    application = Applications.query.get(application_id)

    if not application:
        return "Application not found"

    # assuming relationship exists
    applicant =application.student_p.usr_s

    if not applicant:
        return "Applicant not found"

    subject = "Congratulations on getting hired"

    body = f"""
    Dear {applicant.user_name},<br>

    We are pleased to inform you that your application 
    (ID: {application.application_id}) has been selected. You are hired.<br><br>

    Please log in to the portal to check further details.<br>
    You will get offer letter by the company side.<br><br>

    """

    send_email.delay(applicant.user_email, subject, body)

    return "Shortlisted email sent"




@celery_app.task()
def send_email(to_email, subject, body):
    msg = MIMEMultipart()
    msg['From'] = FROM_EMAIL
    msg['To'] = to_email
    msg['Subject'] = subject

    
    body = HTML_TEMPLATE.format(subject=subject, body=body)
    msg.attach(MIMEText(body, 'html'))

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        server.send_message(msg)



# DAILY REMAINDER FOR UPCOMING DRIVES

@celery_app.task
def send_daily_reminder():
    today = date.today()
    # upcoming = today + timedelta(days=1)
    drives = PlacementsDrives.query.filter(
        PlacementsDrives.application_deadline >= today,PlacementsDrives.status == 1
    ).order_by(PlacementsDrives.application_deadline.asc()).limit(3).all()   
    if not drives:
        print("No upcoming drives")
        return
    users = User.query.join(Role).filter(Role.name == 'student').all()
    emails = [user.user_email for user in users]

    for email in emails:
        subject='Remainder for upcoming drive'
        body=f'''Dear student,<br>
            there are many drives listed in portal visit and apply in which you are elligible. <br>
            some drives with near deadline<br>
            Today : {today}'''
        for drive in drives:
            body+=f"""<br>
            Drive Id: {drive.drive_id},<br>
            Job Title: {drive.job_title},<br>
            Description: {drive.job_description},<br>
            Company Id: {drive.company_id},<br>
            Deadline: {drive.application_deadline}<br>
            apply before deadline....
            <br>
            """
        send_email.delay(email,subject,body)
    return "email sent"


@celery_app.task
def send_monthly_report():
    today = date.today()

    #yesterday - ek din pahle
    end = today - timedelta(days=1)

    # last month ka 1 tarik
    start = end.replace(day=1)

    total_applications = Applications.query.filter(
        Applications.application_date >= start,
        Applications.application_date <= end
    ).count()

    selected_students = Applications.query.filter(
        Applications.status == 2,
        Applications.application_date >= start,
        Applications.application_date <= end
    ).count()
    subject=f'''Report for {start} to {end}'''
    report = f"""
    Monthly Placement Report<br>
    
    
    Total Applications received: {total_applications}<br>
    Students Selected: {selected_students}<br>
    """
    body=f''' Admin,<br>
     have a look on report of placement portal activity data from {start} to {end}<br>
       {report}  
    Thank You'''

    send_email.delay('admin@admin.com',subject,body)