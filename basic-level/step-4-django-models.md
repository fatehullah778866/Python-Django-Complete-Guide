# Step 4: Django Models

## 🎯 What You'll Learn

In this step, you'll learn:
- What Django ORM is (in simple words)
- How to create your first model
- Different types of model fields
- How models relate to each other
- Model methods and special features

---

## 🤔 What is a Model?

### Simple Explanation

**A model is like a blueprint for storing information in a database.**

**Real-world analogy:**
Think of a model like a form you fill out:
- **Form for a library book**: Title, Author, ISBN, Pages
- **Form for a person**: Name, Age, Email, Phone

A Django model is like that form - it defines what information you want to store.

**Technical definition:**
A model is a Python class that represents a database table. Each attribute of the class represents a database field.

### What is a Database?

**Simple explanation:**
A database is like a digital filing cabinet where you store information.

**Examples:**
- A phone's contact list (stores names and phone numbers)
- A library's catalog (stores book information)
- A school's student records (stores student information)

**In Django:**
- Models define what information you want to store
- The database actually stores that information
- Django helps you save, find, and update that information

---

## 🧠 Understanding Django ORM

### What is ORM?

**ORM** stands for **Object-Relational Mapping**.

**Simple explanation:**
ORM is like a translator between Python code and the database.

**Without ORM (hard way):**
```sql
SELECT * FROM books WHERE author = 'John Doe';
```
You have to write SQL (database language) yourself.

**With Django ORM (easy way):**
```python
Book.objects.filter(author='John Doe')
```
You write Python code, and Django translates it to SQL automatically!

**Analogy:**
- **SQL** = Speaking in database language
- **Python/Django ORM** = Speaking in Python
- **ORM** = The translator that converts Python to database language

### Why Use ORM?

1. **Easier to write**: Python is easier than SQL
2. **Safer**: Django protects against common mistakes
3. **Works with different databases**: Same code works with SQLite, PostgreSQL, MySQL
4. **Less code**: Write less, do more

---

## 🏗️ Creating Your First Model

### Step 1: Create an App

Before creating models, you need an app!

**What is an app?**
An app is a part of your website that does one thing (like a blog, or a shop).

**Create an app:**
```powershell
# Make sure you're in your project folder
cd myfirstproject

# Make sure virtual environment is activated
# You should see (myenv) at the start of your command line

# Create an app called "blog"
python manage.py startapp blog
```

**What this command does:**
- `python manage.py` = Use Django's control file
- `startapp` = Create a new app
- `blog` = Name of the app (you can name it anything)

**What gets created:**
```
blog/
├── __init__.py
├── admin.py
├── apps.py
├── models.py      ← This is where we'll create models!
├── tests.py
└── views.py
```

### Step 2: Register the App

Tell Django about your new app!

**Open:** `myfirstproject/settings.py`

**Find this section:**
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

**Add your app:**
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',  # ← Add this line!
]
```

**Why?**
Django needs to know about your app so it can use it!

### Step 3: Create Your First Model

**Open:** `blog/models.py`

**What's currently there:**
```python
from django.db import models

