# Django Virtual Environment Setup
1. First, install python3.9-venv package by using the following command.<br>
$ sudo apt-get install python3.9-venv  ###administrator user will run <br> 
$ mkdir mydjango   ###guest user can run<br>
$ cd mydjango ###guest user can run <br>
$ python3.9 -m venv django_vir_env1 ###guest user can run <br>
$ cd ../ ###guest user can run <br>
$ source django_vir_env1/bin/activate ###guest user can run <br>

<p>Now you can see</p>
(django_vir_env1) moonjdoob@atul-Lenovo-G570:~/pythonprojects/mydjango$ 

# How to install django in linux by guest user
(django_vir_env1) moonjdoob@atul-Lenovo-G570:~/pythonprojects/mydjango$ pip3 install django

# How to check dejango version
(django_vir_env1) moonjdoob@atul-Lenovo-G570:~/pythonprojects/mydjango$ django-admin --version

# How to create project
(django_vir_env1) moonjdoob@atul-Lenovo-G570:~/pythonprojects/mydjango$ django-admin startproject django_vir_env1_proj

# How to run project
(django_vir_env1) moonjdoob@atul-Lenovo-G570:~/pythonprojects/mydjango$ django-admin startproject django_vir_env1_proj
