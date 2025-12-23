# Step 3: Your First Django Project

## 🎯 What You'll Learn

In this step, you'll learn:
- How to create your first Django project
- Understanding every file Django creates
- What each file does (line by line)
- How to run your development server
- The difference between projects and apps

---

## 🚀 Part 1: Creating Your First Django Project

### What is a Django Project?

**Simple explanation:**
A Django project is like a house. It's the main container that holds everything together.

**Technical definition:**
A Django project is a collection of settings and configurations for an instance of Django. It contains one or more apps.

**Analogy:**
- **Project** = The entire house
- **App** = A room in the house (like kitchen, bedroom, etc.)
- You can have multiple apps (rooms) in one project (house)

### Step-by-Step: Creating a Project

**Step 1: Open your terminal/command prompt**

Make sure you're in the folder where you want to create your project.

**Step 2: Activate your virtual environment**

```bash
# Windows PowerShell
.\myenv\Scripts\Activate.ps1

# Windows CMD
myenv\Scripts\activate

# Mac/Linux
source myenv/bin/activate
```

You should see `(myenv)` at the beginning of your command line.

**Step 3: Create your project**

```bash
django-admin startproject myfirstproject
```

**Let's break this command down word by word:**

- `django-admin` = This is Django's command-line tool
  - Think of it as a special tool that knows how to create Django projects
  
- `startproject` = This is an action that means "create a new project"
  - It's like saying "build me a new house"
  
- `myfirstproject` = This is the name of your project
  - You can name it anything you want (no spaces, use lowercase and underscores)
  - Examples: `myblog`, `myshop`, `learning_django`

**What happens when you run this command?**

Django creates a folder structure like this:

```
myfirstproject/              ← Your project folder
├── manage.py                ← The control file
└── myfirstproject/          ← Settings folder (same name as project)
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
```

**🎉 Congratulations!** You just created your first Django project!

---

## 📁 Part 2: Understanding Project Structure (Line by Line)

Let's explore every file Django created and understand what each one does.

### The Outer Folder: `myfirstproject/`

**What it is:**
The main folder containing your entire project.

**Think of it as:**
The foundation of your house - everything sits on top of it.

**What's inside:**
- `manage.py` - The control file
- `myfirstproject/` - The settings folder

---

### File 1: `manage.py` - The Control Center

**Location:** `myfirstproject/manage.py`

**What it is:**
This is the most important file in your project. It's like the remote control for your Django project.

**Let's look at what's inside:**

```python
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myfirstproject.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
```

**Line-by-line explanation:**

**Line 1: `#!/usr/bin/env python`**
- This is called a "shebang" line
- It tells the computer: "Use Python to run this file"
- On Windows, this line is ignored, but it's good practice to keep it
- **Simple explanation:** "Hey computer, this is a Python file!"

**Line 2: `"""Django's command-line utility for administrative tasks."""`**
- This is a docstring (documentation)
- It describes what this file does
- **Simple explanation:** "This file helps you run Django commands"

**Line 3: `import os`**
- Imports the `os` module (operating system functions)
- Allows Python to interact with your computer's operating system
- **Simple explanation:** "Get tools to talk to the computer"

**Line 4: `import sys`**
- Imports the `sys` module (system-specific functions)
- Allows access to command-line arguments
- **Simple explanation:** "Get tools to read command-line commands"

**Line 7: `def main():`**
- Defines a function called `main`
- This is where the main code runs
- **Simple explanation:** "Here's the main program"

**Line 8: `"""Run administrative tasks."""`**
- Docstring explaining what the function does
- **Simple explanation:** "This function runs admin tasks"

**Line 9: `os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myfirstproject.settings')`**
- This is VERY important!
- `os.environ` = Environment variables (settings for your program)
- `setdefault` = "Set this value if it's not already set"
- `'DJANGO_SETTINGS_MODULE'` = The name of the setting
- `'myfirstproject.settings'` = The value (where to find settings)
- **Simple explanation:** "Tell Django where to find the settings file"

**Line 10: `try:`**
- Starts a try-except block (error handling)
- **Simple explanation:** "Try to do this, but if it fails, do something else"

**Line 11: `from django.core.management import execute_from_command_line`**
- Imports a function from Django
- `execute_from_command_line` = A function that runs Django commands
- **Simple explanation:** "Get the tool that runs Django commands"

**Line 12: `except ImportError as exc:`**
- If importing fails, catch the error
- `ImportError` = Error when Python can't find a module
- **Simple explanation:** "If we can't find Django, do this instead"

