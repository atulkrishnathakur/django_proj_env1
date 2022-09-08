
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


# print hello world 
1. create a folder corePython3.9
2. create helloworld.py in the folder

```
 print("Hello World")

```
2. run below command in terminal
```
 (django_vir_env1) moonjdoob@atul-Lenovo-G570:~/pythonprojects/mydjango/django_vir_env1_proj/corePython3.9$ python3.9 helloworld.py

```

# Python Syntax Example
1. create a file pythonSyntaxaExample.py in folder
2. If you’ve been working in other programming languages such as Java, C#, or C/C++, you know that these languages use semicolons (;) to separate the statements. Python, however, uses whitespace and indentation to construct the code structure.

```
# define main function to print out something
def main():
    i = 1
    max = 10
    while (i < max):
        print(i)
        i = i + 1

# call function main 
main()
```
3. run this file as below
```
(django_vir_env1) moonjdoob@atul-Lenovo-G570:~/pythonprojects/mydjango/django_vir_env1_proj/corePython3.9$ python3.9 pythonSyntaxExample.py
```

# Continuation of statements

1. Python uses a newline character to separate statements. It places each statement on one line. However, a long statement can span multiple lines by using the backslash (\) character. The following example illustrates how to use the backslash (\) character to continue a statement in the second line:

```
a = True
b = False
c = True
# However, a long statement can span multiple lines by using the backslash (\) character.
if (a == True) and (b == False) and \
   (c == True):
    print("Continuation of statements")

```

# Keywords

1. Python provides a special module for listing its keywords called keyword. 
2. To find the current keyword list, you use the following code:
```
import keyword

print(keyword.kwlist)

```
3. run the file as below.
```
(django_vir_env1) moonjdoob@atul-Lenovo-G570:~/pythonprojects/mydjango/django_vir_env1_proj/corePython3.9$ python3.9 keywords.py

```

# Variable

1. Syntax of variable

```
variable_name = value

```

# Strings 

```
# Single quotes string
message1 = 'This is a string in Python'
print(message1)

# String in double quotes
message2 = "This is also a string"
print(message2)

# If a string contains a single quote, you should place it in double-quotes like this
message3 = "It's a string"
print(message3)

# When a string contains double quotes, you can use the single quotes
message4 = '"Beautiful is better than ugly.". Said Tim Peters'
print(message4)

# To escape the quotes, you use the backslash (\). For example
message5 = 'It\'s also a valid string'
print(message5)

# The Python interpreter will treat the backslash character (\) special. If you don’t want it to do so, you can use raw strings by adding the letter r before the first quote. For example
message6 = r'C:\python\bin'
print(message6)

# Creating multiline strings
message7 = '''
Usage: mysql command
    -h hostname     
    -d database name
    -u username
    -p password 
'''
print(message7)

# Using variables in Python strings with the f-strings
name = "Atul"
message8 = f"Hi {name}"
print(message8)

# Concatenating Python strings
greeting = 'Good '
time = 'Afternoon'

greeting = greeting + time + '!'
print(greeting)

# Accessing string elements
str = "Python String"
print(str[0]) # P
print(str[1]) # y

str = "Python String"
print(str[-1])  # g
print(str[-2])  # n

# Getting the length of a string
str = "Python String"
str_len = len(str)
print(str_len)

# Slicing strings
str = "Python String"
print(str[0:2])

# Python strings are immutable. It means that you cannot change the string. For example, you’ll get an error if you update one or more characters in a string:
str = "Python String"
str[0] = 'J'


```

# How to create app 
1. (django_vir_env1) moonjdoob@atul-Lenovo-G570:~/pythonprojects/mydjango/django_vir_env1_proj$ python3.9 manage.py startapp myadmin
2. add "myadmin" app in setting.py file
```
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

```
3. Note "admin" is bydefault app created by django

# Databas connectin with mysql
1. atul@atul-Lenovo-G570:~$ sudo sudo apt-get insall python3.9-dev build-essential ###If you get error when install mysqlclient
2. (django_vir_env1) moonjdoob@atul-Lenovo-G570:~/pythonprojects/mydjango/django_vir_env1_proj$ pip3 install mysqlclient ###install myssqlclient
```
DATABASES = {
        'default': {  
        'ENGINE': 'django.db.backends.mysql',  
        'NAME': 'django_vir_env1_proj',  
        'USER':'root',  
        'PASSWORD':'123456789',  
        'HOST':'localhost',  
        'PORT':'3306'  
    } 
} 
```

3. set in setting.py file to connect mysql database

# create templates in project root directory
1. Create a templates directory in project root directory
2. Now change the setting.py file for 
```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates', ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

```
# crete static directory in project root directory
1. create a static directory in project root directory
2. Now change the setting.py file for
```
 STATICFILES_DIRS = [
    BASE_DIR / "static",
]
```

# how to write models.py file to create table name without concatenate app name in database table
1. use the meta 
```
from django.db import models 

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    
    class Meta:
      db_table = 'person'
      
class Boys(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=50)
    
    class Meta:
      db_table = 'boys'
      app_label = 'myadmin'
```

# How to organize models in a package if you have many models 
1. delete models.py file
2. create models directory in app
3. create file in models directory (Example: country.py)
4. create __init__.py file in models directory
5. write code in __init_.py file to import your model file. (Example: from myadmin.models import country)
6. now write code in modle file ##write below code in in country.py
```
from django.db import models

class Country(models.Model):
    id = models.BigAutoField(primary_key=True, default=None)
    country_name = models.CharField(max_length=255)
    
    class Meta:
      db_table = 'country'
```
7. db_table is attribute of Meta class
8. if you not use db_table then django automatically concatenate app name with table name in database like myadmin_country
9. if you use db_table then you can create table name according to your need

# How to create foreign key in django model

1. create a model for state (state.py) in model directory
2. write below code in state.py file
  ```
from django.db import models
from myadmin.models import country

class State(models.Model):
    id = models.BigAutoField(primary_key=True, default=None)
    state_name = models.CharField(max_length=255)
    country_id = models.ForeignKey(country.Country,null=True,on_delete=models.SET_NULL,db_column='country_id')
    
    class Meta:
      db_table = 'state'
 ```
2. when you create foreign key then django automatically add _id with column name 
3. if you not use db_column then dajango create field with _id (example: country_id_id)
4. if you want create foreign key field name according to your need then use db_column it create custom field name
