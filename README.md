# Databank System (CS18 Team Project)

Databank System is a project for Glasgow Imaging Facility, that helps to automate the process of storing data in database via user friendly interface, and allows users to export billing sheets in a CSV format.

This repository contains the files developed by group CS18 for Glasgow Imaging Facility.

## Getting Started

These instructions will help you run the project locally for development and testing purposes.

### Prerequisites

Python: Version 3.8 or later

### Installation

1. Clone the repository

2. Open in an IDE

3. Run `pip install -r requirements.txt` to install all needed modules, libraries and packages.

4. Navigate to gif_project/settings.py, and make sure Debug is set to True and ALLOWED_HOSTS to empty list as following, and if it isn't, set it according to this example:
```
DEBUG = True

ALLOWED_HOSTS = []
```
5. (OPTIONAL) To create/apply migrations, run:
```
python manage.py makemigrations databank_system
python manage.py migrate
```
6. (OPTIONAL) To create a superuser, run:
```
python manage.py createsuperuser
```
7. To run the app locally, run:
```
python manage.py runserver
```

## Running Tests

To run tests, simply run:
```
python manage.py test databank_system
```
To see also coverage, run:
```
coverage run manage.py test -v 2 && coverage report
```

## Style Guide

Project was developed in accordance with [pep8](https://www.python.org/dev/peps/pep-0008/) style guide.

## License

[MIT License](https://choosealicense.com/licenses/mit/)


## Team Members
| Name | Email |Roles|
| ------ | ------ | ------ |
|Kristina Galikova  |2478689g@student.gla.ac.uk  |Scrum Master|
|Erin Morgan  |2343910m@student.gla.ac.uk  |Developer|
|Scott Donaldson |2474880d@student.gla.ac.uk  |Product Owner|
|Qing Liang |2512275l@student.gla.ac.uk  | Scribe |

## Dissertation

Dissertation is present in the [dissertation repository](https://stgit.dcs.gla.ac.uk/team-project-h/2021/cs18/cs18-dissertation).