# Create your models here.
```

**Let's create a simple model - a Blog Post:**

```python
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
```

**Let's break this down line by line:**

**Line 1: `from django.db import models`**
- **What it does:** Imports Django's model tools
- **Simple explanation:** "Get the tools to create models"
- **Think of it as:** Getting a toolbox with model-building tools

**Line 3: `class Post(models.Model):`**
- **`class`** = Defines a new class (a blueprint)
- **`Post`** = Name of the model (like "Blog Post")
- **`models.Model`** = Tells Django "this is a model"
- **Simple explanation:** "Create a blueprint called Post for storing blog posts"
- **The colon `:`** = Starts the class definition

**Line 4: `title = models.CharField(max_length=200)`**
- **`title`** = Name of the field (like "title" in a form)
- **`models.CharField`** = Type of field (text, limited length)
- **`max_length=200`** = Maximum 200 characters
- **Simple explanation:** "Store a title, up to 200 characters long"
- **Real-world example:** Like a "Subject" field in an email

**Line 5: `content = models.TextField()`**
- **`content`** = Name of the field
- **`models.TextField()`** = Type of field (text, unlimited length)
- **Simple explanation:** "Store the blog post content, can be very long"
- **Real-world example:** Like the "Message" field in an email (can be long)

**Line 6: `created_at = models.DateTimeField(auto_now_add=True)`**
- **`created_at`** = Name of the field
- **`models.DateTimeField`** = Type of field (date and time)
- **`auto_now_add=True`** = Automatically set when created
- **Simple explanation:** "Store when this post was created, set automatically"
- **Real-world example:** Like a timestamp that says "Created: December 23, 2025"

**Line 8: `def __str__(self):`**
- **`def`** = Define a function
- **`__str__`** = Special function name (tells Python how to display this)
- **`self`** = Refers to this specific post
- **Simple explanation:** "Define how to display this post as text"

**Line 9: `return self.title`**
- **`return`** = Give back this value
- **`self.title`** = The title of this post
- **Simple explanation:** "When showing this post, show its title"
- **Why?** So when Django shows a post, it shows the title instead of "Post object"

**Complete example:**
```python
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
```

---

## 📋 Model Fields and Field Types

### What is a Field?

**Simple explanation:**
A field is like a box where you store one piece of information.

**Example:**
- **Name field** = Stores the name
- **Email field** = Stores the email
- **Age field** = Stores the age

### Common Field Types

#### 1. CharField - Short Text

**What it is:** Stores short text (like a name or title)

**Example:**
```python
name = models.CharField(max_length=100)
```

**Parameters:**
- **`max_length`** = Maximum characters (required!)

**Real-world use:**
- Names, titles, short descriptions

#### 2. TextField - Long Text

**What it is:** Stores long text (like an article or description)

**Example:**
```python
description = models.TextField()
```

**Real-world use:**
- Blog post content, long descriptions, comments

#### 3. IntegerField - Whole Numbers

**What it is:** Stores whole numbers (1, 2, 3, 100, etc.)

**Example:**
```python
age = models.IntegerField()
price = models.IntegerField()
```

**Real-world use:**
- Age, price (in cents), quantity, rating

#### 4. DecimalField - Decimal Numbers

**What it is:** Stores decimal numbers (1.99, 3.14, etc.)

**Example:**
```python
price = models.DecimalField(max_digits=10, decimal_places=2)
```

**Parameters:**
- **`max_digits`** = Total number of digits
- **`decimal_places`** = Number of decimal places

**Real-world use:**
- Prices, measurements, percentages

#### 5. BooleanField - True/False

**What it is:** Stores True or False (yes or no)

**Example:**
```python
is_published = models.BooleanField(default=False)
```

**Parameters:**
- **`default`** = Default value if not specified

**Real-world use:**
- Published/not published, active/inactive, yes/no questions

#### 6. DateField - Date Only

**What it is:** Stores a date (year, month, day)

**Example:**
```python
birth_date = models.DateField()
```

**Real-world use:**
- Birth dates, event dates, deadlines

#### 7. DateTimeField - Date and Time

**What it is:** Stores date and time

**Example:**
```python
created_at = models.DateTimeField(auto_now_add=True)
updated_at = models.DateTimeField(auto_now=True)
```

**Special parameters:**
- **`auto_now_add=True`** = Set automatically when created
- **`auto_now=True`** = Update automatically when saved

**Real-world use:**
- Timestamps, creation dates, update dates

#### 8. EmailField - Email Address

**What it is:** Stores email addresses (validates format)

**Example:**
```python
email = models.EmailField()
```

**Real-world use:**
- User emails, contact emails

#### 9. URLField - Website URL

**What it is:** Stores website URLs (validates format)

**Example:**
```python
website = models.URLField()
```

**Real-world use:**
- Website links, social media profiles

#### 10. ImageField - Images

**What it is:** Stores image files

**Example:**
```python
photo = models.ImageField(upload_to='photos/')
```

**Parameters:**
- **`upload_to`** = Folder where images are saved

**Note:** Requires `Pillow` library: `pip install Pillow`

**Real-world use:**
- User photos, product images, blog post images

#### 11. FileField - Files

**What it is:** Stores any type of file

**Example:**
```python
document = models.FileField(upload_to='documents/')
```

**Real-world use:**
- PDFs, documents, downloads

### Field Options (Parameters)

Many fields can use these options:

#### `null=True`
**What it does:** Allows empty values in database
```python
middle_name = models.CharField(max_length=100, null=True)
```

#### `blank=True`
**What it does:** Allows empty values in forms
```python
bio = models.TextField(blank=True)
```

#### `default=value`
**What it does:** Sets a default value
```python
status = models.CharField(max_length=20, default='draft')
```

#### `choices=LIST`
**What it does:** Limits values to a list
```python
STATUS_CHOICES = [
    ('draft', 'Draft'),
    ('published', 'Published'),
]
status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
```

---

## 🔗 Model Relationships

### What are Relationships?

**Simple explanation:**
Relationships connect models together, like connecting puzzle pieces.

**Example:**
- A **Blog Post** has an **Author** (one author, many posts)
- A **Student** has many **Classes** (many-to-many)
- A **Person** has one **Profile** (one-to-one)

### Three Types of Relationships

#### 1. ForeignKey - Many-to-One

**What it is:** Many things belong to one thing

**Example:**
Many blog posts belong to one author.

**Code:**
```python
class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
```

**Line-by-line explanation:**

**In the Post model:**
```python
author = models.ForeignKey(Author, on_delete=models.CASCADE)
```

- **`author`** = Name of the field
- **`models.ForeignKey`** = Type of relationship (many-to-one)
- **`Author`** = The model this connects to
- **`on_delete=models.CASCADE`** = What to do if author is deleted
  - **CASCADE** = Delete all posts if author is deleted
  - **PROTECT** = Don't allow deleting author if they have posts
  - **SET_NULL** = Set author to NULL if author is deleted

**Simple explanation:**
"Each post has one author. If the author is deleted, delete all their posts too."

**Real-world analogy:**
- Many students → One classroom
- Many comments → One blog post
- Many orders → One customer

#### 2. ManyToManyField - Many-to-Many

**What it is:** Many things connect to many things

**Example:**
A student can have many classes, and a class can have many students.

**Code:**
```python
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    
    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField(Student)
    
    def __str__(self):
        return self.name
