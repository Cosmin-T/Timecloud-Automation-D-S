import schedule
import time as tm
import os
import traceback
import smtplib

def run_script():
    try:
        os.system("python3 main.py")
    except Exception as e:
        # Write error message and stack trace to a log file
        with open('error.log', 'a') as f:
            f.write(f"{tm.ctime()}: {e}\n{traceback.format_exc()}\n")
        # Send email notification with error message
        subject = "Error in running Timecloud automation"
        message = f"{tm.ctime()}: {e}\n{traceback.format_exc()}"
        email_from = "jamroack@gmail.com"
        email_to = "cosmin.turculeanu@dandsltd.com"
        email_message = f"Subject: {subject}\n\n{message}"
        try:
            smtp_server = smtplib.SMTP("smtp.example.com")
            smtp_server.sendmail(email_from, email_to, email_message)
            smtp_server.quit()
        except Exception as e:
            with open('error.log', 'a') as f:
                f.write(f"Error sending email notification: {e}\n")

# Schedule the script to run every weekday at 20:48

times = ["11:55", "14:55", "15:15", "17:55", "18:55", "19:55", "20:15", "20:55"]

for time in times:
    schedule.every().monday.at(time).do(run_script)
    schedule.every().tuesday.at(time).do(run_script)
    schedule.every().wednesday.at(time).do(run_script)
    schedule.every().thursday.at(time).do(run_script)
    schedule.every().friday.at(time).do(run_script)

while True:
    schedule.run_pending()
    tm.sleep(1)