from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os
import subprocess

root_dir = os.path.abspath(os.path.dirname(__file__))
test_dir = os.path.join(root_dir, "test_heroku")
test_file = os.path.join(test_dir, "test_heroku.py")



def send_email_on_failure():
    message = Mail(
        from_email="hugo.fugeray@gmail.com",
        to_emails="payatonkawadeveloppeurs@gmail.com",
        subject="Tests Failed on Heroku",
        html_content="<strong>One or more tests failed on Heroku. Please check the logs for more details.</strong>"
    )

    sg = SendGridAPIClient(os.environ.get("SENDGRID_API_KEY"))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)

def run_tests():
    result = subprocess.run(["pytest", test_file, f"--rootdir={root_dir}"], capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)
    send_email_on_failure()

    if result.returncode != 0:
        send_email_on_failure()

if __name__ == "__main__":
    run_tests()

