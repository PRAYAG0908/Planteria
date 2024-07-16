# Planteria

Planteria is Ecommerce Web-Application with PayPal Payment Integration. Planteria uses Django as backend.

## Installation

### Prerequisites
- Python (version above 3.6)
- Django 
- python -dotenv *(optional)*

### Steps to Install

1. **Clone the repository**
   ```bash
   git clone https://github.com/PRAYAG0908/Planteria.git
   cd ecommerce
   ```

2. **Setup Virtual Environment** (Optional but recommended)
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Perform Migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a Superuser** (Optional, for admin access)
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```

7. **Access the Application**
   Open a web browser and go to `http://localhost:8000/` to see the application running.
