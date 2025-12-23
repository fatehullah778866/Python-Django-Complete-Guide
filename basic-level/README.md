# Basic Level - Weeks 1-8: Django Fundamentals

Welcome to your Django learning journey! 🎉

This folder contains detailed, beginner-friendly guides for your first eight weeks of learning Django. Each step is explained in simple terms, as if you're learning for the first time, with line-by-line explanations and Windows-specific commands.

## 📚 What You'll Learn

In these first eight weeks, you'll learn:

**Weeks 1-2: Introduction & Setup**
1. **What Django is and why we use it** - Understanding the basics
2. **How to set up your computer** - Getting everything ready
3. **How to create your first Django project** - Building something real!

**Weeks 3-4: Models & Database**
4. **Django Models** - Creating database structures
5. **Database Migrations** - Saving your models to the database
6. **Django Admin Interface** - Managing your data easily

**Weeks 5-6: Views & Templates**
7. **URL Routing** - Connecting URLs to pages
8. **Views** - The logic that handles requests
9. **Templates** - Creating beautiful HTML pages

**Weeks 7-8: Forms & Complete App**
10. **Django Forms** - Creating and handling forms
11. **Building a Complete App** - CRUD operations and integration

## 📖 Step-by-Step Guides

Follow these guides in order:

### Weeks 1-2: Introduction & Setup

1. [Step 1: Understanding Django](./step-1-understanding-django.md)
   - Learn what Django is
   - Understand why we use it
   - Learn Django's philosophy (DRY, MVT pattern)
   - Django vs other frameworks
   - Django project structure

2. [Step 2: Environment Setup](./step-2-environment-setup.md)
   - Install Python and pip
   - Create virtual environments
   - Install Django
   - Set up IDE/Editor (VS Code, PyCharm)
   - Understanding `django-admin` and `manage.py`
   - **All commands are Windows-specific!**

3. [Step 3: Your First Django Project](./step-3-first-django-project.md)
   - Creating a project: `django-admin startproject`
   - Understanding project structure (line by line!)
   - Running the development server
   - Creating your first app: `python manage.py startapp`
   - Understanding apps vs projects

### Weeks 3-4: Models & Database

4. [Step 4: Django Models](./step-4-django-models.md)
   - Understanding Django ORM
   - Creating your first model
   - Model fields and field types (explained simply!)
   - Model relationships (ForeignKey, ManyToMany, OneToOne)
   - Model methods and properties
   - `__str__` method and Meta options

5. [Step 5: Database Migrations](./step-5-database-migrations.md)
   - Understanding migrations
   - Creating migrations: `makemigrations`
   - Applying migrations: `migrate`
   - Migration files and rollback
   - Data migrations
   - **Windows commands included!**

6. [Step 6: Django Admin Interface](./step-6-django-admin.md)
   - Activating admin site
   - Creating superuser
   - Registering models
   - Customizing admin interface
   - Admin actions and filters

### Weeks 5-6: Views & Templates

7. [Step 7: URL Routing](./step-7-url-routing.md)
   - Understanding URLconf
   - URL patterns and parameters
   - Named URLs and reverse()
   - URL namespaces
   - Including other URLconfs

8. [Step 8: Views](./step-8-views.md)
   - Function-based views (FBV)
   - Class-based views (CBV) basics
   - Request and response objects
   - HTTP methods (GET, POST)
   - View decorators (@login_required, @csrf_exempt)

9. [Step 9: Templates](./step-9-templates.md)
   - Django template language (DTL)
   - Template inheritance
   - Template tags and filters
   - Static files (CSS, JS, images)
   - Template context

### Weeks 7-8: Forms & Complete App

10. [Step 10: Django Forms](./step-10-django-forms.md)
    - Creating forms
    - Form fields and widgets
    - Form validation
    - Rendering forms in templates
    - Handling form submissions
    - ModelForms
    - **Windows commands included!**

11. [Step 11: Building a Complete App](./step-11-building-complete-app.md)
    - Create a complete blog application
    - CRUD operations (Create, Read, Update, Delete)
    - Integrating all concepts learned
    - Building a working Django application from scratch
    - **Step-by-step project walkthrough!**

## 🎯 Learning Tips

- **Take your time**: Don't rush! Understanding the basics is important
- **Practice**: Try typing the commands yourself instead of copy-pasting
- **Ask questions**: If something doesn't make sense, look it up or ask for help
- **Experiment**: Try changing things and see what happens (you can't break anything!)
- **Follow in order**: Each step builds on the previous one
- **Read line-by-line**: Every code example is explained in detail
- **Use Windows commands**: All terminal commands are for Windows PowerShell/CMD

## ✅ Checklist

Before moving to the intermediate level, make sure you can:

### Weeks 1-2
- [ ] Explain what Django is in your own words
- [ ] Set up a virtual environment
- [ ] Install Django successfully
- [ ] Create a new Django project
- [ ] Run the development server
- [ ] Understand the basic project structure

### Weeks 3-4
- [ ] Create a model with different field types
- [ ] Understand model relationships
- [ ] Create and apply migrations
- [ ] Use the Django admin interface
- [ ] Register models in admin
- [ ] Customize admin display

### Weeks 5-6
- [ ] Create URL patterns
- [ ] Create function-based views
- [ ] Handle GET and POST requests
- [ ] Create templates with inheritance
- [ ] Use template tags and filters
- [ ] Load and use static files

### Weeks 7-8
- [ ] Create Django forms
- [ ] Validate form data
- [ ] Use ModelForms
- [ ] Build a complete CRUD application
- [ ] Integrate models, views, URLs, templates, and forms
- [ ] Understand how all Django pieces work together

## 🚀 Ready to Start?

Begin with [Step 1: Understanding Django](./step-1-understanding-django.md)

Follow the steps in order, and don't skip ahead! Each step builds on what you learned before.

## 📝 Note for Windows Users

All commands in these guides are written for **Windows PowerShell** or **Command Prompt**. If you see a command that doesn't work:

- **PowerShell**: Use `.\` for relative paths
- **CMD**: Use `\` for paths
- **Virtual environment activation**: 
  - PowerShell: `.\myenv\Scripts\Activate.ps1`
  - CMD: `myenv\Scripts\activate`

## 🎓 What's Next?

After completing all 11 steps, you'll be ready for:
- **Practice Projects** - Build 8 real projects to master Django (see [Projects Plan](./PROJECTS-PLAN.md))
- Intermediate level topics (Authentication, APIs, Advanced Forms)
- Building more complex projects
- Advanced Django features
- Deployment
- Django REST Framework

## 🚀 Practice Projects

Ready to build real applications? Check out our **[Projects Plan](./PROJECTS-PLAN.md)**!

**8 Projects to Master Django:**
1. Personal Blog (Basic CRUD)
2. Todo List Application
3. Contact Form Website
4. Book Library Manager
5. Recipe Sharing Platform
6. Student Grade Tracker
7. Event Management System
8. Product Catalog (E-commerce Basics)

Each project includes:
- ✅ Detailed step-by-step guide
- ✅ Complete code examples
- ✅ What you'll learn
- ✅ Challenges to extend functionality

**Start building after completing Steps 1-11!**

**Congratulations!** You've completed the basic level and built a complete Django application! 🎉

Good luck! You've got this! 💪
