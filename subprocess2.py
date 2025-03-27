import subprocess
import sys

cmd = ['ping', '127.0.0.1', '-c', '4']
encoding = 'utf_8'
system = sys.platform

if system == "win32":
    cmd = ['ping', '127.0.0.1']
    encoding = 'cp850'

proc = subprocess.run(
    cmd, capture_output=True,
    text=True, encoding=encoding
)

# print(proc.args)
# print(proc.stderr)
print(proc.stdout)
# print(proc.returncode)