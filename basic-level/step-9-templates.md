# Step 9: Templates

## 🎯 What You'll Learn

In this step, you'll learn:
- What templates are (in simple words)
- Django Template Language (DTL)
- Template inheritance
- Template tags and filters
- Static files (CSS, JS, images)
- Template context

---

## 🤔 What are Templates?

### Simple Explanation

**Templates are HTML files with special Django code that can display dynamic data.**

**Real-world analogy:**
Think of a template like a form letter:
- **Template** = The form letter with blanks
- **Data** = Information to fill in the blanks
- **Result** = Complete letter with personalized information

**Another analogy:**
- **Template** = A cookie cutter (the shape)
- **Data** = The dough (the content)
- **Result** = The cookie (the final page)

### Technical Definition

Templates are text files that define the structure or layout of a file (like an HTML page), with placeholders for actual content. Django fills in these placeholders with actual data when rendering the template.

**Breaking it down:**
- **Template** = HTML file with special syntax
- **Dynamic data** = Data from your views
- **Rendering** = Django fills in the data and creates HTML

### Why Use Templates?

1. **Separation of concerns**: HTML separate from Python code
2. **Reusability**: Use same template with different data
3. **Maintainability**: Easier to update design
4. **Security**: Django automatically escapes data
5. **Powerful**: Lots of built-in features

---

## 📁 Setting Up Templates

### Where to Put Templates

**Django looks for templates in:**
1. Each app's `templates/` folder
2. Global `templates/` folder (in project root)

**Recommended structure:**
```
myfirstproject/
├── templates/          ← Global templates (optional)
│   └── base.html
└── blog/
    └── templates/     ← App-specific templates
        └── blog/
            ├── list.html
            └── detail.html
```

**Why `blog/blog/`?**
- First `blog/` = App folder
- `templates/blog/` = Namespace (prevents conflicts)
- `list.html` = The actual template

### Configuring Templates

**File:** `myfirstproject/settings.py`

**Find TEMPLATES setting:**
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # ← Global templates folder
        'APP_DIRS': True,  # ← Look in app templates folders
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

**Line-by-line:**

**Line 4: `'DIRS': [BASE_DIR / 'templates']`**
- Where to look for global templates
- **Simple explanation:** "Also look in the templates folder at project root"

**Line 5: `'APP_DIRS': True`**
- Look in each app's templates folder
- **Simple explanation:** "Look in each app's templates folder too"

**Line 7-12: `'context_processors'`**
- Functions that add data to all templates
- **Simple explanation:** "Add this data to every template automatically"

---

## 🎨 Django Template Language (DTL)

### What is DTL?

**Django Template Language** is Django's way of adding dynamic content to HTML.

**DTL uses:**
- **Variables**: `{{ variable }}`
- **Tags**: `{% tag %}`
- **Filters**: `{{ variable|filter }}`
- **Comments**: `{# comment #}`

### Variables

**Syntax:** `{{ variable_name }}`

**What it does:** Displays the value of a variable

**Example:**
```html
<h1>Hello, {{ name }}!</h1>
```

**If `name = "John"`:**
```html
<h1>Hello, John!</h1>
```

**Accessing object attributes:**
```html
<p>Title: {{ post.title }}</p>
<p>Author: {{ post.author.username }}</p>
```

**Accessing dictionary keys:**
```html
<p>Name: {{ user.name }}</p>
<p>Email: {{ user.email }}</p>
```

**Accessing list items:**
```html
<p>First item: {{ items.0 }}</p>
<p>Second item: {{ items.1 }}</p>
```

### Template Tags

**Syntax:** `{% tag_name %}`

**What they do:** Perform logic, loops, conditionals, etc.

#### 1. {% if %} - Conditionals

**What it does:** Shows content conditionally

**Example:**
```html
{% if user.is_authenticated %}
    <p>Welcome, {{ user.username }}!</p>
{% else %}
    <p>Please log in.</p>
{% endif %}
```

**Line-by-line:**

**Line 1: `{% if user.is_authenticated %}`**
- Checks if user is logged in
- **Simple explanation:** "If the user is logged in..."

**Line 2: `<p>Welcome, {{ user.username }}!</p>`**
- Shows if condition is true
- **Simple explanation:** "Show this message"

**Line 3: `{% else %}`**
- What to show if condition is false
- **Simple explanation:** "Otherwise..."

**Line 4: `<p>Please log in.</p>`**
- Shows if condition is false
- **Simple explanation:** "Show this instead"

**Line 5: `{% endif %}`**
- Ends the if block
- **Simple explanation:** "End of the if statement"

**More examples:**
```html
{% if age >= 18 %}
    <p>You are an adult.</p>
{% elif age >= 13 %}
    <p>You are a teenager.</p>
{% else %}
    <p>You are a child.</p>
{% endif %}
```

