
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from celery_thing import celery_app
from models import Applications, User, PlacementsDrives, Role

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{subject}</title>
</head>
<body>
    <div style='background:linear-gradient(45deg, #2980b9,white); color:#f5f5f5; padding:10px;'>
        <p>{body}</p>
        <p>Best Regards<br>
        Placement Cell<br>
        admin@admin.com</p>
    </div>
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
    
    # print('Task received at stage 1',application_id)
    application = Applications.query.get(application_id)

    if not application:
        return "Application not found"

    # assuming relationship exists
    applicant =application.student_p.usr_s

    if not applicant:
        return "Applicant not found"

    subject = "Congratulations on getting shortlisted"

    body = f"""
    Dear {applicant.user_name},<br>

    We are pleased to inform you that your application 
    (ID: {application.application_id}) has been <b>shortlisted</b>.<br><br>

    Please log in to the portal to check further details.<br>
    We will notify you about the next steps soon.<br><br>

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
    We will notify you about the next steps soon.<br><br>

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


# if __name__ == "__main__":
#     send_email('user@example.com', 'Congratulations you get shortlisted', 'Dear student, <br> i am happy to tell you your aplication got shortlisted')