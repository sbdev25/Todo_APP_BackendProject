#  Todo app 

##  Desription
This project is  a Backend project. It allows for users to create a todo list  .Each user have his own to do list and that by the jwt authentication wich is json web token .

### app Features:
* **User permissions:** the users can create , edit and update or delete a todo task in the list 
* **Json web token auth (jwt) :** ensure secure login in the system using access and refresh tokens 

---

##  frameworks and  Stack
* **Language:** Python 3.11 or higher 
* **Framework:** Django 5.2.7
* **API Toolkit:** Django REST Framework (DRF) 3.16.1
* **Authentication:** SimpleJWT 5.5.1
* **Database:** SQLite

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
git clone https://github.com/sbdev25/Todo_APP_BackendProject.git
cd Todo_APP_BackendProject
```
### 3. Setup Virtual Environment
```bash
python -m venv venv
cd venv
Scripts\activate
```
### 4. Install Dependencies
```bash
cd ..
pip install -r requirements.txt
```
### 5. Database Setup
```bash
python manage.py makemigrations
python manage.py migrate
```
### 6. Create an Admin User
You must create a superuser for the first time to access the Django dashboard and test the token APIs:
```bash
python manage.py createsuperuser
```
Follow the terminal prompts to set your username and password.

### 7. Run the Server
```bash
python manage.py runserver
```
The API will be available at: http://127.0.0.1:8000/

## ● Todo Model Fields
As per the challenge requirements, each Todo item includes:

* **id**: Auto-generated primary key.
* **user**: ForeignKey linked to the authenticated User.
* **title**: Character field (max 50).
* **description**: Text field (max 500).
* **isCompleted**: Boolean (default False).
* **createdAt**: Automatically generated timestamp.

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


##  Folder Structure Explanation

This project follows the **Django** standards  architecture.

### 1. The main directory (`todo_project/`)
This is the **Project Root**. It serves as the "brain" of the entire application.
* **`settings.py`**: The most important configuration file. It manages database connections, security keys, installed apps (like REST Framework), and JWT authentication settings.
* **`urls.py`**: The main entry point for routing. It tells Django which URL paths lead to which applications.

### 2. The Application Directory (`todo_app/`)
This is where the **Business Logic** of the Todo app lives.
* **`models.py`**: Defines the data structure. It describes exactly what a "Todo" is in the database (title, description, status, etc.).
* **`serializers.py`**: Acts as a translator. Since a database cannot "speak" JSON, the serializer converts complex Django models into JSON format for the frontend and validates incoming data.
* **`views.py`**: Contains the actual functions for your endpoints. It handles the logic for creating, updating, and deleting todos while checking user permissions.
* **`urls.py`**: Contains the specific paths for your API (like `/todos/add/` or `/todos/delete/`).

### 3. The Environment (`venv/`)
* This directory contains the **Virtual Environment**. It holds an isolated copy of Python and all the libraries listed in `requirements.txt`. This ensures that the project runs the same way on any computer without interfering with system-wide software.

### 4. Management & Dependencies
* **`manage.py`**: A command-line utility that allows you to interact with the project. You use it to run the server, create users, and sync the database.
* **`requirements.txt`**: The manifest of all necessary packages. It ensures that any developer can install the exact same versions of Django, DRF, and SimpleJWT that you used.
