# Online Job Portal

A Django web application where **employers** post jobs and **job seekers** search, apply, and track their applications and interviews.

## Features

- **Accounts** – register, log in and out, two roles (Job Seeker / Employer), job seeker profile with CV upload.
- **Jobs** – employers create, view, edit and delete job posts (full CRUD). Anyone can browse and search jobs by title, location and category.
- **Applications** – job seekers apply with a cover letter and CV. Employers review applicants, accept or reject them, and schedule interviews.
- **Messaging** – users send and read messages in an inbox.
- **Dashboard** – overview page, user profile and reports.
- **Admin panel** – manage every model at `/admin/`.

## Tech stack

- Python 3 and Django
- SQLite database
- Django templates with HTML, CSS and Bootstrap

## Database models and relationships

| Model | App | Relationships |
|-------|-----|---------------|
| `User` (custom, has `role`) | accounts | – |
| `JobSeekerProfile` | accounts | One-to-one with `User` |
| `UserProfile` | dashboard | One-to-one with `User` |
| `Category` | jobs | – |
| `Job` | jobs | Many-to-one with `User` (employer) and `Category` |
| `JobApplication` | applications | Many-to-one with `User` (applicant) and `Job` |
| `Interview` | applications | Many-to-one with `JobApplication` |
| `Message` | messaging | Many-to-one with `User` (sender) and `User` (receiver) |

## How to run the project

1. Install [Python 3](https://www.python.org/downloads/) and [Git](https://git-scm.com/downloads).
2. Clone the repository:
   ```bash
   git clone https://github.com/cadnanahmed62-pixel/Online-job-portal.git
   cd Online-job-portal
   ```
3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate        # Windows
   source venv/bin/activate     # macOS / Linux
   ```
4. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Create the database tables:
   ```bash
   python manage.py migrate
   ```
6. Create an admin account:
   ```bash
   python manage.py createsuperuser
   ```
7. Start the server:
   ```bash
   python manage.py runserver
   ```
8. Open http://127.0.0.1:8000/ in your browser.

> **Tip:** Log in to `/admin/` and add a few **Categories** before you post jobs. Employer accounts must be approved (`is_employer_approved`) in the admin panel before they can post jobs.

## Main URLs

| URL | Page |
|-----|------|
| `/jobs/` | Job list and search |
| `/accounts/register/` | Register |
| `/accounts/login/` | Log in |
| `/dashboard/` | Dashboard |
| `/applications/my-applications/` | Job seeker's applications |
| `/applications/employer-applications/` | Employer's applicants |
| `/messages/` | Inbox |
| `/admin/` | Admin panel |

## Group members and responsibilities

See [CONTRIBUTORS.md](CONTRIBUTORS.md).
