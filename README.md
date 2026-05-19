# Gaming Website

A futuristic gaming website built with Django. This platform provides an immersive experience for gamers to browse, purchase, and read the latest news about video games.

## Features

- **Store**: Browse available games for purchase.
- **Checkout System**: Seamlessly place orders for different game editions (Standard, Deluxe, etc.).
- **User Library**: A personal space where authenticated users can view their purchased games.
- **Gaming Blog**: Read the latest articles and news in the gaming world.
- **User Authentication**: Secure user registration, login, and logout functionalities ("Neural ID" login system).
- **Responsive UI**: A modern, dark-themed, glassmorphic design tailored for gamers.

## Technologies Used

- **Backend**: Python, Django
- **Database**: SQLite3 (default for Django)
- **Frontend**: HTML5, CSS3, JavaScript
- **Deployment**: Configured for deployment (includes `Procfile` and `build.sh`)

## Project Structure

- `gamingproject/`: The main Django project configuration directory.
- `gameapp/`: The core Django application containing models, views, and templates.
    - `models.py`: Contains the `Post` (for blog) and `Order` (for purchases) models.
    - `views.py`: Logic for rendering pages (index, home, store, checkout, blog, login, library, etc.).
    - `templates/`: HTML templates for the website.
    - `static/`: Static files like CSS, JavaScript, and images.
- `populate_data.py`: A script to populate the database with initial sample data.

## Setup Instructions

### Prerequisites
- Python 3.8+
- pip (Python package installer)

### Installation

1. **Navigate to the project directory:**
   ```bash
   cd "Gaming Website"
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **Mac/Linux:**
     ```bash
     source venv/bin/activate
     ```

4. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Apply database migrations:**
   ```bash
   python manage.py migrate
   ```

6. **(Optional) Populate sample data:**
   You can use the provided script to add sample posts and data:
   ```bash
   python populate_data.py
   ```

7. **(Optional) Create a superuser for the admin panel:**
   ```bash
   python manage.py createsuperuser
   ```

8. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

9. **Access the Application:**
   Open your web browser and go to: `http://127.0.0.1:8000/`

## Admin Panel

You can access the Django admin panel by navigating to `http://127.0.0.1:8000/admin/` and logging in with your superuser credentials. From there, you can manage users, blog posts, and orders.
