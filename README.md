# Backend Wizards — Stage 0 Task (Django)

## Overview
This Django API provides a `/me` endpoint returning:
- Your profile (name, email, stack)
- Current UTC timestamp
- A random cat fact fetched from [Cat Facts API](https://catfact.ninja/fact)

## Stack
- Python 3
- Django
- Requests
- Gunicorn

## Local Setup
```bash
git clone https://github.com/<yourusername>/backend-wizards-stage0.git
cd backend-wizards-stage0
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
