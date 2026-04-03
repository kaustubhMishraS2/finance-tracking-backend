#  Finance Tracking Backend System

##  Overview

This project is a backend system built using **Python (Django + Django REST Framework)** to manage financial transactions such as income and expenses.

It allows users to register, log in, and manage their own financial records with filtering, validation, and summary features.

---

##  Features

###  Core Functionality

* Create, Read, Update, Delete (CRUD) transactions
* User registration and login
* User-specific data access (each user sees only their own data)

###  Filtering

* Filter by category
* Filter by transaction type (income/expense)

###  Summary Analytics

* Total Income
* Total Expense
* Balance Calculation

###  Validation

* Amount must be greater than zero
* Category cannot be empty
* Valid transaction type required
* Username uniqueness
* Password validation

###  Security

* User-based data isolation
* Session authentication

###  Additional Enhancements

* Pagination for transaction listing
* Admin panel for data management

---

##  Project Structure

```
finance_system/
│
├── finance/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│
├── finance_system/
│   ├── settings.py
│   ├── urls.py
│
├── templates/ (optional UI)
├── manage.py
```

---

##  Tech Stack

* Python
* Django
* Django REST Framework
* SQLite

---

##  Setup Instructions

###  Clone the repository

```bash
git clone <https://github.com/kaustubhMishraS2/finance-tracking-backend.git>
cd finance_system
```

###  Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

###  Install dependencies

```bash
pip install django djangorestframework
```

###  Apply migrations

```bash
python manage.py migrate
```

###  Create superuser

```bash
python manage.py createsuperuser
```

###  Run server

```bash
python manage.py runserver
```

---

##  API Endpoints

###  Authentication

* Register → `/api/register/`
* Login → `/api-auth/login/`

---

###  Transactions (CRUD)

* GET → `/api/transactions/`
* POST → `/api/transactions/`
* GET (single) → `/api/transactions/<id>/`
* PUT/PATCH → `/api/transactions/<id>/`
* DELETE → `/api/transactions/<id>/`

---

###  Filtering

* `/api/transactions/?category=Food`
* `/api/transactions/?type=income`

---

###  Summary

* `/api/transactions/summary/`

---

##  How to Test

1. Register a new user
2. Login using `/api-auth/login/`
3. Add transactions
4. Test CRUD operations
5. Apply filters
6. Check summary endpoint

---

##  Assumptions

* Each user manages their own financial data
* Backend-focused project (no full frontend)
* Basic authentication used for simplicity

---

##  Notes

This project is designed for evaluation purposes and focuses on:

* Clean backend structure
* Logical implementation
* Practical API design
* Reliable and maintainable code

---

#  Assignment Explanation

##  Role-Based Access Design

* Viewer → Can view records and summary
* Analyst → Can filter and analyze data
* Admin → Manage records via Django Admin

User-based filtering ensures data isolation:

```
Transaction.objects.filter(user=request.user)
```

---

##  API Design

* Structured using Django REST Framework
* ModelViewSet used for CRUD operations
* Clean and scalable routing

---

##  Validation & Error Handling

* Input validation implemented
* Proper error messages
* Correct HTTP status codes used

---

##  Database

* SQLite database
* Django ORM used
* Structured and reliable persistence

---

##  Code Quality

* Clean and modular structure
* Separation of concerns
* Readable and maintainable code

---

##  Optional Enhancements

* Authentication
* Pagination
* Filtering
* Admin panel

---

##  Conclusion

This project demonstrates a clean and structured backend system using Django REST Framework with strong fundamentals, proper validation, and practical API design.

---

##  Developer

**Kaustubh Mishra**
