# Full Stack Portfolio Website
Django + PostgreSQL + REST API + Email Integration

A production-ready portfolio website built using Django, PostgreSQL, Authentication, REST API, and Email Integration.

---

# 📌 Features

• Home, About, Projects, Contact pages  
• Slug-based project detail URLs  
• Admin-only dashboard  
• Project CRUD (Admin only)  
• Contact form with email notification  
• PostgreSQL integration  
• REST API endpoints  
• Environment variable security (.env)

---

# 🛠 Tech Stack

Backend:
- Python 3.11
- Django 5.x
- Django REST Framework
- PostgreSQL

Frontend:
- HTML
- CSS
- Bootstrap (Dark Premium UI)

---

# ==============================
# LOCAL SETUP (STEP BY STEP)
# ==============================

Follow all steps carefully.

---

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate it:

Windows:
```bash
venv\Scripts\activate
```

Mac/Linux:
```bash
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Install PostgreSQL

Download from:
https://www.postgresql.org/download/

After installation:

Open SQL Shell (psql) and create database:

```sql
CREATE DATABASE portfolio_db;
```

---

## 5️⃣ Create .env File

In project root (same folder as manage.py), create:

```
.env
```

Add the following:

```
SECRET_KEY=your_generated_secret_key
DEBUG=True

DB_NAME=portfolio_db
DB_USER=postgres
DB_PASSWORD=your_postgres_password
DB_HOST=localhost
DB_PORT=5432

EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_gmail_app_password
```

IMPORTANT:
`.env` must NOT be pushed to GitHub.

---

## 6️⃣ Generate Secret Key

Run:

```bash
python manage.py shell
```

Then:

```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

Copy the generated key into `.env`.

Exit shell.

---

## 7️⃣ Apply Database Migrations

```bash
python manage.py migrate
```

---

## 8️⃣ Create Admin User

```bash
python manage.py createsuperuser
```

Follow prompts.

---

## 9️⃣ Run Development Server

```bash
python manage.py runserver
```

Open browser:

```
http://127.0.0.1:8000
```

---

# 📧 EMAIL SETUP (Gmail SMTP)

1. Enable 2-Step Verification in Google account  
2. Generate App Password  
3. Add App Password in `.env`:

```
EMAIL_HOST_PASSWORD=your_generated_app_password
```

Restart server after updating.

---

# 🔐 Admin Panel

Visit:

```
http://127.0.0.1:8000/admin
```

Only admin can:
• Add projects  
• Access dashboard  
• Manage contact messages  

---

# 📡 REST API ENDPOINTS

GET all projects:
```
/api/projects/
```

GET single project:
```
/api/projects/<slug>/
```

POST create project (Admin only):
```
/api/projects/create/
```

POST contact message:
```
/api/contact/
```

---

# 🔒 Security

• SECRET_KEY stored in .env  
• Database credentials not pushed to GitHub  
• Email uses Gmail App Password  
• .env included in .gitignore  

---

# 🧪 Run Tests

```bash
python manage.py test
```

---

# Author

Dhirendra Singh Kaushik  
AI & Machine Learning Engineer  
LinkedIn: www.linkedin.com/in/dhirendra14  
GitHub: https://github.com/dhirendra345  
