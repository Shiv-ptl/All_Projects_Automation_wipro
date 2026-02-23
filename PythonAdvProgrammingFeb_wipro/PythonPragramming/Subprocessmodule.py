#subprocess.run() - run command and wait
#subprocess.popen() -run process aynchronulsy
#subprocess.PIPE-  capture the output
#subprocess.CompletePrecess  - result
#subprocess.TimeoutExpired - Time out exception
#subprocess.CalledPrecessError - command failure
import subprocess
result = subprocess.run(args="dir",shell=True,capture_output=True,text=True)
print(result)

result = subprocess.run(args="ipconfig",shell=True,capture_output=True,text=True)
print(result.stdout)

result = subprocess.run(args="python --version",shell=True,capture_output=True,text=True)
print(result)
print(result.stdout)
print(result.stderr)

# result = subprocess.run(args="clear",shell=True,capture_output=True,text=True)
# print(result)
result = subprocess.run(args="ping",shell=True,capture_output=True,text=True)
print(result.stdout)

