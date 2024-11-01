import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time

def send_email():
    # Email configuration
    from_email = "ziyax360@gmail.com"
    from_password = "nasaaazi"  # Consider using environment variables for security
    to_email = "saminabarveen@gmail.com"

    # Craft the email
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = "Daily Reminder"
    
    # Email body content
    body = "This is your daily reminder."
    msg.attach(MIMEText(body, 'plain'))

    # Send the email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, from_password)
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Schedule the email to be sent daily
schedule.every().day.at("11:50").do(send_email)  # Set the time you want the email sent

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
