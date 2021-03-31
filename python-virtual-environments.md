# Virtual Environments and Packages

I have two different ways listed below for creating Virtual Environments.  There is many other options but these are my current favorites.  I'm currently looking into `pyenv` for my `python` version management and `poetry` for my package management.  My current recommendation is using `venv` over `pipenv`.  Please make sure to add your `venv` folder to your `.gitignore` if you plan to use version control.

- https://docs.python.org/3/tutorial/venv.html
- https://pipenv.pypa.io/en/latest/


## Venv:
**Create Virtual Environment:**
> Wherever you run this command it will create a `venv` folder.  If you want the folder to be called something different change the second `venv`.
```
# Mac
$ python3 -m venv venv

# PC
$ python -m venv venv
```


**Activate The Virtual Environment:**
```
# Mac
$ source venv/bin/activate
(venv) $ _

# Windows
$ venv\Scripts\activate
(venv) $ _
```


**Installing Packages:**
```
(venv) $ pip install package-name
```


**Requirements File**

If you ever need to regenerate your environment on another machine, you are going to have trouble remembering what packages you had to install, so the generally accepted practice is to write a `requirements.txt` file in the root folder of your project listing all the dependencies, along with their versions. Producing this list is actually easy:
```
(venv) $ pip freeze > requirements.txt
```

The `pip freeze` command will dump all the packages that are installed on your virtual environment in the correct format for the `requirements.txt` file. Now, if you need to create the same virtual environment on another machine, instead of installing packages one by one, you can run:
```
(venv) $ pip install -r requirements.txt
```


## Pipenv
You can also setup virtual environments with `pipenv`.  My current recommendation is `venv` listed above.  When using `pipenv` the environment folder isn't created inside your project directory.  Be mindful you can setup `venv` first and then `pipenv` will use that `venv` location for it's environment.  Also when using `pipenv` you will get a `pipfile` and `pipfile.lock` for your package dependencies management, so there is no need to create a `requirements.txt` file.

**Create Virtual Environment:**
```
$ pipenv --three
```

**Activate The Virtual Environment:**
```
$ pipenv shell
```

**Installing Packages:**
```
(venv) $ pipenv install package_name
```

## Environment Variables
Sometimes you need to create environment variables for your project.  You can easily create them for your current terminal session with a simple `export` command.  The downfall is the variable isn't remembered across terminal sessions.  A more popular way is using a package called `python-dotenv`, which gives you the ability to store these variables inside a file.  If you plan on using version control with the `python-dotenv` method, please remember to hide your environment file in a `.gitignore` file.

> Be mindful you can set variables globally or specific to your virtual environment.  Make sure you're inside your virtual environment before running the `export` commands.

> When you host applications on `heroku` your environment variables are called `config variables`.  Luckily the methods for accessing your environment variables is the same. 

**Exported Environment Variable Setup**
```
# MAC
(venv) $ export VAR_NAME=secret

# PC
(venv) $ set VAR_NAME=secret
```

**Python-dotenv Environment Variable Setup**
- Create a file in your root directory, usually named `.env`
  - Are you using version control?  Add this file to your `.gitignore` file
  - It is common convention to use `ALL_CAPS_WITH_SNAKE_CASE_FOR_VARIABLE_NAMES`.  There is also no need for spaces before and after the `=` sign along with no need for `quotes` for strings.
```
# Env file
VAR_NAME=secret
```

**Accessing Environment Variables**

- Exported Variables
```python
import os
print(os.getenv('VAR_NAME'))
print(os.environ.get('VAR_NAME'))
print(os.environ['VAR_NAME'])
```

- Python-dotenv Variables
  - If you're using `flask v1.0 or above` you don't need to import and call the `load_dotenv`.
```python
import os
from dotenv import load_dotenv
load_dotenv()

print(os.getenv('VAR_NAME'))
print(os.environ.get('VAR_NAME'))
print(os.environ['VAR_NAME'])
```

**Unsetting An Exported Environment Variable**
```
# List all variables
(venv) $ printenv
OR
$ printenv

# Unset Virtual Environment Variables
(venv) $ unset VAR_NAME

# Unset Global Variables
$ unset VAR_NAME
```

## Starting the app
  uvicorn app.main:app --reload