**Line 13-16: The error message**
- Shows a helpful error if Django isn't installed
- **Simple explanation:** "Tell the user what went wrong"

**Line 17: `execute_from_command_line(sys.argv)`**
- This runs the Django command
- `sys.argv` = The command you typed (like "runserver")
- **Simple explanation:** "Run the Django command the user asked for"

**Line 20: `if __name__ == '__main__':`**
- This checks if the file is being run directly (not imported)
- **Simple explanation:** "Only run this if someone runs this file directly"

**Line 21: `main()`**
- Calls the main function
- **Simple explanation:** "Start the program"

**Summary:**
`manage.py` is the entry point. When you type `python manage.py runserver`, it:
1. Sets up Django settings
2. Imports Django's command runner
3. Runs the command you asked for

**You rarely edit this file!** Django creates it and manages it for you.

---

### The Inner Folder: `myfirstproject/myfirstproject/`

**What it is:**
This is the settings folder. It has the same name as your project.

**Why two folders with the same name?**
- Outer folder = Your project container
- Inner folder = Django's configuration folder

**Think of it as:**
- Outer folder = The house
- Inner folder = The control room with all the switches and settings

---

### File 2: `__init__.py` - The Package Marker

**Location:** `myfirstproject/myfirstproject/__init__.py`

**What it is:**
This file is usually empty! Its only job is to tell Python: "This folder is a Python package."

**What's inside:**
Usually nothing, or sometimes:
```python
# This file makes Python treat this directory as a package
```

**Line-by-line explanation:**

**If it's empty:**
- An empty file is fine!
- Python just needs this file to exist
- **Simple explanation:** "This folder contains Python code"

**If it has a comment:**
- Comments start with `#`
- They're notes for humans, Python ignores them
- **Simple explanation:** "This is just a note, not actual code"

**Why is it needed?**
- Python needs this file to import code from this folder
- Without it, Python won't recognize this as a package
- **Simple explanation:** "This is like a sign that says 'Python code lives here'"

**You rarely edit this file!** It's usually left empty.

---

### File 3: `settings.py` - The Configuration File

**Location:** `myfirstproject/myfirstproject/settings.py`

**What it is:**
This is the MOST IMPORTANT configuration file. It's like the control panel for your entire Django project.

**Think of it as:**
The settings menu on your phone - it controls how everything works.

**Let's look at the key parts:**

#### Section 1: Path Configuration

```python
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
```

**Line-by-line:**

**Line 1: `from pathlib import Path`**
- Imports the `Path` class for handling file paths
- **Simple explanation:** "Get tools to work with file and folder locations"

**Line 4: `BASE_DIR = Path(__file__).resolve().parent.parent`**
- `__file__` = The current file (settings.py)
- `.resolve()` = Get the absolute path
- `.parent` = Go up one folder (to myfirstproject folder)
- `.parent` again = Go up one more folder (to the project root)
- `BASE_DIR` = The root folder of your project
- **Simple explanation:** "Find the main folder of this project"

**Why is this important?**
- Django uses `BASE_DIR` to find other files
- It's like having a home address for your project

#### Section 2: Secret Key

```python
SECRET_KEY = 'django-insecure-...'
```

**What it is:**
A secret code used for security (encryption, sessions, etc.)

**Simple explanation:**
Like a password that Django uses to keep things secure.

**⚠️ IMPORTANT:**
- Never share this key publicly!
- In production, use environment variables
- Django generates a random one for you

#### Section 3: Debug Mode

```python
DEBUG = True
```

**What it is:**
Controls whether Django shows detailed error messages.

**Simple explanation:**
- `DEBUG = True` = Show detailed errors (good for learning)
- `DEBUG = False` = Hide errors (good for production)

**When developing:** Keep it `True`
**When live:** Change to `False`

#### Section 4: Allowed Hosts

```python
ALLOWED_HOSTS = []
```

**What it is:**
A list of domain names that can host your site.

**Simple explanation:**
Like a guest list - only these websites can serve your Django app.

**For development:** Leave it empty `[]`
**For production:** Add your domain: `['yourdomain.com']`

#### Section 5: Installed Apps

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

**What it is:**
A list of apps (features) that Django should use.

**Line-by-line:**

- `'django.contrib.admin'` = Admin interface (manage your site)
- `'django.contrib.auth'` = User authentication (login, logout)
- `'django.contrib.contenttypes'` = Content type framework
- `'django.contrib.sessions'` = Session framework (remember users)
- `'django.contrib.messages'` = Messaging framework (show messages to users)
- `'django.contrib.staticfiles'` = Handle static files (CSS, images, JS)

