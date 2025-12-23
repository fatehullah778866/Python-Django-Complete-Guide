# Step 7: URL Routing

## 🎯 What You'll Learn

In this step, you'll learn:
- What URL routing is (in simple words)
- Understanding URLconf
- How to create URL patterns
- Named URLs and reverse()
- URL namespaces
- Including other URLconfs

---

## 🤔 What is URL Routing?

### Simple Explanation

**URL routing is like a map that tells Django: "When someone visits this URL, show them this page."**

**Real-world analogy:**
Think of a restaurant:
- **URL** = The table number (like "Table 5")
- **Routing** = The waiter knows "Table 5 gets the menu"
- **View** = The menu (what the customer sees)

**Another analogy:**
- **URL** = An address (like "123 Main Street")
- **Routing** = The postal service knows where to deliver
- **View** = The house at that address (what you see)

### Technical Definition

URL routing (URLconf) is the mechanism Django uses to map URL patterns to views. When a user requests a URL, Django uses the URLconf to find the matching view function.

**Breaking it down:**
- **URL pattern** = A pattern that matches certain URLs
- **View** = The function that handles the request
- **Mapping** = Connecting URLs to views

### How It Works

**Step 1: User visits a URL**
```
User types: http://127.0.0.1:8000/blog/
```

**Step 2: Django looks at urls.py**
```
Django: "Let me check my map..."
```

**Step 3: Django finds a match**
```
Django: "blog/ matches this pattern, so I'll use this view"
```

**Step 4: Django calls the view**
```
Django: "Hey view function, show this user the blog page!"
```

**Step 5: View returns a response**
```
View: "Here's the HTML page!"
Django: "Perfect! Sending it to the user."
```

---

## 📝 Understanding URLconf

### What is URLconf?

**URLconf** = **URL Configuration**

**Simple explanation:**
URLconf is the file (urls.py) that contains all your URL patterns.

**Where is it?**
- Main project: `myfirstproject/urls.py`
- Each app can have: `blog/urls.py`

### The Main URLs File

**File:** `myfirstproject/urls.py`

**What's in it:**
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
- **Important:** Must be named `urlpatterns`!

**Line 5: `path('admin/', admin.site.urls)`**
- **`path()`** = Creates a URL pattern
- **`'admin/'`** = The URL pattern (matches /admin/)
- **`admin.site.urls`** = What to show (the admin interface)
- **Simple explanation:** "If someone visits /admin/, show the admin page"

---

## 🛠️ Creating URL Patterns

### Basic URL Pattern

**Syntax:**
```python
path('url-pattern/', view_function, name='url_name')
```

**Breaking it down:**
- **`'url-pattern/'`** = The URL to match
- **`view_function`** = The function to call
- **`name='url_name'`** = Optional name for the URL

### Example 1: Simple Home Page

**Step 1: Create a view**

**File:** `blog/views.py`
```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to my blog!")
```

**Step 2: Create URL pattern**

**File:** `myfirstproject/urls.py`
```python
from django.contrib import admin
from django.urls import path
from blog import views  # ← Import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # ← Add this!
]
```

**Line-by-line:**

**Line 3: `from blog import views`**
- Imports views from the blog app
- **Simple explanation:** "Get the view functions from blog app"

**Line 7: `path('', views.home, name='home')`**
- **`''`** = Empty string = homepage (matches /)
- **`views.home`** = The home function in views.py
- **`name='home'`** = Name this URL "home"
- **Simple explanation:** "If someone visits the homepage, show them the home view"

**Test it:**
Visit: `http://127.0.0.1:8000/`
You should see: "Welcome to my blog!"

### Example 2: Blog List Page

**Step 1: Create view**

**File:** `blog/views.py`
```python
from django.http import HttpResponse

def blog_list(request):
    return HttpResponse("Here are all the blog posts!")
```

**Step 2: Add URL pattern**

**File:** `myfirstproject/urls.py`
```python
from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('blog/', views.blog_list, name='blog_list'),  # ← Add this!
]
```

