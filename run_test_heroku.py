import smtplib
from email.mime.text import MIMEText
import os
import subprocess

root_dir = os.path.abspath(os.path.dirname(__file__))
test_dir = os.path.join(root_dir, "test_heroku")
test_file = os.path.join(test_dir, "test_heroku.py")

def send_email(subject, body, from_email, to_email, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Error while sending email: {e}")



def run_tests():
    result = subprocess.run(["pytest", test_file, f"--rootdir={root_dir}"], capture_output=True, text=True)

    if result.returncode != 0:
        from_email = "payatonkawadeveloppeurs@gmail.com"
        to_email = "hugo.fugeray@gmail.com"
        password = "mxihxxyfggmscqyb"
        subject = "Test Failure"
        body = f"Tests failed:\n\n{result.stdout}\n{result.stderr}"
        send_email(subject, body, from_email, to_email, password)

    else:
        print("All tests passed")
        from_email = "payatonkawadeveloppeurs@gmail.com"
        to_email = "hugo.fugeray@gmail.com"
        password = "mxihxxyfggmscqyb"
        subject = "Test success"
        body = f"Tests failed:\n\n{result.stdout}\n{result.stderr}"
        send_email(subject, body, from_email, to_email, password)

    print(result.stdout)
    print(result.stderr)




if __name__ == "__main__":
    run_tests()

