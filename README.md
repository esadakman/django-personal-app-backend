<h1 align="center">Full Stack - Personal List App - Backend</h1>

<div align="center">
  <h3>
    <a href="http://esadd26.pythonanywhere.com/">
      Project Link
    </a>
  </h3>
</div>

<!-- TABLE OF CONTENTS -->

## Table of Contents

- [Overview](#overview)
- [Project Info](#projectinfo)
- [Entity Relationship Diagram](#entity-relationship-diagram)
- [Project Link](#project-link)
- [Preview](#preview-of-the-project)
- [Built With](#built-with)
- [Project Structure](#project-structure)
- [How to use](#how-to-use)
- [Contact](#contact)

## Overview  

- This is the backend side of my personal list app project.
- I used reactjs for frontend.
  ##### You can see the frontend side of this project from [here](https://github.com/esadakman/reactjs-personal-app-frontend) 👈

## Project Info

<ul>
    <li>Department and Personnel tables are interconnected and each department has its own personnel..</li>
    <li>Company personnel who have logged into the system can see the departments of the company and the personnel working under those departments in detail.</li>
    <li>Staff members can add or update new staff to the department list.</li>
    <li>Only superusers will have the authority to delete staff.</li>
    <li>We will construct this structure using a generic view. In order to override Class methods, we will provide if-else structures that should act accordingly whether the person is a staff or superuser. We will use IsAuthenticated from Rest framework permissions.</li>
    <li>I used nested serializer and method fields in our serializer.</li>
    <li>I used the cors-headers package to connect the frontend to our API.</li>
</ul>

- You can perform staff operations using the following account information:
  - userName: michaelscott
  - password: Littlekidlover1
<!-- ERD -->

## Entity Relationship Diagram

![erd](https://user-images.githubusercontent.com/98649983/196051154-04aba539-afb2-44d9-b81b-97858f3ad483.jpg)


 <!-- OVERVIEW -->

## Project Link

#### You can reach my project from [here](http://esadd26.pythonanywhere.com/) 👈
## Preview of the Project
![personal-back](https://user-images.githubusercontent.com/98649983/196050067-271c11be-31e3-4a9b-aad7-6679c2c1a45a.gif)

### Built With

<!-- This section should list any major frameworks that you built your project using. Here are a few examples.-->

- Django
- Django Rest Framework
- Django Rest Auth
- Django Cors Headers

## Project Structure

```bash
.──── django-personal-app-backend (repo)
│
├── main
│     ├── __pycache__
│     ├── __init__.py
│     ├── asgi.py
│     ├── urls.py
│     ├── wsgi.py
│     └── settings.py
│─── personalApp
│       ├── __pycache__
│       ├── migrations
│       │── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── models.py
│       ├── serializers.py
│       ├── signals.py
│       ├── tests.py
│       ├── urls.py
│       └── views.py
├──── users
│       ├── __pycache__
│       ├── migrations
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── models.py
│       ├── serializers.py
│       ├── signals.py
│       ├── tests.py
│       ├── urls.py
│       └── views.py
├── manage.py
├── db.sqlite3
├── debug.log
├── requirements.txt
└── .env

```

## How To Use

To clone and run this application, you'll need [Git](https://git-scm.com)

```bash
# Clone this repository
$ git clone https://github.com/esadakman/django-personal-app-backend

# Install dependencies
    $ py -m venv env
    > env/Scripts/activate (for win OS)
    $ source env/bin/activate (for macOs/linux OS)
    $ pip install -r requirements.txt


# Add .env file for secret key and set your secret_key

- Create a .env file for =>
  -- SECRET_KEY,

- After these you can run the project as usual =>
    $ py manage.py migrate
    $ py manage.py createsuperuser

# Run the app
    $ python manage.py runserver
```

## Contact

- Website [@esadakman](https://esadakman.github.io/)
- GitHub [@esadakman](https://github.com/esadakman)
- Linkedin [@esadakman](https://www.linkedin.com/in/esadakman/)
