import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

html_template = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{subject}</title>
</head>
<body style="margin:0; padding:0; background-color:#f4f6f8; font-family:Arial, sans-serif;">

    <table align="center" width="100%" cellpadding="0" cellspacing="0" style="padding:20px 0;">
        <tr>
            <td align="center">

                <!-- Main Container -->
                <table width="600" cellpadding="0" cellspacing="0" style="background:#ffffff; border-radius:8px; overflow:hidden; box-shadow:0 2px 8px rgba(0,0,0,0.05);">

                    <!-- Header -->
                    <tr>
                        <td style="background:#4f46e5; color:#ffffff; padding:20px; text-align:center;">
                            <h1 style="margin:0; font-size:22px;">{subject}</h1>
                        </td>
                    </tr>

                    <!-- Body -->
                    <tr>
                        <td style="padding:30px; color:#333333; line-height:1.6;">
                            <p style="margin:0 0 15px 0; font-size:15px;">
                                {body}
                            </p>

                            <!-- Button -->
                            <div style="text-align:center; margin:30px 0;">
                                <a href="http://localhost:5173"
                                   target="_blank"
                                   style="background:#4f46e5;
                                          color:#ffffff;
                                          padding:12px 20px;
                                          text-decoration:none;
                                          border-radius:5px;
                                          font-size:14px;
                                          display:inline-block;">
                                    View Details
                                </a>
                            </div>

                            <p style="font-size:13px; color:#777;">
                                If the button doesn't work, copy and paste this link into your browser:<br>
                                <a href="http://localhost:5173" style="color:#4f46e5;">http://localhost:5173</a>
                            </p>
                        </td>
                    </tr>

                    <!-- Footer -->
                    <tr>
                        <td style="background:#f1f1f1; padding:15px; text-align:center; font-size:12px; color:#888;">
                            © 2026 Your Company. All rights reserved.
                        </td>
                    </tr>

                </table>

            </td>
        </tr>
    </table>

</body>
</html>
"""

SMTP_HOST = 'localhost'
SMTP_PORT = 1025
FROM_EMAIL = 'admin@gmail.com'

def send_email(to_email, subject, body):
    msg = MIMEMultipart()
    msg['From'] = FROM_EMAIL
    msg['To'] = to_email
    msg['Subject'] = subject
    body = html_template.format(subject=subject, body=body)
    msg.attach(MIMEText(body, 'html'))

    # Send the email
    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        server.send_message(msg)

if __name__ == "__main__":
    send_email('user@example.com', 'Test Subject', 'Welcome to Mobile Shopping!, Check out our latest collection of mobiles.')