```

**Line-by-line:**

```python
students = models.ManyToManyField(Student)
```

- **`students`** = Name of the field
- **`models.ManyToManyField`** = Type of relationship (many-to-many)
- **`Student`** = The model this connects to

**Simple explanation:**
"A course can have many students, and a student can be in many courses."

**Real-world examples:**
- Books and Authors (a book can have many authors, an author can write many books)
- Posts and Tags (a post can have many tags, a tag can be on many posts)

#### 3. OneToOneField - One-to-One

**What it is:** One thing connects to exactly one thing

**Example:**
A User has one Profile, and a Profile belongs to one User.

**Code:**
```python
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"
```

**Line-by-line:**

```python
user = models.OneToOneField(User, on_delete=models.CASCADE)
```

- **`user`** = Name of the field
- **`models.OneToOneField`** = Type of relationship (one-to-one)
- **`User`** = Django's built-in User model
- **`on_delete=models.CASCADE`** = Delete profile if user is deleted

**Simple explanation:**
"Each user has exactly one profile, and each profile belongs to exactly one user."

**Real-world examples:**
- User and Profile
- Person and ID Card
- Product and Product Details

---

## 🎨 Model Methods and Properties

### What are Methods?

**Simple explanation:**
Methods are functions that belong to a model. They can do things with the model's data.

### The `__str__` Method

**What it does:** Tells Python how to display the model as text

**Example:**
```python
class Post(models.Model):
    title = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title
```

**Without `__str__`:**
- Django shows: `Post object (1)`

**With `__str__`:**
- Django shows: `My First Blog Post`

**Why it's important:**
Makes things easier to read in the admin panel and when debugging!

### Custom Methods

You can create your own methods to do things with your model.

**Example:**
```python
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def get_excerpt(self, length=50):
        """Return a short excerpt of the content."""
        if len(self.content) <= length:
            return self.content
        return self.content[:length] + "..."
    
    def is_recent(self):
        """Check if post was created in the last 7 days."""
        from django.utils import timezone
        from datetime import timedelta
        return self.created_at >= timezone.now() - timedelta(days=7)
```

**Line-by-line explanation:**

**Method 1: `get_excerpt`**
```python
def get_excerpt(self, length=50):
```
- **`def`** = Define a function
- **`get_excerpt`** = Name of the method
- **`self`** = Refers to this specific post
- **`length=50`** = Parameter with default value 50

```python
if len(self.content) <= length:
    return self.content
