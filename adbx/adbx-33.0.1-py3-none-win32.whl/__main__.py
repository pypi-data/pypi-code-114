import subprocess, sys

subprocess.run("adb " + " ".join(sys.argv[1:]), shell = True)