import os
import subprocess

root_dir = os.path.abspath(os.path.dirname(__file__))
test_dir = os.path.join(root_dir, "test_heroku")
test_file = os.path.join(test_dir, "test_heroku.py")

def run_tests():
    result = subprocess.run(["pytest", test_file, f"--rootdir={root_dir}"], capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)

if __name__ == "__main__":
    run_tests()

