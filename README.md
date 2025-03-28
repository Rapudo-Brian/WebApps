Django Multi-User Payment Service

Project Overview

This is a web-based multi-user payment service built with Django. Users can send and request money, view transactions, 
and manage accounts with multi-currency support (GBP, USD, EUR). 
The system ensures security with authentication, authorization, and protection against common web vulnerabilities.

Features.

1.User Registration & Authentication.
2.Multi-Currency Support (Automatic conversion between GBP, USD, and EUR).
3.Send & Request Money between users.
4.Transaction Management (View and approve/reject requests).
5.Admin Panel for managing users and transactions.

Security Features.

1.HTTPS (when deployed).
2.CSRF & XSS Protection.
3.SQL Injection Prevention.
4.Secure Authentication.

CURRENCY CONVERSION LOGIC.

The system uses hardcoded exchange rates for currency conversion.
Default currency: GBP (£)
Users choosing USD or EUR have their initial balance converted from 750 GBP using:

EXCHANGE_RATES = {
    ('GBP', 'EUR'): 1.16,
    ('GBP', 'USD'): 1.38,
    ('EUR', 'GBP'): 0.86,
    ('EUR', 'USD'): 1.18,
    ('USD', 'GBP'): 0.72,
    ('USD', 'EUR'): 0.85,
}
Transactions between different currencies are converted accordingly.

SECURITY FEATURES.

1.Authentication & Authorization (Django user model, login/logout).
2.Cross-Site Scripting (XSS) Protection (SECURE_BROWSER_XSS_FILTER = True).
3.Cross-Site Request Forgery (CSRF) Protection (CSRF_COOKIE_SECURE = True).
4.Clickjacking Protection (X_FRAME_OPTIONS = 'DENY').
5.SQL Injection Prevention (ORM queries instead of raw SQL).


INSTALLATION AND SETUP.

1.Extract the ZIP File.
2.Locate the downloaded ZIP file.
3.Extract it to your preferred directory.
4.Open the Project.
5.Open the extracted folder in your code editor (e.g., VS Code, PyCharm).
6.Set Up a Virtual Environment (Recommended).
7.Open a terminal inside the project folder and run: python3 -m venv venv
8.Activate the virtual environment:
   Linux/macOS:
     source venv/bin/activate
   Windows:
     venv\Scripts\activate
9.Install Dependencies.
10.Install required Python packages:
     pip install -r requirements.txt
11.Set Up the Database.
12.Apply database migrations:
     python manage.py migrate
13.Create a Superuser (For Admin Access)
 Run the command:
  python manage.py createsuperuser
Follow the prompts to set up an admin account. (Remember, For this project, the superuser/admin should have both username and password set as admin1).
14.Start the Django server:
   python manage.py runserver
15.Open your browser and visit:
http://127.0.0.1:8000/home/

16.(Optional) Load Default Data
If needed, load initial data using fixtures by running this command:
   python manage.py loaddata initial_data.json


Deployment Guide (Amazon EC2)

1.Set up an EC2 instance with Ubuntu or your OS.
2.Install dependencies (Python, pip, virtualenv).
3.Deploy the Django app (gunicorn, Nginx).
4.Configure HTTPS using Let's Encrypt SSL.
5.Set environment variables (DEBUG=False, ALLOWED_HOSTS)