# Django CRUD Application with Error Injection

This is a simple Django application that demonstrates CRUD (Create, Read, Update, Delete) functionality with user authentication and error injection for testing purposes.

## Features

- User authentication (login/logout)
- Book management (create, read, update, delete)
- Error injection for testing
- Proper error handling and redirection

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Virtualenv (recommended)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/MarcusCJH/SampleDjangoCRUD.git
   cd SampleDjangoCRUD
   
2. **Create a virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   
3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   
4. **Set up the database:**
   ```bash
   python manage.py migrate

5. **Create a superuser:**
    ```bash
   python manage.py createsuperuser

6. **Run the development Server:**
    ```bash
   python manage.py runserver

7. **Access the Application:**

   Open your browser and go to http://127.0.0.1:8000/.

## Testing Error Injection

To test the error injection, you can perform the following actions:

- Raise a ValueError: Create a book with the title "Error". 
- Trigger a 404 error: Access a book detail page with the title "Not Found". 
- Cause a form validation error: Create a book with the title "Invalid".

