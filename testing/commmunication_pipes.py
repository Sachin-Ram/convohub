import subprocess

p= subprocess.run (["ipconfig"],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)

stdout,stderr=p.stdout,p.stderr

print(stdout.decode('utf-8'))

if stderr:
    print(stderr.decode('utf-8'))