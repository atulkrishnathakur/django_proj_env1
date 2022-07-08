# Django Virtual Environment Setup
1. First, install python3.9-venv package by using the following command.<br>
$ sudo apt-get install python3.9-venv  ###administrator user will run <br> 
$ mkdir mydjango   ###guest user can run<br>
$ cd mydjango ###guest user can run <br>
$ python3.9 -m venv django_vir_env1 ###guest user can run <br>
$ source django_vir_env1/bin/activate ###guest user can run <br>

<p>Now you can see</p>
(django_vir_env1) moonjdoob@atul-Lenovo-G570:~/pythonprojects/mydjango$ 

# How to install django in linux by guest user
(django_vir_env1) moonjdoob@atul-Lenovo-G570:~/pythonprojects/mydjango$ pip3 install django <br>
<p> OR </p>
(django_vir_env1) moonjdoob@atul-Lenovo-G570:~/pythonprojects/mydjango$ pip3 install Django==4.0.5 ###with specific django version

# How to check dejango version
(django_vir_env1) moonjdoob@atul-Lenovo-G570:~/pythonprojects/mydjango$ django-admin --version

# How to create project
(django_vir_env1) moonjdoob@atul-Lenovo-G570:~/pythonprojects/mydjango$ django-admin startproject django_vir_env1_proj

# How to run project
(django_vir_env1) moonjdoob@atul-Lenovo-G570:~/pythonprojects/mydjango$ cd django_vir_env1_proj <br>

(django_vir_env1) moonjdoob@atul-Lenovo-G570:~/pythonprojects/mydjango/django_vir_env1_proj$ python3.9 manage.py runserver

# How to connect workbench with mysql in ubuntu
1. Install mysql
2. Install mysql workbench from ubuntu software center
3. atul@atul-Lenovo-G570:~$ sudo snap connect mysql-workbench-community:password-manager-service :password-manager-service ###if MySQLWorkbench is blocked by AppArmor

# How to use git and github
1. clone the repository from github.com in other location
2. copy the .git folder and README.md file and paste it in root directory of your python project
3. click the profile icon from right top corner > setting > Developer Settings > personal access token > Generate new token ##set personal access token if token not set
4. moonjdoob@atul-Lenovo-G570:~/pythonprojects/mydjango/django_vir_env1_proj$ git remote set-url origin https://ghp_qyPE2VCh8EqXlUkM7r0T2X@github.com/atulkrishnathakur/django_proj_env1.git ###set the token in url
5. now you push your changes on github

# How to create app 
1. (django_vir_env1) moonjdoob@atul-Lenovo-G570:~/pythonprojects/mydjango/django_vir_env1_proj$ python3.9 manage.py startapp myadmin
2. add "myadmin" app in setting.py file

   #Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myadmin',
]

3. Note "admin" is bydefault app created by django

# Databas connectin with mysql
1. atul@atul-Lenovo-G570:~$ sudo sudo apt-get insall python3.9-dev build-essential ###If you get error when install mysqlclient
2. (django_vir_env1) moonjdoob@atul-Lenovo-G570:~/pythonprojects/mydjango/django_vir_env1_proj$ pip3 install mysqlclient ###install myssqlclient
3. DATABASES = {
        'default': {  
        'ENGINE': 'django.db.backends.mysql',  
        'NAME': 'django_vir_env1_proj',  
        'USER':'root',  
        'PASSWORD':'123456789',  
        'HOST':'localhost',  
        'PORT':'3306'  
    } 
} ###set in setting.py file to connect mysql database

# create tempolates in project root directory
1. Create a templates directory in project root directory
2. Now change the setting.py file for 

TEMPLATES = [
    {
        ..........
        'DIRS': [BASE_DIR / 'templates', ],
        .........................
        
    },

# crete static directory in project root directory
1. create a static directory in project root directory
2. Now change the setting.py file for

STATICFILES_DIRS = [
    BASE_DIR / "static",
]


