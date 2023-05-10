import os
import subprocess

def run_tests():
    result = subprocess.run(["pytest", "test_heroku.py"], capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)

if __name__ == "__main__":
    run_tests()

