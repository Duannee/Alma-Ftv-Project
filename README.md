# Alma Ftv
[![NPM](https://img.shields.io/npm/l/react)](https://github.com/Duannee/Alma-Ftv-Project/blob/main/LICENSE) 

# About the Project

**Alma-Ftv** is a REST API for managing footvolley training centers. The API is developed in Python using Django and Django Rest Framework. 
The Alma-Ftv API is a tool that helps training center owners organize and control their business activities simply and efficiently. With it, you can manage student information, track payments and administer the coaches working at the center.

## Base URL
The base URL to access the API is: [Api Alma Ftv](https://alma-ftv-project.onrender.com/api/user/create)

## Features
- **Accounts**: Full CRUD operations for user accounts.
- **Students**: Management of students, including creation, reading, updating, and deletion.
- **Student Profiles**: Each student can have a detailed profile associated with them.
- **Payments**: Payment tracking for students, with a payment profile associated with each student, making it easier to control.
- **Coaches**: Management of the coaches information at the training center.

## Requirements
- Python 3.8+
- Django 4.0+
- Django Rest Framework 3.12+
- drf-spectacular 0.22+

## Installation
Clone the repository:
```bash
git clone https://github.com/Duannee/Alma-Ftv-Project
cd Alma-Ftv-Project
```
Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate.ps1`
```
Install the dependencies:
```bash
pip install -r requirements.txt
```
Run the migrations:
```bash
python manage.py migrate
```
Create a superuser to access the admin panel:
```bash
python manage.py createsuperuser
```
Start the server:
```bash
python manage.py runserver
```

## Authentication
This API uses authentication for POST, PATCH, PUT, and DELETE methods. To access these features, you need to include an authentication token in the request headers.

### How to Obtain the Authentication Token

#### Get the Token:
- Use the superuser that was created.
- Log in using the `/api/token/` endpoint.
- You will receive a JWT token that should be used to authenticate subsequent requests.

#### Get a Refresh Token:
Your token expires in 30 minutes, so you'll need to regenerate it if you wish to make a new request after it has expired.
- In the `/api/token/` endpoint, copy the `refresh` key.
- In the `/api/token/refresh/` endpoint, paste your `refresh` token in the request body, and a new token will be generated in response.

## Endpoints
The full documentation for the API endpoints can be accessed after starting the server at:
- [Alma-Ftv-API Documentation](http://127.0.0.1:8000/api/docs/alma/)

### Example Endpoints
- **POST** `/api/user/create/` - Create user accounts.
- **GET** `/api/student/list/` - List all students.
- **GET** `/api/student_profile/{id}/retrieve/` - Retrieve details of a specific student's profile.
- **PATCH** `/api/payment/{id}/update/` - Update a student's payment details.
- **DELETE** `/api/coach/{id}/delete/` - Delete a coach.

## Query Parameters
The API allows the use of query parameters to filter the results returned by some endpoints. Below are the query parameters that can be used:

### Filtering
You can filter results based on different fields. For example:

- `/api/user/list/?username=username`: Filters accounts by username.
- `/api/student/list?name=student_name`: Filters students by name.
- `/api/student_profile/list?student=student_name`: Filters profiles by student name.
- `/api/payment/list?student=student_name`: Filters payments by student name.
- `/api/coach/list/?name=coach_name`: Filters coaches by name.

## Technologies Used
- Python
- Django
- Django Rest Framework

## Author

Duanne Moraes de Souza

[Duanne Moraes Linkedin](https://www.linkedin.com/in/duanne-moraes-7a0376278/)