**What this does:**
- Matches: `http://127.0.0.1:8000/blog/`
- Shows: "Here are all the blog posts!"

### Example 3: Blog Detail Page (with parameters)

**Step 1: Create view**

**File:** `blog/views.py`
```python
from django.http import HttpResponse

def blog_detail(request, post_id):
    return HttpResponse(f"Blog post number {post_id}")
```

**Step 2: Add URL pattern**

**File:** `myfirstproject/urls.py`
```python
from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/<int:post_id>/', views.blog_detail, name='blog_detail'),  # ← Add this!
]
```

**Line-by-line:**

**`path('blog/<int:post_id>/', ...)`**
- **`'blog/'`** = Matches /blog/
- **`<int:post_id>`** = Captures an integer, calls it post_id
- **`/`** = End of URL
- **Simple explanation:** "Match /blog/ followed by a number, save that number as post_id"

**How it works:**
- URL: `http://127.0.0.1:8000/blog/5/`
- Django captures: `post_id = 5`
- Django calls: `blog_detail(request, post_id=5)`
- View shows: "Blog post number 5"

### URL Pattern Types

#### 1. String (str)
```python
path('blog/<str:slug>/', views.post_detail)
```
- Matches any string
- Example: `/blog/my-first-post/`

#### 2. Integer (int)
```python
path('blog/<int:post_id>/', views.post_detail)
```
- Matches whole numbers only
- Example: `/blog/5/`

#### 3. Slug (slug)
```python
path('blog/<slug:slug>/', views.post_detail)
```
- Matches URL-friendly strings (letters, numbers, hyphens, underscores)
- Example: `/blog/my-first-post/`

#### 4. UUID (uuid)
```python
path('blog/<uuid:post_id>/', views.post_detail)
```
- Matches UUID format
- Example: `/blog/550e8400-e29b-41d4-a716-446655440000/`

#### 5. Path (path)
```python
path('files/<path:file_path>/', views.serve_file)
```
- Matches any string including slashes
- Example: `/files/images/photo.jpg/`

---

## 🏷️ Named URLs and reverse()

### What are Named URLs?

**Simple explanation:**
Named URLs give your URLs friendly names so you can refer to them easily.

**Without names:**
```python
path('blog/', views.blog_list)  # No name
```
- Hard to reference in templates
- If URL changes, you have to update everywhere

**With names:**
```python
path('blog/', views.blog_list, name='blog_list')  # Has a name!
```
- Easy to reference: `{% url 'blog_list' %}`
- If URL changes, only change it once!

### Using Named URLs in Templates

**In HTML templates:**
```html
<a href="{% url 'blog_list' %}">View All Posts</a>
```

**What this does:**
- Django looks up the URL named 'blog_list'
- Replaces `{% url 'blog_list' %}` with the actual URL
- Result: `<a href="/blog/">View All Posts</a>`

### Using reverse() in Python Code

**What is reverse()?**
`reverse()` is a function that gets the URL from a name.

**Example:**
```python
from django.urls import reverse

# Get the URL for 'blog_list'
url = reverse('blog_list')
# Result: '/blog/'

# Use it in a redirect
from django.shortcuts import redirect
return redirect(reverse('blog_list'))
```

**Line-by-line:**

**Line 1: `from django.urls import reverse`**
- Imports the reverse function
- **Simple explanation:** "Get the tool to get URLs from names"

**Line 4: `url = reverse('blog_list')`**
- Gets the URL for the name 'blog_list'
- **Simple explanation:** "What URL is named 'blog_list'?"

**Line 8: `return redirect(reverse('blog_list'))`**
- Redirects to the blog_list URL
- **Simple explanation:** "Send user to the blog list page"

### Why Use Named URLs?

1. **Easy to change**: Change URL once, works everywhere
2. **No hardcoding**: Don't write URLs manually
3. **Less errors**: Django checks if URL exists
4. **Better code**: More maintainable

