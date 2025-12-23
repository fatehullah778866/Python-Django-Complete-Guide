# Step 5: Database Migrations

## 🎯 What You'll Learn

In this step, you'll learn:
- What migrations are (in simple words)
- How to create migrations
- How to apply migrations
- How to read migration files
- How to rollback migrations
- How to create data migrations

---

## 🤔 What are Migrations?

### Simple Explanation

**A migration is like a set of instructions that tells the database how to change its structure.**

**Real-world analogy:**
Think of building a house:
1. **Model** = The blueprint (what you want)
2. **Migration** = The construction instructions (how to build it)
3. **Database** = The actual house (what gets built)

**Another analogy:**
- **Model** = A recipe (what ingredients you need)
- **Migration** = The cooking instructions (how to prepare it)
- **Database** = The finished dish (the actual result)

### Technical Definition

Migrations are Django's way of propagating changes you make to your models (adding a field, deleting a model, etc.) into your database schema.

**Breaking it down:**
- **Propagating** = Spreading/transferring
- **Changes to models** = What you changed in your models.py
- **Database schema** = The structure of your database (tables, columns, etc.)

### Why Do We Need Migrations?

**Problem without migrations:**
- You create a model in Python
- But the database doesn't know about it yet!
- You'd have to manually create tables in the database (hard work!)

**Solution with migrations:**
- Django automatically creates instructions
- You run the migration
- Database is updated automatically!

**Benefits:**
1. **Automatic**: Django does the work for you
2. **Version control**: You can track changes
3. **Team-friendly**: Everyone's database stays in sync
4. **Reversible**: You can undo changes

---

## 📝 Understanding Migrations

### What Happens When You Create a Model?

**Step 1: You write a model**
```python
# blog/models.py
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
```

**Step 2: Django needs to create a migration**
- Django sees your model
- Django creates instructions to make a database table

**Step 3: You apply the migration**
- Django reads the instructions
- Django creates the table in the database

**Step 4: Your database now has a table!**
- Table name: `blog_post`
- Columns: `id`, `title`, `content`

### Migration Files

**Where are they?**
Migrations are stored in: `blog/migrations/` folder

**What do they look like?**
```python
# blog/migrations/0001_initial.py
from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    
    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(...)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
            ],
        ),
    ]
```

**File naming:**
- `0001_initial.py` = First migration, initial setup
- `0002_add_author.py` = Second migration, adds author field
- `0003_remove_old_field.py` = Third migration, removes a field

**The numbers matter!** They show the order of migrations.

---

## 🛠️ Creating Migrations

### Command: `makemigrations`

**What it does:** Creates migration files based on your model changes

**How to use it:**
```powershell
# Make sure you're in your project folder
cd myfirstproject

# Make sure virtual environment is activated
# You should see (myenv) at the start

# Create migrations
python manage.py makemigrations
```

**What happens:**
1. Django looks at your models
2. Django compares them to the database
3. Django creates migration files for any changes
4. Django shows you what it's creating

**Example output:**
```
Migrations for 'blog':
  blog/migrations/0001_initial.py
    - Create model Post
```

**What this means:**
- Created a migration file: `0001_initial.py`
- This migration will create the `Post` model

### Creating Migrations for a Specific App

**If you have multiple apps:**
```powershell
# Create migrations for just the blog app
python manage.py makemigrations blog

# Create migrations for all apps
python manage.py makemigrations
```

### What if Nothing Happens?

**If you see:**
```
No changes detected
```

**This means:**
- Your models match what's already in the database
- No migrations needed!

**Common reasons:**
- You haven't changed any models
- You haven't created any new models
- Migrations are already up to date

---

## ▶️ Applying Migrations

### Command: `migrate`

**What it does:** Applies migrations to the database (actually creates/updates tables)

**Important:** Creating migrations doesn't change the database! You must apply them!

**How to use it:**
```powershell
# Apply all migrations
python manage.py migrate
```

**What happens:**
1. Django looks at all migration files
2. Django checks which ones haven't been applied
3. Django applies them in order
4. Django updates the database

**Example output:**
```
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions, blog
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying sessions.0001_initial... OK
  Applying blog.0001_initial... OK
```

**What this means:**
- Applied migrations for: admin, auth, contenttypes, sessions, blog
- All migrations completed successfully (OK)

### Applying Migrations for a Specific App

```powershell
# Apply migrations for just the blog app
python manage.py migrate blog

# Apply all migrations
python manage.py migrate
```

### Understanding the Output

**`Operations to perform:`**
- Shows what Django is about to do

**`Running migrations:`**
- Shows migrations being applied

**`Applying blog.0001_initial... OK`**
- **`Applying`** = Currently applying this migration
- **`blog.0001_initial`** = Name of the migration
- **`OK`** = Successfully completed

**If there's an error:**
- Django will show an error message
- The migration won't be applied
- You need to fix the problem first

---

## 📖 Reading Migration Files

### Understanding Migration Structure

**Let's look at a real migration file:**

```python
# blog/migrations/0001_initial.py
from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    
    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
```

