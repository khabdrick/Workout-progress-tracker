# Workout progress tracker ![Lint Python](https://github.com/khabdrick/Workout-progress-tracker/actions/workflows/lint_python.yml/badge.svg)



This project is a workout progress tracker, it can be used to track your progress after the gyming session and indicate if you are making progress or not. It can also be used as a log to see your past sessions and how you have improved over time.
It will also have a feature of providing helpful suggestions from time to time.

## Running this project locally

To get this project up and running you should start by having Python installed on your computer. It's advised you create a virtual environment to store your projects dependencies separately. You can install virtualenv with

```
pip install virtualenv
```

Clone or download this repository and open it in your editor of choice. In a terminal (mac/linux) or windows terminal, run the following command in the base directory of this project

```
virtualenv env
```

That will create a new directory `env` in your project directory. Next activate it with this command on mac/linux:

```
source env/bin/active
```

Then install the project dependencies with

```
pip install -r requirements.txt
```


Now you can run the project with this command

```
python manage.py runserver

```


## Use this to access admin

username: admin

email: admin@gmail.com

password: admin
