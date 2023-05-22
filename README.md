# ROUS

## How to set up project

1. create virtual environment

```bash
python -m venv env
```

2. activate on environment Windows (PS: check env file becuase Scrips folder can be named as bin instead of Scrips)

```bash
env\Scripts\Activate.ps1   (powershell- used in VS Code)
env\Scripts\activate.bat    (cmd)
```

3. install django in the virtual environment.

```bash
pip install django
```

4. install all the packages and used to update to new packages installed.

```bash
pip install -r requirements.txt
```
other: after installing new packages please update the requirements.txt shown below.
```bash
pip freeze > requirements.txt
```

# For API,

First, in the my_django_app, activate the virtual environment with the command: env\Scripts\activate
Next go into the ROUS directory, and then to run the server, do the command: python manage.py runserver
