=============
River
=============

:Info: River business communication tool
:Author: River Software

Dependencies
=============

1. django-extensions:

    g clone git://github.com/django-extensions/django-extensions.git djex && cd djex && sudo python setup.py install


Installation
=============
1. Create your local version of settings.py, copy settings.example.py and replace the PATH variable with the full path to your installation
2. Run @python manage.py syncdb@ and make sure to create a super user
3. Run @python manage.py runserver_plus@, browse to 127.0.0.1:8000 and enjoy!