#### 2. {% for %} - Loops

**What it does:** Repeats content for each item in a list

**Example:**
```html
<ul>
{% for post in posts %}
    <li>{{ post.title }}</li>
{% endfor %}
</ul>
```

**Line-by-line:**

**Line 2: `{% for post in posts %}`**
- Loops through posts list
- **Simple explanation:** "For each post in the posts list..."

**Line 3: `<li>{{ post.title }}</li>`**
- Shows post title
- **Simple explanation:** "Show the post title"

**Line 4: `{% endfor %}`**
- Ends the loop
- **Simple explanation:** "End of the loop"

**With empty:**
```html
{% for post in posts %}
    <li>{{ post.title }}</li>
{% empty %}
    <li>No posts yet.</li>
{% endfor %}
```

**Loop variables:**
```html
{% for post in posts %}
    <p>Post {{ forloop.counter }}: {{ post.title }}</p>
    {% if forloop.first %}
        <p>This is the first post!</p>
    {% endif %}
    {% if forloop.last %}
        <p>This is the last post!</p>
    {% endif %}
{% endfor %}
```

**Available variables:**
- `forloop.counter` = Current iteration (1, 2, 3...)
- `forloop.counter0` = Current iteration (0, 1, 2...)
- `forloop.first` = True if first item
- `forloop.last` = True if last item
- `forloop.revcounter` = Reverse counter

#### 3. {% url %} - URL Tag

**What it does:** Gets URL from URL name

**Example:**
```html
<a href="{% url 'blog_list' %}">All Posts</a>
<a href="{% url 'blog_detail' post_id=5 %}">Post 5</a>
```

**Line-by-line:**

**Line 1: `{% url 'blog_list' %}`**
- Gets URL for 'blog_list'
- **Simple explanation:** "What is the URL named 'blog_list'?"

**Line 2: `{% url 'blog_detail' post_id=5 %}`**
- Gets URL with parameter
- **Simple explanation:** "What is the URL for post 5?"

**Result:**
```html
<a href="/blog/">All Posts</a>
<a href="/blog/5/">Post 5</a>
```

#### 4. {% csrf_token %} - CSRF Protection

**What it does:** Adds CSRF token to forms (required for POST!)

**Example:**
```html
<form method="post">
    {% csrf_token %}
    <input type="text" name="name">
    <button type="submit">Submit</button>
</form>
```

**⚠️ Important:** Always include this in forms that use POST!

#### 5. {% block %} and {% extends %} - Template Inheritance

**We'll cover this in detail next!**

### Filters

**Syntax:** `{{ variable|filter }}`

**What they do:** Modify the display of variables

#### Common Filters

**1. |upper - Uppercase**
```html
{{ name|upper }}
```
- "john" → "JOHN"

**2. |lower - Lowercase**
```html
{{ name|lower }}
```
- "JOHN" → "john"

**3. |title - Title Case**
```html
{{ name|title }}
```
- "john doe" → "John Doe"

**4. |length - Length**
```html
{{ items|length }}
```
- Shows number of items

**5. |default - Default Value**
```html
{{ name|default:"Guest" }}
```
- If name is empty, shows "Guest"

**6. |date - Format Date**
```html
{{ post.created_at|date:"F d, Y" }}
```
- Formats date: "December 23, 2025"

**7. |truncatewords - Truncate Text**
```html
{{ content|truncatewords:20 }}
```
- Shows first 20 words, adds "..."

**8. |safe - Mark as Safe**
```html
{{ html_content|safe }}
```
- Renders HTML instead of showing it as text
- **⚠️ Only use with trusted content!**

**9. |slice - Slice List**
```html
{{ items|slice:":5" }}
```
- Shows first 5 items

**10. |join - Join List**
```html
{{ tags|join:", " }}
```
- Joins list with comma and space

**Chaining filters:**
```html
{{ name|upper|truncatewords:5 }}
```
- Applies multiple filters in order

---

## 🏗️ Template Inheritance

### What is Template Inheritance?

**Simple explanation:**
Template inheritance lets you create a base template and extend it, like building on a foundation.

**Real-world analogy:**
- **Base template** = A house blueprint
- **Child template** = A specific room (uses the blueprint but adds its own details)

### How It Works

**Step 1: Create Base Template**

**File:** `templates/base.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}My Blog{% endblock %}</title>
</head>
<body>
    <header>
        <h1>My Blog</h1>
        <nav>
            <a href="{% url 'home' %}">Home</a>
            <a href="{% url 'blog_list' %}">Blog</a>
        </nav>
    </header>
    
    <main>
        {% block content %}
        {% endblock %}
    </main>
    
    <footer>
        <p>&copy; 2025 My Blog</p>
    </footer>
</body>
</html>
```

