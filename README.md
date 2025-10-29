## Project description

This is a fork of another repository. I added a login/logout/registration system and password recovery.
Most of the modifications were made in the main/view.py file, but it was also necessary to change other files.
To mark changes in the Python code, I used the following markings: “#added,” “#changed,” and if I added or changed
more than one line, I used the following template (“#added start ->” “<- #added end”).
In addition, I made some modifications to the HTML files to ensure backend compatibility, and
it was also necessary to restructure the database because my approach required the use of a user ID (username_id) in the database records, which
was not included.



## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/mohammedwed/lushlyrics-webapp-django.git
$ cd lushlyrics-webapp-django
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

You should also add an .env file containing the following variables:
HOST = /selected SMTP server
PORT = /port number/
HOST_USER = /sender's email address/
HOST_PASSWORD = /application password/ 

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd spotify-clone-django
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/demo`.