**Line-by-line explanation:**

**Line 1: `from django.db import migrations, models`**
- Imports migration tools and model tools
- **Simple explanation:** "Get the tools to create migrations"

**Line 3: `class Migration(migrations.Migration):`**
- Defines a migration class
- **Simple explanation:** "This is a migration"

**Line 4: `initial = True`**
- Marks this as the first migration
- **Simple explanation:** "This is the starting point"

**Line 5: `dependencies = []`**
- Lists migrations this depends on
- Empty = no dependencies (first migration)
- **Simple explanation:** "This migration doesn't need anything else first"

**Line 7: `operations = [`**
- List of operations to perform
- **Simple explanation:** "Here's what to do"

**Line 8-14: `migrations.CreateModel(...)`**
- Operation to create a model
- **Simple explanation:** "Create a table for the Post model"

**Inside CreateModel:**
- **`name='Post'`** = Name of the model
- **`fields=[...]`** = List of fields (columns)

**Each field:**
- **`('id', models.AutoField(...))`** = Auto-incrementing ID field
- **`('title', models.CharField(max_length=200))`** = Title field, max 200 chars
- **`('content', models.TextField())`** = Content field, unlimited text
- **`('created_at', models.DateTimeField(auto_now_add=True))`** = Timestamp field

### Common Migration Operations

#### 1. CreateModel
**What it does:** Creates a new table
```python
migrations.CreateModel(
    name='Post',
    fields=[...],
)
```

#### 2. AddField
**What it does:** Adds a new column to a table
```python
migrations.AddField(
    model_name='post',
    name='author',
    field=models.ForeignKey(on_delete=models.CASCADE, to='auth.User'),
)
```

#### 3. RemoveField
**What it does:** Removes a column from a table
```python
migrations.RemoveField(
    model_name='post',
    name='old_field',
)
```

#### 4. AlterField
**What it does:** Changes a field's properties
```python
migrations.AlterField(
    model_name='post',
    name='title',
    field=models.CharField(max_length=300),  # Changed from 200 to 300
)
```

#### 5. RenameField
**What it does:** Renames a column
```python
migrations.RenameField(
    model_name='post',
    old_name='content',
    new_name='body',
)
```

#### 6. DeleteModel
**What it does:** Deletes a table
```python
migrations.DeleteModel(
    name='OldModel',
)
```

---

## 🔄 Example: Adding a Field

### Step 1: Modify Your Model

**Before:**
```python
# blog/models.py
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
```

**After (add author field):**
```python
# blog/models.py
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # ← New field!
```

### Step 2: Create Migration

```powershell
python manage.py makemigrations
```

**Output:**
```
Migrations for 'blog':
  blog/migrations/0002_post_author.py
    - Add field author to post
```

**What happened:**
- Created migration file: `0002_post_author.py`
- This migration will add the `author` field

### Step 3: Look at the Migration File

**File: `blog/migrations/0002_post_author.py`**
```python
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]
    
    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
```

**Line-by-line:**

**Line 5: `dependencies = [`**
- Lists migrations this depends on
- **`('blog', '0001_initial')`** = Must run 0001_initial first
- **Simple explanation:** "Do the first migration before this one"

**Line 12-18: `migrations.AddField(...)`**
- Adds the author field
- **`model_name='post'`** = Add to Post model
- **`name='author'`** = Field name
- **`field=models.ForeignKey(...)`** = Field type and settings

### Step 4: Apply Migration

```powershell
python manage.py migrate
```

**Output:**
```
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions, blog
Running migrations:
  Applying blog.0002_post_author... OK
```

**What happened:**
- Applied the migration
- Database now has the `author` field!

---

## ⏪ Rolling Back Migrations

### What is Rolling Back?

**Simple explanation:**
Rolling back means undoing a migration - going back to how things were before.

**Real-world analogy:**
Like using "Undo" in a word processor - you go back to the previous version.

### How to Rollback

**Step 1: See migration history**
```powershell
python manage.py showmigrations
```

**Output:**
```
blog
 [X] 0001_initial
 [X] 0002_post_author
 [X] 0003_add_category
```

**What this means:**
- `[X]` = Migration has been applied
- `[ ]` = Migration has not been applied

**Step 2: Rollback to a specific migration**
```powershell
# Rollback to migration 0002
python manage.py migrate blog 0002_post_author
```

**What happens:**
- Django undoes migration 0003
- Database goes back to state after 0002

**Step 3: Rollback all migrations for an app**
```powershell
# Rollback all blog migrations
python manage.py migrate blog zero
```

**What happens:**
- Undoes ALL migrations for the blog app
- Removes all blog tables from database

**⚠️ WARNING:** This deletes data! Be careful!

### When to Rollback?

**Good reasons:**
- You made a mistake
- You want to test something
- You're developing and experimenting

**Bad reasons:**
- In production (unless absolutely necessary)
- When others are using the database

---

## 📊 Data Migrations

### What are Data Migrations?

**Simple explanation:**
Data migrations move or change data in your database, not just the structure.

