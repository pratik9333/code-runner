import json
import subprocess  
def c_runner(filepath,test_cases):
    build_cmd = f"gcc -o main {filepath}"
    subprocess.getstatusoutput(build_cmd)
    run_cmd=f"./main"
    print(subprocess.getstatusoutput(run_cmd))

def py_runner(filepath,test_cases):
    run_cmd=f"python3 {filepath}"
    print(subprocess.getstatusoutput(run_cmd))

def call_runner(language,filename,test_cases):
    file_path = f'solutions/{filename}'
    test_cases = json.loads(test_cases)
    if language == "python3":
        py_runner(file_path,test_cases)
    elif language == "c":
        c_runner(file_path,test_cases)