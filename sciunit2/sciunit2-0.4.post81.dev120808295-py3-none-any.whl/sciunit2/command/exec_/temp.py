import subprocess

try:
    output = subprocess.check_output(['date', '-i'], stderr=subprocess.STDOUT)
except subprocess.CalledProcessError as exc:
    print(exc.output.decode('utf-8'))
    print(exc.returncode)
else:
    print(output.decode('utf-8'))
