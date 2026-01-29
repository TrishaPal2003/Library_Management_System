# Library Management System

A **web-based Library Management System** built using **Django** and **Python** for backend and **HTML/CSS** for frontend.  
This is a **Database Course Final Project** demonstrating CRUD operations, relational data management, and professional UI design.

---

## 📌 Project Overview

This system allows a library to manage:

- Books (add, list, view)
- Members (add, list, view)
- Issue and return of books
- Borrow history tracking

The project uses **Django’s ORM** for database management and provides a **clean, professional interface** for academic use.

---

## 🛠 Technologies Used

- **Backend:** Python, Django  
- **Frontend:** HTML, CSS  
- **Database:** SQLite (default Django DB, easy setup)  
- **Version Control:** Git & GitHub

---

## 🚀 Features

1. **Books Management**
   - Add new books
   - List all books
   - View book details (title, author, ISBN, quantity)

2. **Members Management**
   - Add new members
   - List all members
   - View member details (ID, name, department, email, phone)

3. **Issue & Return**
   - Issue a book to a member
   - Track return status
   - Automatically updates book quantity

4. **Borrow History**
   - Displays all issued books
   - Shows status: Issued / Returned
   - Return button available for active issues

5. **Professional UI**
   - Single CSS file for all pages
   - Responsive, clean, and readable layout
   - Home page with navigation to all features

---

## 📂 Project Structure

Library_Management/
├── backend/
│ ├── library/
│ │ ├── models/
│ │ ├── templates/library/
│ │ ├── static/library/css/form.css
│ │ ├── views/
│ │ └── urls.py
│ ├── core/
│ │ └── urls.py
│ └── settings.py
├── README.md
├── manage.py
└── venv/