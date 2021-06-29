#!/usr/bin/python3

print("content-type: text/html")
print()

import cgi
import subprocess

#function to get input
f = cgi.FieldStorage()
cmd = f.getvalue("x")

#sudo to give extra power for docker
output = subprocess.getoutput("sudo " + cmd)
#osname= f.getvalue("osname")
#imgname=f.getvalue("imgname")
#output=subprocess.getoutput("sudo docker run -dit --name {} {}".format(osname,imgname))
print(output)