**Line-by-line:**

**Line 5: `{% block title %}My Blog{% endblock %}`**
- Defines a block called "title"
- **`My Blog`** = Default value
- **Simple explanation:** "This is where the page title goes, default is 'My Blog'"

**Line 14: `{% block content %}`**
- Defines a block called "content"
- **Simple explanation:** "This is where page content goes"

**Line 15: `{% endblock %}`**
- Ends the block
- **Simple explanation:** "End of the content area"

**Step 2: Extend Base Template**

**File:** `blog/templates/blog/list.html`
```html
{% extends 'base.html' %}

{% block title %}Blog Posts - My Blog{% endblock %}

{% block content %}
    <h2>All Blog Posts</h2>
    <ul>
    {% for post in posts %}
        <li>
            <a href="{% url 'blog_detail' post_id=post.id %}">
                {{ post.title }}
            </a>
        </li>
    {% endfor %}
    </ul>
{% endblock %}
```

**Line-by-line:**

**Line 1: `{% extends 'base.html' %}`**
- Extends the base template
- **Simple explanation:** "Use base.html as the foundation"

**Line 3: `{% block title %}Blog Posts - My Blog{% endblock %}`**
- Overrides the title block
- **Simple explanation:** "Change the title to this"

**Line 5: `{% block content %}`**
- Fills in the content block
- **Simple explanation:** "Put this content in the main area"

**Result:**
- Uses base.html structure
- Header and footer from base
- Content from list.html
- Title is "Blog Posts - My Blog"

### Block Inheritance

**You can also use `{{ block.super }}` to keep parent content:**

```html
{% block title %}
    Blog Posts - {{ block.super }}
{% endblock %}
```

**Result:** "Blog Posts - My Blog" (adds to parent instead of replacing)

---

## 📦 Static Files

### What are Static Files?

**Simple explanation:**
Static files are files that don't change (CSS, JavaScript, images).

**Types:**
- **CSS** = Stylesheets (make things look pretty)
- **JavaScript** = Interactive features
- **Images** = Photos, icons, logos
- **Fonts** = Custom fonts

### Setting Up Static Files

**Step 1: Create Static Folder**

**Structure:**
```
blog/
└── static/
    └── blog/
        ├── css/
        │   └── style.css
        ├── js/
        │   └── script.js
        └── images/
            └── logo.png
```

**Step 2: Configure Settings**

**File:** `myfirstproject/settings.py`

**Should already have:**
```python
STATIC_URL = 'static/'
```

**For production, add:**
```python
STATIC_ROOT = BASE_DIR / 'staticfiles'
```

**Step 3: Use Static Files in Templates**

**Load static files:**
```html
{% load static %}
```

**Use in template:**
```html
{% load static %}
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="{% static 'blog/css/style.css' %}">
</head>
<body>
    <img src="{% static 'blog/images/logo.png' %}" alt="Logo">
    <script src="{% static 'blog/js/script.js' %}"></script>
</body>
</html>
```

**Line-by-line:**

**Line 1: `{% load static %}`**
- Loads static files tag
- **Simple explanation:** "Enable static file tags"

**Line 5: `{% static 'blog/css/style.css' %}`**
- Gets the static file URL
- **Simple explanation:** "Get the URL for this CSS file"

**Result:**
```html
<link rel="stylesheet" href="/static/blog/css/style.css">
```

### Collecting Static Files (Production)

**For production, collect all static files:**

```powershell
python manage.py collectstatic
```

**What it does:**
- Copies all static files to STATIC_ROOT
- Needed for production servers

---

## 📊 Template Context

### What is Context?

**Simple explanation:**
Context is the data you pass from your view to your template.

**Example:**
```python
def blog_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
        'title': 'All Posts'
    }
    return render(request, 'blog/list.html', context)
```

**In template:**
```html
<h1>{{ title }}</h1>
{% for post in posts %}
    <p>{{ post.title }}</p>
{% endfor %}
```

### Context Processors

**Context processors** add data to ALL templates automatically.

**Built-in context processors:**
- `request` = The request object
- `user` = Current user
- `messages` = Flash messages

**You can access them in any template:**
```html
{% if user.is_authenticated %}
    <p>Hello, {{ user.username }}!</p>
{% endif %}
```

---

## ✅ Complete Template Examples

### Example 1: Blog List Template

