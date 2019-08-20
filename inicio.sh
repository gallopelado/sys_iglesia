#!/bin/bash

# Do something
# ...

# then
source venv/bin/activate
#python run.py 

#Desde 19-08-2019
export FLASK_APP=app.py
export FLASK_ENV=development
flask run 
