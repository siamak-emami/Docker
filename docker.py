import os
import subprocess
  	
args = ["dpkg-query", "-l"]
out, err = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()

i=0
chunks = out.split('\n')
for j in chunks:
    linetext=j.split()

	
    if 'docker-ce' in linetext or 'docker' in linetext:
	i=i+1

if i>0:
   print("Docker image has been installed")
else:
   print("Docker image has not been installed yet")
