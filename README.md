#  Todo API - Backend Challenge

##  Project Description
This project is a **RESTful API** built for a Todo application as part of a Backend Development challenge. It allows users to manage their daily tasks securely. Each user has their own private list of todos, protected by **JWT (JSON Web Token) authentication**.

### Main Features:
* **User Isolation:** Users can only see, edit, or delete the todos they created.
* **JWT Authentication:** Secure login system using access and refresh tokens.
* **Full CRUD:** Supports Creating, Reading, Updating, and Deleting tasks.
* **Standards:** Implements proper HTTP status codes and input validation.

---

##  Tech Stack
* **Language:** Python 3.11+
* **Framework:** Django 5.2.7
* **API Toolkit:** Django REST Framework (DRF) 3.16.1
* **Authentication:** SimpleJWT 5.5.1
* **Database:** SQLite (Default)

---

##  Installation & Setup Instructions

Follow these steps exactly to run the project on your local machine:

### 1. Prerequisites
Ensure you have **Python 3.11 or higher** installed. Check your version with:
```bash
python --version
```

### 2. Clone the Repository
```bash
git clone [https://github.com/sbdev25/Todo_APP_BackendProject.git](https://github.com/sbdev25/Todo_APP_BackendProject.git)
cd Todo_APP_BackendProject
```
###3. Setup Virtual Environment
```bash
python -m venv venv
cd venv
Scripts\activate
```
###4. Install Dependencies
```bash
cd ..
pip install -r requirements.txt
```
###5. Database Setup
```bash
python manage.py makemigrations
python manage.py migrate
```
###6. Create an Admin User
You must create a superuser for the first time to access the Django dashboard and test the token APIs:
```bash
python manage.py createsuperuser
```
Follow the terminal prompts to set your username and password.

###7. Run the Server
```bash
python manage.py runserver
```
The API will be available at: http://127.0.0.1:8000/

## Todo Model Fields
As per the challenge requirements, each Todo item includes:
id: Auto-generated primary key.
user: ForeignKey linked to the authenticated User.
title: Character field (max 50).
description: Text field (max 500).
isCompleted: Boolean (default False).
createdAt: Automatically generated timestamp.

## List of Endpoints
All todos/ endpoints require the header: Authorization: Bearer <your_access_token>


| HTTP Method | Endpoint URL | Description |
| :--- | :--- | :--- |
| **POST** | `/token/` | Obtain Access & Refresh tokens (Customized with username). |
| **POST** | `/token/refresh/` | Use a Refresh token to generate a new Access token. |
| **GET** | `/todos/` | Retrieve a list of todos for the authenticated user. |
| **POST** | `/todos/add/` | Create a new Todo item. |
| **PUT** | `/todos/edit/<int:pk>/` | Update a specific Todo (Checks ownership). |
| **DELETE** | `/todos/delete/<int:pk>/` | Delete a specific Todo (Checks ownership). |

