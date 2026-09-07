# Django + HTMX + Alpine.js + Tailwind Starter

A simple, modern starter template using:

- **Django** – backend
- **HTMX** – dynamic interactions without writing much JavaScript
- **Alpine.js** – lightweight reactivity
- **Tailwind CSS** – utility-first styling

## Features

- Pure Tailwind (no DaisyUI)
- django-htmx integration
- django-tailwind (npm mode)
- Live reload with django-browser-reload
- Clean project structure

## Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/django-htmx-alpine-tailwind.git
cd django-htmx-alpine-tailwind

# 2. Create virtual environment
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Install Tailwind dependencies
python manage.py tailwind install

# 5. Run the project
python manage.py tailwind start          # Terminal 1
python manage.py runserver               # Terminal 2