**Regular migration:** Changes the structure (adds fields, creates tables)
**Data migration:** Changes the data (updates values, moves data)

### When to Use Data Migrations?

**Examples:**
- Moving data from one field to another
- Setting default values for existing records
- Converting data format
- Populating new fields with calculated values

### Creating a Data Migration

**Step 1: Create empty migration**
```powershell
python manage.py makemigrations --empty blog
```

**Output:**
```
Migrations for 'blog':
  blog/migrations/0004_auto_20251223_1200.py
    - Empty migration
```

**Step 2: Edit the migration file**

**File: `blog/migrations/0004_auto_20251223_1200.py`**
```python
from django.db import migrations

def set_default_status(apps, schema_editor):
    """Set default status for existing posts."""
    Post = apps.get_model('blog', 'Post')
    Post.objects.filter(status__isnull=True).update(status='draft')

def reverse_set_default_status(apps, schema_editor):
    """Reverse: set status back to None."""
    Post = apps.get_model('blog', 'Post')
    Post.objects.filter(status='draft').update(status=None)

class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0003_previous_migration'),
    ]
    
    operations = [
        migrations.RunPython(set_default_status, reverse_set_default_status),
    ]
```

**Line-by-line explanation:**

**Line 3: `def set_default_status(apps, schema_editor):`**
- Defines a function that runs during migration
- **`apps`** = Access to models
- **`schema_editor`** = Database editor (not used here)
- **Simple explanation:** "Function that sets default status"

**Line 5: `Post = apps.get_model('blog', 'Post')`**
- Gets the Post model
- **`apps.get_model`** = Get a model (use this, not direct import!)
- **Simple explanation:** "Get the Post model"

**Line 6: `Post.objects.filter(status__isnull=True).update(status='draft')`**
- Finds posts with no status
- Sets their status to 'draft'
- **Simple explanation:** "Set status to 'draft' for posts without status"

**Line 8: `def reverse_set_default_status(...):`**
- Reverse function (for rollback)
- **Simple explanation:** "Undo what we did"

**Line 17: `migrations.RunPython(...)`**
- Runs Python code during migration
- **Simple explanation:** "Run this Python code"

### Why Use `apps.get_model`?

**❌ Wrong way:**
```python
from blog.models import Post  # Don't do this in migrations!
```

**✅ Right way:**
```python
Post = apps.get_model('blog', 'Post')  # Do this!
```

**Why?**
- Models might change in the future
- `apps.get_model` gets the model as it was at migration time
- Direct import gets the current model (might be different!)

---

## 🔍 Useful Migration Commands

### Show Migration Status

```powershell
python manage.py showmigrations
```

**Shows:** Which migrations are applied, which are not

### Show SQL for a Migration

```powershell
python manage.py sqlmigrate blog 0001
```

**Shows:** The SQL code that will be executed

**Example output:**
```sql
CREATE TABLE "blog_post" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "title" varchar(200) NOT NULL,
    "content" text NOT NULL,
    "created_at" datetime NOT NULL
);
```

### Fake a Migration

```powershell
python manage.py migrate --fake blog 0001
```

**What it does:** Marks migration as applied without actually running it

**When to use:** When you've manually changed the database

**⚠️ Advanced!** Only use if you know what you're doing!

---

## ✅ Checklist: Migrations Complete

Before moving to Step 6, make sure you can:

- [ ] Explain what migrations are
- [ ] Create migrations: `python manage.py makemigrations`
- [ ] Apply migrations: `python manage.py migrate`
- [ ] Read and understand a migration file
- [ ] Rollback a migration
- [ ] Understand the difference between structure and data migrations

---

## 🐛 Common Problems and Solutions

### Problem: "No changes detected"

**Solution:**
- Make sure you saved your models.py file
- Make sure the app is in INSTALLED_APPS
- Check for syntax errors in models.py

### Problem: "Migration conflicts"

**Solution:**
- Two migrations have the same number
- Merge the migrations or rename one

### Problem: "Table already exists"

**Solution:**
- Migration was partially applied
- Try: `python manage.py migrate --fake-initial`

### Problem: "Field doesn't exist"

**Solution:**
- You're trying to use a field that hasn't been migrated yet
- Run: `python manage.py migrate`

---

## 🚀 Ready for Step 6?

Excellent! You now understand how migrations work!

Next, you'll learn about the Django Admin Interface - a powerful tool for managing your data. Go to [Step 6: Django Admin Interface](./step-6-django-admin.md)

---

## 💡 Pro Tips

1. **Always create migrations after changing models**
2. **Always apply migrations after creating them**
3. **Commit migrations to version control** (Git)
4. **Test migrations on a copy of your database first**
5. **Never edit applied migrations** - create new ones instead
6. **Use `showmigrations`** to check status
7. **Keep migrations small** - easier to debug

---

## 📝 Quick Reference

```powershell
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Show migration status
python manage.py showmigrations

# Show SQL for migration
python manage.py sqlmigrate app_name migration_number

# Rollback to specific migration
python manage.py migrate app_name migration_name

# Create empty migration
python manage.py makemigrations --empty app_name
```

