### By **AHMED MUKHTAR**
## Installation Requirements
* A web browser
* A virtual environment
* Django
* Internet connection
* Terminal if you want to access the app locally through your computer


####
### Installation
* Clone,download or fork the the app from this link https://github.com/mukhtarabdirahman
* Install a virtual environment in your project folder by running the following commands: `$sudo apt-get install python3.6-venv`
* Then run  `$ python3.6 -m venv virtual`.
* To activate the virtual environment run `$ source virtual/bin/activate`
* To install Django,run the following command `$ source virtual/bin/activate`
* Then run `pip install django==1.11`
* To confirm whether Django is installed run the python shell by opening the terminal in the project folder and running `python3.6`
* In the shell `>>> import django`
* Then `>>> django.get_version()`.
* If Django is present you should get `'1.11'`
* Congratulations,you now have Django :-)
* To install requirements,go to your shell and enter the command
 `pip install -r requirements.txt`
* Rubn the app by `python3 manage.py runserver`
* Go to your browser and open the link http://127.0.0.1:8000 or http:///localhost:8000**
* Enjoy the App :-)...

### Important packages used in app development.

```
confusable-homoglyphs==3.1.1
Django==1.11
django-bootstrap3==10.0.1
django-registration==2.4.1
django-tinymce==2.7.0
gunicorn==19.9.0
Pillow==5.2.0
psycopg2==2.7.5
python-decouple==3.1
pytz==2018.5
```