```
- **`if`** = Check a condition
- **`len(self.content)`** = Length of the content
- **`<= length`** = Is it shorter than or equal to the length?
- **`return self.content`** = If yes, return the full content

```python
return self.content[:length] + "..."
```
- **`self.content[:length]`** = First 50 characters
- **`+ "..."`** = Add three dots at the end
- **`return`** = Give back this value

**How to use it:**
```python
post = Post.objects.get(id=1)
print(post.get_excerpt())  # Shows first 50 characters
print(post.get_excerpt(100))  # Shows first 100 characters
```

**Method 2: `is_recent`**
```python
def is_recent(self):
```
- Checks if the post is less than 7 days old

```python
from django.utils import timezone
from datetime import timedelta
```
- Import tools for working with dates

```python
return self.created_at >= timezone.now() - timedelta(days=7)
```
- **`timezone.now()`** = Current date and time
- **`timedelta(days=7)`** = 7 days
- **`timezone.now() - timedelta(days=7)`** = 7 days ago
- **`>=`** = Is created_at greater than or equal to 7 days ago?

**How to use it:**
```python
post = Post.objects.get(id=1)
if post.is_recent():
    print("This is a recent post!")
```

---

## 📝 Meta Options

### What is Meta?

**Simple explanation:**
Meta is like a settings panel for your model. It controls how the model behaves.

**Example:**
```python
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'
    
    def __str__(self):
        return self.title
```

**Line-by-line:**

**`class Meta:`**
- Starts the Meta class (settings for this model)

**`ordering = ['-created_at']`**
- **`ordering`** = How to sort posts
- **`['-created_at']`** = Sort by created_at, newest first (minus means reverse)
- **Simple explanation:** "Show newest posts first"

**`verbose_name = 'Blog Post'`**
- **`verbose_name`** = Human-readable name (singular)
- **Simple explanation:** "Call this 'Blog Post' instead of 'Post'"

**`verbose_name_plural = 'Blog Posts'`**
- **`verbose_name_plural`** = Human-readable name (plural)
- **Simple explanation:** "Call multiple posts 'Blog Posts'"

### Common Meta Options

#### `ordering`
```python
ordering = ['-created_at']  # Newest first
ordering = ['title']  # Alphabetical by title
ordering = ['-created_at', 'title']  # Newest first, then alphabetical
```

#### `verbose_name` and `verbose_name_plural`
```python
verbose_name = 'Blog Post'
verbose_name_plural = 'Blog Posts'
```

#### `db_table`
```python
db_table = 'blog_posts'  # Custom table name
```

#### `get_latest_by`
```python
get_latest_by = 'created_at'  # Which field to use for "latest"
```

---

## ✅ Complete Example Model

Here's a complete example with everything we learned:

```python
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    
    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']
    
    def __str__(self):
        return self.name

class Post(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_featured = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'
    
    def __str__(self):
        return self.title
    
    def get_excerpt(self, length=100):
        """Return a short excerpt."""
        if len(self.content) <= length:
            return self.content
        return self.content[:length] + "..."
    
    def is_recent(self):
        """Check if post is less than 7 days old."""
        from django.utils import timezone
        from datetime import timedelta
        return self.created_at >= timezone.now() - timedelta(days=7)

class Tag(models.Model):
    name = models.CharField(max_length=50)
    posts = models.ManyToManyField(Post)
    
    def __str__(self):
        return self.name
```

---

## ✅ Checklist: Models Complete

Before moving to Step 5, make sure you can:

- [ ] Explain what a model is in your own words
- [ ] Explain what ORM is
- [ ] Create a model with different field types
- [ ] Understand ForeignKey, ManyToManyField, and OneToOneField
- [ ] Create a `__str__` method
- [ ] Use Meta options
- [ ] Create custom methods

---

## 🚀 Ready for Step 5?

Great job! You now understand Django models!

Next, you'll learn about migrations - how to save your models to the database. Go to [Step 5: Database Migrations](./step-5-database-migrations.md)

---

## 💡 Pro Tips

1. **Always add `__str__` method** - Makes debugging easier
2. **Use meaningful field names** - `created_at` is better than `date1`
3. **Think about relationships** - How do your models connect?
4. **Use choices for limited options** - Better than free text
5. **Add help_text** - Document your fields: `help_text='Enter the post title'`

