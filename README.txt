visit https://mhsn06-backend.readthedocs.io/en/latest/

Welcome

This is the backend component of the test project.

This component process data from user and store to database and query database for information requested by user.

This component implements a web service using Representational State Transfer (REST) technology.

Programming Language: Python

Core Rest Framework: Django
https://www.django-rest-framework.org/



The following guide describe how to setup environment to contribute to this component.

-----------------------------------------
step - 1:
Download and install lasted python version.
https://www.python.org/downloads/
-----------------------------------------
step - 2:
--------------
Pipenv is a python package manager to make life easier.

Install Pipenv package using following command
pip install pipenv
(press enter)
-----------------------------------------
step - 3:
To perform this step your present working directory in console should be within this project folder.

pipenv shell
(press enter)

Explanation:
This will create a viratual environment and active it. if you have used viratual environment in python you should feel what a relief.
-----------------------------------------

step - 4:
Installing neccessary packages
pipenv install
(press enter)
-----------------------------------------
step - 5:
Running the project

python manage.py runserver
(press enter)

The should be running now. Use control+C to stop the server when done.
-----------------------------------------
step - 6:
Running automated test

python manage.py test
(press enter)

-----------------------------------------
optional step

Manuall test

use firefox restclient extension
http://www.restclient.net/