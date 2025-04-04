# Django E-commerce Product Catalog

A Django-based e-commerce product catalog application with search and filtering capabilities.

## Quick Start Guide

Follow these steps to run the e-commerce project:

### 1. Clone the repository

```bash
git clone https://github.com/Hruthik-T/django_assignment.git
cd django_assignment
```

### 2. Navigate to the project directory

```bash
cd ecommerce_project
```

### 3. Install Django

```bash
pip install django
```

### 4. Apply database migrations

```bash
python manage.py migrate
```

### 5. Populate the database with sample data

```bash
python populate_db.py
```

This script will create:
- 6 product categories
- 12 tags
- 20 sample products with descriptions, prices, and relationships

### 6. Run the development server

```bash
python manage.py runserver
```

### 7. Access the application

- product catalog: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)



