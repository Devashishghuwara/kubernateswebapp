#!/usr/bin/python3

print("content-type: text/html")     # this line is used by the  browser as Head of Website
print()                              # used to seprate Head of website to its Body

import cgi			     # CGI is Common Gateway Interface between client and server
import subprocess		     # this is used to retrive data and produce output by running system command 

form = cgi.FieldStorage()	      
cmd  = form.getvalue("x")	     # var is the variable that store the input from the website page 
output = subprocess.getoutput(cmd)   # the value store in var is parse into system command and it return output
print(output)

if("all" in cmd ) and ("pods" in cmd):
    output = sb.getoutput("kubectl get pods --kubeconfig admin.conf")    
    print("<pre>{}</pre>".format(output))
    print("</body>")
    
elif("all" in cmd) and ("deployments" in cmd):
    output = sb.getoutput("kubectl get deployment --kubeconfig admin.conf")
    print("<pre>{}</pre>".format(output))
    print("</body>")


elif(("create" in cmd) or ("launch" in cmd ) and ("pod" in cmd ):
    output = sb.getoutput("kubectl run {} --image=centos:latest --kubeconfig admin.conf".format(name))
    print("<pre>{}</pre>".format(output))
    print("</body>")


elif("deployment" in cmd) and ("create" in cmd ):
    output = sb.getoutput("kubectl create deployment {} --image=centos:latest --kubeconfig admin.conf ".format(name))
    print("<pre>{}</pre>".format(output))
    print("</body>")


elif("deployment" in cmd) and ("expose") and ("port number"):
    output = sb.getoutput("kubectl expose deployment {} --port={} --type=NodePort --kubeconfig admin.conf ".format(name,port))
    print("<pre>{}</pre>".format(output))
    print("</body>")


elif("create" in cmd ) or ("scale" in cmd ) and (("replica" in cmd ) or ("deployment" in cmd )):
    output = sb.getoutput("kubectl scale deployment  {} --replicas={} --kubeconfig admin.conf ".format(name,replica))
    print("<pre>{}</pre>".format(output))
    print("</body>")


elif ("delete" in cmd ) and ("pod" in cmd):
    output = sb.getoutput("kubectl delete pods {} --kubeconfig admin.conf".format(name))
    print("<pre>{}</pre>".format(output))
    print("</body>")


elif("delete" in cmd ) and ("deployment" in cmd ):
    output = sb.getoutput("kubectl delete deployment {}  --kubeconfig admin.conf" .format(name))
    print("<pre>{}</pre>".format(output))
    print("</body>")


else:
    print("<pre>Invelid Input...</pre>")
    print("</body>")
