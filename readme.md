# Personal Expense Tracker

## Overview

Personal Expense Tracker is a simple web application built using Django that helps users manage their daily income and expenses. It provides an easy way to add, edit, delete, and categorize transactions while giving a quick overview of financial activity.

This project was created to practice Django fundamentals, including URL routing, views, templates, models, and CRUD operations.

---

## Features

- Add income and expense records
- Edit existing transactions
- Delete transactions
- Categorize transactions
- View expense summary
- Simple and responsive user interface

---

## Technologies Used

- Python
- Django
- HTML
- CSS
- Bootstrap
- SQLite
- Git & GitHub

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Appajireddyv/personal-ExpenseTracker-API.git
cd expense_tracker
```

### 2. Create a virtual environment

```bash
python -m venv env
```

### 3. Activate the virtual environment

**Windows**

```bash
env\Scripts\activate
```

**Linux/macOS**

```bash
source env/bin/activate
```

### 4. Install the required packages

```bash
pip install -r requirements.txt
```

---

## Running the Application

Move to the source directory:

```bash
cd src
```

Apply database migrations:

```bash
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

Open your browser and visit:

```
http://127.0.0.1:8000/
```
---
## Running Tests

Run the following command from the `src` directory:

```bash
python manage.py test
```

## Author

**Appaji Reddy**

