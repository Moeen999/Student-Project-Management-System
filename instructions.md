# Student Project Management System

A Django-based **Student Project Management System** designed to manage academic projects efficiently.  
This system allows students and to manage project records, submissions, and evaluations in a structured way.

Developed as an **academic Web Engineering project**, following proper Django project architecture and coding practices.

---

## 📌 Project Overview

The **Student Project Management System** is built to simplify the management of student projects in educational institutions.  
It provides a centralized platform where:

- Students can submit project details,edit if project is in pending state.
- teachers can review and manage projects, teachers can reject or approve the project also they can mention the rejecttion reason.
- Project records are stored securely

---

## 🛠 Technologies Used

- **Backend:** Python, Django
- **Frontend:** HTML, CSS (Django Templates)
- **Database:** SQLite (Django default)
- **Environment:** Virtual Environment (venv)

---

## 📂 Project Structure

Student_Project_Management_System/
│
├── manage.py
│
├── student_project_system/ # Main Django Project
│ ├── settings.py
│ ├── urls.py
│ ├── asgi.py
│ └── wsgi.py
│
├── accounts/ # Django App
│ ├── migrations/
│ ├── models.py
│ ├── views.py
│ ├── admin.py
│ └── apps.py
│ └── forms.py
│ └── urls.py
|
├── projects/ # Django App
│ ├── migrations/
│ ├── models.py
│ ├── views.py
│ ├── admin.py
│ └── apps.py
│ └── forms.py
│ └── urls.py
│
├── templates/
│ └── base.html
│ ├── project_add.html
│ └── project_edit.html
│ └── project_review.html
│ └── login.html
│ └── register.html
│ └── teacher_dashboard.html
│ └── dashboard.html
│
├── static/
│ └── css/
│ └── style.css
│
├── venv/ # Virtual environment
│
└── README.md

---

## ⚙️ How the System Works

1. Students submit project information (title, description, technology, supervisor).
2. Project data is validated and stored in the database.
3. teachers can view, update, or evaluate submitted projects.
4. Admin panel allows full control over users and project records.
5. All project information remains organized and easily accessible.

---

## 🚀 How to Run the Project

### 1️⃣ Download or Clone the Project

Place the project folder on your local machine.

---

### 2️⃣ Activate Virtual Environment

**Windows**

venv\Scripts\activate

---

### 3️⃣ Install Dependencies

pip install django

---

### 4️⃣ Run Migrations

python manage.py makemigrations
python manage.py migrate

---

### 5️⃣ Start Development Server

python manage.py runserver

---

### 6️⃣ Open in Browser

http://127.0.0.1:8000/

---

## 🧪 Admin Panel

Create admin user:

python manage.py createsuperuser

Admin login:

http://127.0.0.1:8000/admin/

---

## 📈 Features

- Student project submission
- Project listing and management
- Secure data storage
- Clean MVC-based Django structure

---

## 🎓 Academic Purpose

This project demonstrates:

- Django MVC architecture
- CRUD operations
- Backend–frontend integration
- Database management
- Real-world academic system design

---

## 📌 Future Enhancements

- User authentication (Student / teachers roles)
- Project grading system
- File upload for project reports
- Search and filter functionality
- Deployment on cloud platform

---

## 👤 Author

**Student Name:** (Muhammad Moeen (F23BDOCS1E02086))
**Program:** BS Computer Science 1E
**Course:** Web Engineering

---

## 👤 Testing Accounts

👤 Teacher Testing Account:
username: "testteacher1"
password: "12345678"

👤 Teacher Student Account:
username: "teststd1"
password: "12345678"

---

## Access complete code here at Github:
Repository Link: https://github.com/Moeen999/Student-Project-Management-System
---

## ✅ License

This project is intended for **academic and educational use only**.