**Simple explanation:**
These are like built-in apps that Django includes. You can add your own apps here later!

#### Section 6: Middleware

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

**What it is:**
Middleware are like filters that process every request.

**Simple explanation:**
Like security guards that check everything before it reaches your code.

**You usually don't need to change this!**

#### Section 7: URL Configuration

```python
ROOT_URLCONF = 'myfirstproject.urls'
```

**What it is:**
Tells Django where to find your URL patterns.

**Simple explanation:**
"Go to this file to see which URLs do what"

#### Section 8: Database

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

**What it is:**
Database configuration.

**Line-by-line:**

- `'ENGINE'` = What database to use (SQLite by default)
- `'NAME'` = Where to store the database file
- `BASE_DIR / 'db.sqlite3'` = In the project root, file named db.sqlite3

**Simple explanation:**
"Store data in a file called db.sqlite3 in the project folder"

**SQLite** = A simple database that's perfect for learning (it's just a file!)

#### Section 9: Password Validators

```python
AUTH_PASSWORD_VALIDATORS = [
    # ... password validation rules
]
```

**What it is:**
Rules for how strong passwords must be.

**Simple explanation:**
"Make sure users create strong passwords"

#### Section 10: Internationalization

```python
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
```

**What it is:**
Language and timezone settings.

**Simple explanation:**
- `LANGUAGE_CODE` = Default language (English US)
- `TIME_ZONE` = Default timezone (UTC)
- `USE_I18N` = Enable internationalization (multiple languages)
- `USE_TZ` = Use timezone-aware datetimes

#### Section 11: Static Files

```python
STATIC_URL = 'static/'
```

**What it is:**
Where to find static files (CSS, JavaScript, images).

**Simple explanation:**
"Static files (like CSS) are in the 'static' folder"

#### Section 12: Default Primary Key

```python
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
```

**What it is:**
Default type for auto-generated IDs in database tables.

**Simple explanation:**
"When Django creates an ID number, use this type"

---

### File 4: `urls.py` - The URL Router

**Location:** `myfirstproject/myfirstproject/urls.py`

**What it is:**
This file tells Django which page to show for each URL.

**Think of it as:**
A map that says "if someone visits /home, show the home page"

**What's inside:**

```python
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
```

**Line-by-line explanation:**

**Line 1: `from django.contrib import admin`**
- Imports the admin module
- **Simple explanation:** "Get the admin tools"

**Line 2: `from django.urls import path`**
- Imports the `path` function
- **Simple explanation:** "Get the tool to create URL patterns"

**Line 4: `urlpatterns = [`**
- Creates a list of URL patterns
- **Simple explanation:** "Here's the list of URLs and what they do"

**Line 5: `path('admin/', admin.site.urls),`**
- `path()` = Creates a URL pattern
- `'admin/'` = The URL (if someone visits /admin/)
- `admin.site.urls` = Show the admin page
- **Simple explanation:** "If someone visits /admin/, show them the admin page"

**This is where you'll add your own URLs later!**

---

### File 5: `wsgi.py` - The Web Server Interface

**Location:** `myfirstproject/myfirstproject/wsgi.py`

**What it is:**
WSGI = Web Server Gateway Interface. It connects your Django app to web servers.

**Simple explanation:**
Like a translator between your Django code and the web server.

**What's inside:**

```python
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myfirstproject.settings')

application = get_wsgi_application()
```

**Line-by-line:**

**Line 1: `import os`**
- Import operating system functions
- **Simple explanation:** "Get tools to work with the computer"

**Line 2: `from django.core.wsgi import get_wsgi_application`**
- Import the WSGI application function
- **Simple explanation:** "Get the tool that connects Django to web servers"

**Line 4: `os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myfirstproject.settings')`**
- Set the settings module
- **Simple explanation:** "Tell Django where the settings are"

**Line 6: `application = get_wsgi_application()`**
- Create the WSGI application
- **Simple explanation:** "Create the connection between Django and the web server"

**You rarely edit this file!** It's for production deployment.

---

### File 6: `asgi.py` - The Async Server Interface

**Location:** `myfirstproject/myfirstproject/asgi.py`

**What it is:**
ASGI = Asynchronous Server Gateway Interface. For async features (like WebSockets).

