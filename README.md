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
3. set personal access token if token not set (click the profile icon from right top corner > setting > Developer Settings > personal access token > Generate new token
4. set the token in url (moonjdoob@atul-Lenovo-G570:~/pythonprojects/mydjango/django_vir_env1_proj$ git remote set-url origin https://ghp_qyPE2VCh8EqXlUkM7r0T2X@github.com/atulkrishnathakur/django_proj_env1.git)
5. now you push your changes on github

# How to create app 
1. (django_vir_env1) moonjdoob@atul-Lenovo-G570:~/pythonprojects/mydjango/django_vir_env1_proj$ python3.9 manage.py startapp admin
2. add "admin" app in setting.py file
   # Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'admin',
]


