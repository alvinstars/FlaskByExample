import sys
sys.path.insert(0, "/var/www/FlaskByExample/Project1/firstapp")
#sys.path.insert(0, "/home/ubuntu/.local/lib/python3.5/site-packages")
#sys.path.append('/home/ubuntu/.local/lib/python3.5/site-packages')
#print(sys.path)
#from flask import Flask
from hello import app as application
