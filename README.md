# Django Blog Project

A feature-rich blog application built with Django, featuring user authentication, social login, RESTful API, and more.

## Features

- User registration and authentication system
- Social authentication with GitHub and Google
- Blog posts with tagging functionality
- Comment system for blog posts
- RESTful API using Django REST Framework
- API documentation with drf-spectacular
- Responsive design with Bootstrap 5
- PostgreSQL database integration

## Requirements

- Python 3.8+
- PostgreSQL
- Other dependencies listed in `requirements.txt`

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd Blog1Project_Django
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv .venv
   # On Windows
   .\.venv\Scripts\activate
   # On Unix or MacOS
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root with the following variables:
   ```
   SECRET_KEY='your_secret_key'
   
   # Social authentication (optional)
   GITHUB_KEY='your_github_key'
   GITHUB_SECRET='your_github_secret'
   GOOGLE_KEY='your_google_key'
   GOOGLE_SECRET='your_google_secret'
   
   # Database credentials
   DB_PASSWORD='your_db_password'
   
   # Email settings
   EMAIL_HOST_USER='your_email'
   EMAIL_HOST_PASSWORD='your_email_password'
   
   # Debug mode
   DEBUG=True  # Set to False in production
   ```

5. Set up the PostgreSQL database:
   - Create a database named 'blog'
   - Create a user named 'blog' with the password specified in your `.env` file
   - Grant all privileges on the database to the user

6. Apply migrations:
   ```
   python manage.py migrate
   ```

7. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

8. Run the development server:
   ```
   python manage.py runserver
   ```

9. Access the application at http://127.0.0.1:8000/

## API Documentation

The API documentation is available at `/api/schema/swagger-ui/` when the server is running.

## License

This project is open-source and available under the MIT License.
