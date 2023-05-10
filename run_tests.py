import os
import subprocess

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
test_dir = os.path.join(root_dir, "tests")

def run_tests():
    result = subprocess.run(["pytest", test_dir, f"--rootdir={root_dir}"], capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)

if __name__ == "__main__":
    run_tests()

