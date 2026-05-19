# Student Record System

A complete Django web application for managing student records with a modern UI and functional admin panel.

## Features

- **Student Management**: Add, edit, delete, and view student records
- **Search & Filter**: Search by name or roll number, filter by course or minimum marks
- **Dashboard**: View total students, average marks, and top 5 performing students
- **Admin Panel**: Customized Django admin with search, filters, and all student fields
- **Form Validation**: Prevents duplicate roll numbers and validates marks
- **Responsive Design**: Modern Bootstrap 5 UI that works on all devices
- **Success Messages**: Django messages framework for user feedback

## Tech Stack

- **Backend**: Django 5.2
- **Database**: SQLite
- **Frontend**: Bootstrap 5, Bootstrap Icons
- **Views**: Class-based views (ListView, CreateView, UpdateView, DeleteView)

## Project Structure

```
Student Record System/
├── manage.py
├── requirements.txt
├── README.md
├── db.sqlite3
├── studentRecordSystem/          # Project configuration
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
└── students/                     # Students app
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── forms.py
    ├── views.py
    ├── dashboard_views.py
    ├── urls.py
    ├── migrations/
    └── templates/students/
        ├── base.html
        ├── student_list.html
        ├── student_form.html
        ├── student_confirm_delete.html
        └── dashboard.html
```

## Setup Instructions

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)

### Step 1: Navigate to the Project Directory

```bash
cd "D:\My Django Projects\Student Record System\Student Record System"
```

### Step 2: Create and Activate Virtual Environment (Optional but Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run Migrations

```bash
python manage.py migrate
```

### Step 5: Create Superuser (for Admin Panel Access)

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account.

### Step 6: Run the Development Server

```bash
python manage.py runserver
```

The application will be available at: **http://127.0.0.1:8000/**

### Step 7: Access the Admin Panel

Navigate to: **http://127.0.0.1:8000/admin/**

Login with the superuser credentials you created in Step 5.

## URL Routes

| URL | Description |
|-----|-------------|
| `/` | Student list (homepage) |
| `/add/` | Add new student |
| `/edit/<id>/` | Edit existing student |
| `/delete/<id>/` | Delete student |
| `/dashboard/` | Dashboard with statistics |
| `/admin/` | Django admin panel |

## Student Model Fields

| Field | Type | Description |
|-------|------|-------------|
| name | CharField | Student's full name |
| roll_number | CharField (unique) | Unique roll number |
| email | EmailField | Student's email address |
| course | CharField | Enrolled course |
| marks | FloatField | Student's marks/score |
| created_at | DateTimeField | Record creation timestamp |

## Development

### Running Tests

```bash
python manage.py test
```

### Collect Static Files (for Production)

```bash
python manage.py collectstatic
```

## Screenshots

The application features:
- Clean navbar with navigation links
- Dashboard cards showing key statistics
- Search and filter functionality
- Color-coded marks badges (green for 90+, blue for 70+, yellow for 50+, red for below 50)
- Responsive table with pagination
- Form validation with error messages
- Delete confirmation page

## License

MIT License