**Simple explanation:**
Like WSGI, but for modern async features (you'll learn this later).

**You won't need this for basic projects!**

---

## 🏃 Part 3: Running the Development Server

### What is the Development Server?

**Simple explanation:**
A mini web server on your computer that lets you see your website.

**Think of it as:**
A practice server - not for real users, just for you to test your website.

### How to Run the Server

**Step 1: Navigate to your project folder**

```bash
cd myfirstproject
```

**Step 2: Make sure virtual environment is activated**

You should see `(myenv)` in your terminal.

**Step 3: Run the server**

```bash
python manage.py runserver
```

**Let's break this down:**

- `python` = Run Python
- `manage.py` = The control file
- `runserver` = The command to start the server

**What you'll see:**

```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
December 23, 2025 - 11:00:00
Django version 4.2.7, using settings 'myfirstproject.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

**What this means:**

- `Watching for file changes` = Django will reload when you change files
- `System check identified no issues` = Everything is working!
- `Starting development server at http://127.0.0.1:8000/` = Your website is running!

### Viewing Your Website

1. **Open your web browser**
2. **Go to:** `http://127.0.0.1:8000/` or `http://localhost:8000/`
3. **You should see:** A Django welcome page! 🎉

**What is 127.0.0.1?**
- It's called "localhost"
- It means "this computer"
- **Simple explanation:** "The website is on your own computer"

**What is :8000?**
- It's the port number
- Like a door number for your website
- **Simple explanation:** "Use door number 8000"

### Stopping the Server

Press `CTRL + C` (or `CTRL + BREAK` on Windows)

---

## 📱 Part 4: Understanding Apps vs Projects

### What's the Difference?

This is a common confusion for beginners!

**Project:**
- The entire website
- Contains settings and configuration
- Can have multiple apps
- **Analogy:** The entire house

**App:**
- A specific feature or part of the website
- Does one thing (like a blog, or user accounts)
- Can be reused in other projects
- **Analogy:** A room in the house

### Examples

**Project: "My Blog Website"**
- **App 1:** Blog (for blog posts)
- **App 2:** Comments (for comments on posts)
- **App 3:** Users (for user accounts)

**Project: "E-commerce Site"**
- **App 1:** Products (for product listings)
- **App 2:** Cart (for shopping cart)
- **App 3:** Checkout (for payment)
- **App 4:** Users (for customer accounts)

### When to Create an App?

Create a new app when you want to add a new feature:
- Blog functionality → `blog` app
- User authentication → `users` app (or use Django's built-in)
- Product catalog → `products` app

### How to Create an App

```bash
python manage.py startapp blog
```

**Breaking it down:**
- `python manage.py` = Use the control file
- `startapp` = Create a new app
- `blog` = Name of the app

**We'll learn more about apps in the next lessons!**

---

## ✅ Checklist: First Project Complete

Before moving forward, make sure you can:

- [ ] Create a Django project: `django-admin startproject myproject`
- [ ] Understand what `manage.py` does
- [ ] Understand what `settings.py` does
- [ ] Understand what `urls.py` does
- [ ] Run the development server: `python manage.py runserver`
- [ ] View your website in a browser
- [ ] Stop the server with CTRL+C
- [ ] Explain the difference between a project and an app

---

## 🎓 Key Concepts Summary

1. **Project** = The entire website (the house)
2. **App** = A feature of the website (a room)
3. **manage.py** = The control center for your project
4. **settings.py** = Configuration file (the control panel)
5. **urls.py** = URL router (the map)
6. **Development Server** = A test server on your computer
7. **localhost:8000** = Your website's address during development

---

## 🐛 Troubleshooting

### Problem: "Command not found: django-admin"

**Solution:**
- Make sure virtual environment is activated
- Make sure Django is installed: `pip install django`
- Try: `python -m django startproject myproject`

### Problem: "Port 8000 is already in use"

**Solution:**
- Another program is using port 8000
- Use a different port: `python manage.py runserver 8080`
- Or stop the other program using port 8000

### Problem: "ModuleNotFoundError: No module named 'django'"

**Solution:**
- Virtual environment is not activated
- Django is not installed
- Activate virtual environment and install Django

---

## 🚀 What's Next?

Congratulations! You've created your first Django project! 🎉

In the next lessons, you'll learn:
- How to create apps
- How to create models (database tables)
- How to create views (the logic)
- How to create templates (the display)

Keep practicing and experimenting!

---

## 💡 Pro Tips

1. **Always activate your virtual environment** before working
2. **Keep the server running** while developing (it auto-reloads on changes)
3. **Don't edit manage.py** - Django manages it
4. **One project, many apps** - that's the Django way
5. **Experiment!** Try changing settings and see what happens

---

## 🎉 Congratulations!

You've completed Week 1-2! You now know:
- ✅ What Django is
- ✅ How to set up your environment
- ✅ How to create a Django project
- ✅ How to run a development server
- ✅ What each file does

You're ready to start building real features! Keep learning! 💪