---

## 📦 URL Namespaces

### What are Namespaces?

**Simple explanation:**
Namespaces prevent URL name conflicts when you have multiple apps.

**Problem without namespaces:**
- Blog app has: `name='detail'`
- Shop app has: `name='detail'`
- **Conflict!** Which one is which?

**Solution with namespaces:**
- Blog app: `blog:detail`
- Shop app: `shop:detail`
- **No conflict!** They're in different namespaces

### How to Use Namespaces

**Step 1: Include app URLs with namespace**

**File:** `myfirstproject/urls.py`
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace='blog')),  # ← Add namespace!
]
```

**Line-by-line:**

**Line 2: `from django.urls import path, include`**
- Imports `include` function
- **Simple explanation:** "Get the tool to include other URL files"

**Line 5: `path('blog/', include('blog.urls', namespace='blog'))`**
- **`'blog/'`** = URL prefix
- **`include('blog.urls')`** = Include URLs from blog/urls.py
- **`namespace='blog'`** = Namespace name
- **Simple explanation:** "All URLs from blog/urls.py are in the 'blog' namespace"

**Step 2: Create app URLs file**

**File:** `blog/urls.py` (create this file)
```python
from django.urls import path
from . import views

app_name = 'blog'  # ← Set app name

urlpatterns = [
    path('', views.blog_list, name='list'),
    path('<int:post_id>/', views.blog_detail, name='detail'),
]
```

**Line-by-line:**

**Line 4: `app_name = 'blog'`**
- Sets the app name (for namespace)
- **Simple explanation:** "This app's namespace is 'blog'"

**Line 6: `urlpatterns = [`**
- List of URL patterns for this app
- **Simple explanation:** "Here are this app's URLs"

**Line 7: `path('', views.blog_list, name='list')`**
- Empty string = matches after the prefix
- **Simple explanation:** "Matches /blog/ (because prefix is 'blog/')"

**Line 8: `path('<int:post_id>/', views.blog_detail, name='detail')`**
- Matches /blog/5/
- **Simple explanation:** "Matches /blog/ followed by a number"

**Step 3: Use namespaced URLs**

**In templates:**
```html
<a href="{% url 'blog:list' %}">All Posts</a>
<a href="{% url 'blog:detail' post_id=5 %}">Post 5</a>
```

**In Python:**
```python
from django.urls import reverse

url = reverse('blog:list')  # Gets /blog/
url = reverse('blog:detail', args=[5])  # Gets /blog/5/
```

---

## 🔗 Including Other URLconfs

### Why Include URLs?

**Simple explanation:**
Instead of putting all URLs in one file, split them into separate files for each app.

**Benefits:**
- **Organized**: Each app manages its own URLs
- **Reusable**: Apps can be used in other projects
- **Cleaner**: Main urls.py stays simple

### How to Include URLs

**Step 1: Create app URLs file**

**File:** `blog/urls.py`
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('<int:post_id>/', views.blog_detail, name='blog_detail'),
]
```

**Step 2: Include in main URLs**

**File:** `myfirstproject/urls.py`
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),  # ← Include blog URLs!
    path('', include('blog.urls')),  # Or include at root
]
```

**Line-by-line:**

**Line 5: `path('blog/', include('blog.urls'))`**
- **`'blog/'`** = URL prefix
- **`include('blog.urls')`** = Include URLs from blog/urls.py
- **Simple explanation:** "All URLs from blog/urls.py start with /blog/"

**Result:**
- `blog/urls.py` has: `path('', ...)` → becomes `/blog/`
- `blog/urls.py` has: `path('<int:post_id>/', ...)` → becomes `/blog/5/`

---

## 📝 URL Patterns with Regex (Advanced)

### Using re_path for Complex Patterns

**For very complex patterns, use `re_path`:**

```python
from django.urls import path, re_path
from . import views