**File:** `blog/templates/blog/list.html`
```html
{% extends 'base.html' %}
{% load static %}

{% block title %}Blog Posts{% endblock %}

{% block content %}
    <h1>All Blog Posts</h1>
    
    {% if posts %}
        <ul>
        {% for post in posts %}
            <li>
                <h2><a href="{% url 'blog_detail' post_id=post.id %}">
                    {{ post.title }}
                </a></h2>
                <p>By {{ post.author.username }} on {{ post.created_at|date:"F d, Y" }}</p>
                <p>{{ post.content|truncatewords:30 }}</p>
            </li>
        {% endfor %}
        </ul>
    {% else %}
        <p>No posts yet.</p>
    {% endif %}
{% endblock %}
```

### Example 2: Blog Detail Template

**File:** `blog/templates/blog/detail.html`
```html
{% extends 'base.html' %}

{% block title %}{{ post.title }}{% endblock %}

{% block content %}
    <article>
        <h1>{{ post.title }}</h1>
        <p class="meta">
            By {{ post.author.username }} 
            on {{ post.created_at|date:"F d, Y" }}
        </p>
        <div class="content">
            {{ post.content|linebreaks }}
        </div>
    </article>
    
    <nav>
        <a href="{% url 'blog_list' %}">← Back to all posts</a>
    </nav>
{% endblock %}
```

### Example 3: Base Template with Navigation

**File:** `templates/base.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}My Blog{% endblock %}</title>
    {% load static %}
    <link rel="stylesheet" href="{% static 'blog/css/style.css' %}">
</head>
<body>
    <header>
        <nav>
            <a href="{% url 'home' %}">Home</a>
            <a href="{% url 'blog_list' %}">Blog</a>
            {% if user.is_authenticated %}
                <a href="{% url 'profile' %}">Profile</a>
                <a href="{% url 'logout' %}">Logout</a>
            {% else %}
                <a href="{% url 'login' %}">Login</a>
            {% endif %}
        </nav>
    </header>
    
    <main>
        {% if messages %}
            <ul class="messages">
            {% for message in messages %}
                <li class="{{ message.tags }}">{{ message }}</li>
            {% endfor %}
            </ul>
        {% endif %}
        
        {% block content %}
        {% endblock %}
    </main>
    
    <footer>
        <p>&copy; 2025 My Blog</p>
    </footer>
    
    <script src="{% static 'blog/js/script.js' %}"></script>
</body>
</html>
```

---

## ✅ Checklist: Templates Complete

Before moving to the next level, make sure you can:

- [ ] Explain what templates are
- [ ] Use variables: `{{ variable }}`
- [ ] Use tags: `{% tag %}`
- [ ] Use filters: `{{ variable|filter }}`
- [ ] Create template inheritance with {% extends %}
- [ ] Use {% block %} to define sections
- [ ] Load and use static files
- [ ] Pass context from views to templates
- [ ] Use {% if %}, {% for %}, {% url %}

---

## 🐛 Common Problems

### Problem: "TemplateDoesNotExist"

**Solution:**
- Check template path is correct
- Check TEMPLATES setting in settings.py
- Make sure template file exists
- Check app is in INSTALLED_APPS

### Problem: "Static files not loading"

**Solution:**
- Make sure {% load static %} is at the top
- Check STATIC_URL in settings.py
- Check file path is correct
- Run `python manage.py collectstatic` (production)

### Problem: "Variable not showing"

**Solution:**
- Check variable name matches context
- Check variable is passed in context
- Check for typos
- Use {% if variable %} to check if it exists

---

## 🚀 What's Next?

Congratulations! You've completed the basic level! 🎉

You now know:
- ✅ What Django is and how to set it up
- ✅ How to create models and databases
- ✅ How to use the admin interface
- ✅ How to route URLs
- ✅ How to create views
- ✅ How to build templates

**Next steps:**
- Move to intermediate level
- Build a complete project
- Learn about forms
- Learn about authentication
- Learn about APIs

---

## 💡 Pro Tips

1. **Use template inheritance** - Saves time and keeps code DRY
2. **Organize templates by app** - Easier to find and maintain
3. **Use meaningful block names** - Makes templates clearer
4. **Always escape user input** - Django does this automatically, but be aware
5. **Use static files** - Keep CSS/JS separate from HTML
6. **Test templates** - Make sure they work with different data
7. **Use template tags** - They make templates more powerful

---

## 📝 Quick Reference

```html
<!-- Variables -->
{{ variable }}
{{ object.attribute }}

<!-- Tags -->
{% if condition %}...{% endif %}
{% for item in items %}...{% endfor %}
{% extends 'base.html' %}
{% block content %}...{% endblock %}
{% url 'name' %}
{% load static %}

<!-- Filters -->
{{ variable|upper }}
{{ variable|date:"F d, Y" }}
{{ variable|truncatewords:20 }}

<!-- Static Files -->
{% load static %}
{% static 'path/to/file.css' %}
```