urlpatterns = [
    # Simple pattern
    path('blog/<int:post_id>/', views.detail),
    
    # Complex pattern with regex
    re_path(r'^blog/(?P<year>\d{4})/(?P<month>\d{2})/$', views.archive),
]
```

**Line-by-line:**

**Line 7: `re_path(r'^blog/(?P<year>\d{4})/(?P<month>\d{2})/$', views.archive)`**
- **`re_path`** = Uses regular expressions
- **`r'...'`** = Raw string (for regex)
- **`^blog/`** = Must start with "blog/"
- **`(?P<year>\d{4})`** = Capture 4 digits, call it "year"
- **`(?P<month>\d{2})`** = Capture 2 digits, call it "month"
- **`/$`** = Must end with "/"

**Example matches:**
- `/blog/2025/12/` → year=2025, month=12
- `/blog/2024/01/` → year=2024, month=01

**⚠️ Note:** Use `path()` when possible, it's simpler!

---

## ✅ Complete Example

**File structure:**
```
myfirstproject/
├── urls.py          (main URLs)
└── blog/
    ├── urls.py      (blog URLs)
    └── views.py     (blog views)
```

**File: `myfirstproject/urls.py`**
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace='blog')),
    path('', include('blog.urls')),  # Homepage URLs
]
```

**File: `blog/urls.py`**
```python
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog_list, name='list'),
    path('<int:post_id>/', views.blog_detail, name='detail'),
    path('category/<str:category>/', views.category_posts, name='category'),
]
```

**File: `blog/views.py`**
```python
from django.http import HttpResponse

def blog_list(request):
    return HttpResponse("All blog posts")

def blog_detail(request, post_id):
    return HttpResponse(f"Blog post {post_id}")

def category_posts(request, category):
    return HttpResponse(f"Posts in category: {category}")
```

**URLs that work:**
- `/blog/` → blog_list
- `/blog/5/` → blog_detail (post_id=5)
- `/blog/category/python/` → category_posts (category='python')

---

## ✅ Checklist: URL Routing Complete

Before moving to Step 8, make sure you can:

- [ ] Explain what URL routing is
- [ ] Create a basic URL pattern
- [ ] Use URL parameters (<int:id>, <str:slug>)
- [ ] Name URLs and use them in templates
- [ ] Use reverse() in Python code
- [ ] Include URLs from other apps
- [ ] Use URL namespaces

---

## 🐛 Common Problems

### Problem: "NoReverseMatch"

**Solution:**
- Check that URL name exists
- Check namespace is correct: `'blog:detail'` not `'detail'`
- Make sure app is in INSTALLED_APPS

### Problem: "404 Page Not Found"

**Solution:**
- Check URL pattern matches the URL you're visiting
- Check for typos in URL
- Make sure view function exists
- Restart development server

### Problem: "URL pattern not working"

**Solution:**
- Check URL pattern syntax
- Make sure view is imported correctly
- Check for trailing slashes (Django adds them automatically)

---

## 🚀 Ready for Step 8?

Excellent! You now understand URL routing!

Next, you'll learn about Views - the functions that handle requests and return responses. Go to [Step 8: Views](./step-8-views.md)

---

## 💡 Pro Tips

1. **Always name your URLs** - Makes templates and code cleaner
2. **Use namespaces** - Prevents conflicts between apps
3. **Split URLs by app** - One urls.py per app
4. **Use path() not re_path()** - Simpler and easier to read
5. **Test URLs** - Visit them in browser to make sure they work
6. **Keep URLs simple** - Easy to remember and type

---

## 📝 Quick Reference

```python
# Basic pattern
path('url/', views.function, name='name')

# With parameter
path('blog/<int:post_id>/', views.detail, name='detail')

# Include other URLs
path('blog/', include('blog.urls'))

# With namespace
path('blog/', include('blog.urls', namespace='blog'))

# In templates
{% url 'name' %}
{% url 'blog:detail' post_id=5 %}

# In Python
from django.urls import reverse
reverse('name')
reverse('blog:detail', args=[5])
```

