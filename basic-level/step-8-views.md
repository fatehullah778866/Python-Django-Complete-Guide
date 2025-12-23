# Step 8: Views

## 🎯 What You'll Learn

In this step, you'll learn:
- What views are (in simple words)
- Function-based views (FBV)
- Class-based views (CBV) basics
- Request and response objects
- HTTP methods (GET, POST)
- View decorators

---

## 🤔 What is a View?

### Simple Explanation

**A view is a function (or class) that takes a web request and returns a web response.**

**Real-world analogy:**
Think of a restaurant:
- **Request** = Customer orders food
- **View** = The chef prepares the food
- **Response** = The waiter brings the food to the customer

**Another analogy:**
- **Request** = You ask a question
- **View** = The brain thinks and answers
- **Response** = You get the answer

### Technical Definition

A view is a Python function (or class) that receives a web request and returns a web response. The response can be HTML, JSON, an image, or anything else.

**Breaking it down:**
- **Request** = Information about what the user wants
- **View** = The function that processes the request
- **Response** = What gets sent back to the user

### What Views Do

**Views can:**
- Show web pages (HTML)
- Return data (JSON)
- Handle form submissions
- Process user input
- Query the database
- Do calculations
- Return files

**Views are the "brain" of your website!**

---

## 📝 Function-Based Views (FBV)

### What are Function-Based Views?

**Simple explanation:**
Function-based views are just Python functions that handle requests.

**Example:**
```python
def my_view(request):
    return HttpResponse("Hello, World!")
```

**That's it!** A function that takes `request` and returns a response.

### Basic View Example

**File:** `blog/views.py`
```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to my blog!")
```

**Line-by-line explanation:**

**Line 1: `from django.http import HttpResponse`**
- Imports HttpResponse class
- **Simple explanation:** "Get the tool to send text responses"

**Line 3: `def home(request):`**
- Defines a function called `home`
- **`request`** = The HTTP request object (required!)
- **Simple explanation:** "This function handles requests"

**Line 4: `return HttpResponse("Welcome to my blog!")`**
- Creates an HTTP response with text
- Returns it to the user
- **Simple explanation:** "Send this text to the user"

**Connect to URL:**
```python
# urls.py
path('', views.home, name='home')
```

**Result:**
- User visits: `http://127.0.0.1:8000/`
- Sees: "Welcome to my blog!"

### View with Parameters

**View that uses URL parameters:**
```python
from django.http import HttpResponse

def blog_detail(request, post_id):
    return HttpResponse(f"Blog post number {post_id}")
```

**Line-by-line:**

**Line 3: `def blog_detail(request, post_id):`**
- **`request`** = HTTP request (always first!)
- **`post_id`** = Parameter from URL
- **Simple explanation:** "This function gets post_id from the URL"

**Line 4: `return HttpResponse(f"Blog post number {post_id}")`**
- Uses f-string to include post_id
- **Simple explanation:** "Show the post number"

**URL pattern:**
```python
path('blog/<int:post_id>/', views.blog_detail, name='detail')
```

**How it works:**
- URL: `/blog/5/`
- Django calls: `blog_detail(request, post_id=5)`
- User sees: "Blog post number 5"

---

## 📦 Understanding Request Object

### What is the Request Object?

**Simple explanation:**
The request object contains all information about the user's request.

**What's inside:**
- What URL they visited
- What data they sent
- Their browser information
- Cookies
- User information
- And much more!

### Common Request Attributes

#### 1. request.method

**What it is:** The HTTP method (GET, POST, etc.)

**Example:**
```python
def my_view(request):
    if request.method == 'GET':
        return HttpResponse("This is a GET request")
    elif request.method == 'POST':
        return HttpResponse("This is a POST request")
```

**Line-by-line:**

**Line 2: `if request.method == 'GET':`**
- Checks if request is GET
- **Simple explanation:** "Did the user just visit the page?"

**Line 3: `return HttpResponse("This is a GET request")`**
- Returns response for GET
- **Simple explanation:** "Show this for GET requests"

**Line 4: `elif request.method == 'POST':`**
- Checks if request is POST
- **Simple explanation:** "Did the user submit a form?"

#### 2. request.GET

**What it is:** Data from URL parameters (query string)

**Example URL:** `/blog/?search=django&page=2`

**Code:**
```python
def search_view(request):
    search_term = request.GET.get('search', '')
    page = request.GET.get('page', '1')
    return HttpResponse(f"Searching for: {search_term}, Page: {page}")
```

**Line-by-line:**

**Line 2: `search_term = request.GET.get('search', '')`**
- Gets 'search' parameter from URL
- **`''`** = Default value if not found
- **Simple explanation:** "Get the search term, or empty string if not found"

**Line 3: `page = request.GET.get('page', '1')`**
- Gets 'page' parameter
- Default is '1'
- **Simple explanation:** "Get the page number, default to 1"

#### 3. request.POST

**What it is:** Data from form submissions

**Example:**
```python
def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        return HttpResponse(f"Thank you, {name}!")
    else:
        return HttpResponse("Please submit the form")
```

**Line-by-line:**

**Line 2: `if request.method == 'POST':`**
- Checks if form was submitted
- **Simple explanation:** "Did the user submit the form?"

**Line 3-5: Getting form data**
- Gets data from the form
- **Simple explanation:** "Get what the user typed in the form"

#### 4. request.user

**What it is:** The current user (if logged in)

**Example:**
```python
def profile_view(request):
    if request.user.is_authenticated:
        return HttpResponse(f"Hello, {request.user.username}!")
    else:
        return HttpResponse("Please log in")
```

**Line-by-line:**

**Line 2: `if request.user.is_authenticated:`**
- Checks if user is logged in
- **Simple explanation:** "Is the user logged in?"

**Line 3: `return HttpResponse(f"Hello, {request.user.username}!")`**
- Shows username
- **Simple explanation:** "Say hello to the logged-in user"

#### 5. request.path

**What it is:** The path of the URL

**Example:**
```python
def debug_view(request):
    return HttpResponse(f"You visited: {request.path}")
```

**Result:**
- If you visit `/blog/`, shows: "You visited: /blog/"

---

## 📤 Understanding Response Objects

### Types of Responses

#### 1. HttpResponse - Basic Response

**What it is:** Returns plain text or HTML

**Example:**
```python
from django.http import HttpResponse

def my_view(request):
    return HttpResponse("Hello, World!")
    # Or with HTML:
    return HttpResponse("<h1>Hello, World!</h1>")
```

#### 2. JsonResponse - JSON Data

**What it is:** Returns JSON data (for APIs)

**Example:**
```python
from django.http import JsonResponse

def api_view(request):
    data = {
        'name': 'John',
        'age': 30,
        'city': 'New York'
    }
    return JsonResponse(data)
```

**Result:**
```json
{"name": "John", "age": 30, "city": "New York"}
```

#### 3. HttpResponseRedirect - Redirect

**What it is:** Sends user to another page

**Example:**
```python
from django.http import HttpResponseRedirect
from django.urls import reverse

def redirect_view(request):
    return HttpResponseRedirect(reverse('home'))
    # Or:
    return HttpResponseRedirect('/blog/')
```

#### 4. FileResponse - File Download

**What it is:** Sends a file to the user

**Example:**
```python
from django.http import FileResponse

def download_view(request):
    file = open('document.pdf', 'rb')
    return FileResponse(file)
```

### Using render() for Templates

**Most common:** Render HTML templates

**Example:**
```python
from django.shortcuts import render

def blog_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/list.html', {'posts': posts})
```

**Line-by-line:**

**Line 1: `from django.shortcuts import render`**
- Imports render function
- **Simple explanation:** "Get the tool to render templates"

**Line 4: `posts = Post.objects.all()`**
- Gets all posts from database
- **Simple explanation:** "Get all blog posts"

**Line 5: `return render(request, 'blog/list.html', {'posts': posts})`**
- **`request`** = The request object
- **`'blog/list.html'`** = Template file to use
- **`{'posts': posts}`** = Data to pass to template
- **Simple explanation:** "Show the list.html template with posts data"

**We'll learn more about templates in Step 9!**

---

## 🔄 HTTP Methods

### What are HTTP Methods?

**Simple explanation:**
HTTP methods tell the server what the user wants to do.

**Common methods:**
- **GET** = Get information (view a page)
- **POST** = Send information (submit a form)
- **PUT** = Update information
- **DELETE** = Delete information

### GET vs POST

#### GET Request

**When used:**
- Visiting a page
- Clicking a link
- Searching

**Characteristics:**
- Data in URL
- Can be bookmarked
- Visible in browser history
- Limited data size

**Example:**
```python
def search_view(request):
    if request.method == 'GET':
        query = request.GET.get('q', '')
        # Search and return results
        return HttpResponse(f"Search results for: {query}")
```

#### POST Request

**When used:**
- Submitting forms
- Uploading files
- Deleting data

**Characteristics:**
- Data in request body (not URL)
- Not visible in URL
- Can send large data
- More secure for sensitive data

**Example:**
```python
def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        # Save to database
        return HttpResponse("Thank you for contacting us!")
    else:
        # Show the form
        return render(request, 'contact.html')
```

### Handling Both GET and POST

**Common pattern:**
```python
def form_view(request):
    if request.method == 'POST':
        # Process form submission
        name = request.POST.get('name')
        # Save data
        return HttpResponseRedirect(reverse('success'))
    else:
        # Show the form
        return render(request, 'form.html')
```

**Line-by-line:**

**Line 2: `if request.method == 'POST':`**
- Checks if form was submitted
- **Simple explanation:** "Did the user submit the form?"

**Line 3-5: Process form**
- Gets form data
- Saves it
- **Simple explanation:** "Save what the user entered"

**Line 6: `return HttpResponseRedirect(...)`**
- Redirects after success
- **Simple explanation:** "Send user to success page"

**Line 7: `else:`**
- If not POST (i.e., GET)
- **Simple explanation:** "Otherwise, show the form"

**Line 8: `return render(request, 'form.html')`**
- Shows the form
- **Simple explanation:** "Show the form page"

---

## 🎨 Class-Based Views (CBV) Basics

### What are Class-Based Views?

**Simple explanation:**
Class-based views use classes instead of functions. They're more organized for complex views.

**Function-based:**
```python
def blog_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/list.html', {'posts': posts})
```

**Class-based:**
```python
from django.views.generic import ListView

class BlogListView(ListView):
    model = Post
    template_name = 'blog/list.html'
    context_object_name = 'posts'
```

### Basic Class-Based Views

#### 1. ListView - Show a List

**What it does:** Shows a list of objects

**Example:**
```python
from django.views.generic import ListView
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
```

**Line-by-line:**

**Line 1: `from django.views.generic import ListView`**
- Imports ListView class
- **Simple explanation:** "Get the tool to show lists"

**Line 4: `class PostListView(ListView):`**
- Creates a class that inherits from ListView
- **Simple explanation:** "This class shows a list"

**Line 5: `model = Post`**
- Which model to show
- **Simple explanation:** "Show Post objects"

**Line 6: `template_name = 'blog/post_list.html'`**
- Which template to use
- **Simple explanation:** "Use this template"

**Line 7: `context_object_name = 'posts'`**
- Name in template
- **Simple explanation:** "In template, call it 'posts'"

**URL:**
```python
path('posts/', PostListView.as_view(), name='post_list')
```

#### 2. DetailView - Show One Object

**What it does:** Shows details of one object

**Example:**
```python
from django.views.generic import DetailView
from .models import Post

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
```

**URL:**
```python
path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail')
```

**Note:** Uses `pk` (primary key) instead of custom parameter!

#### 3. CreateView - Create New Object

**What it does:** Shows form to create new object

**Example:**
```python
from django.views.generic import CreateView
from .models import Post

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content', 'author']
    template_name = 'blog/post_form.html'
    success_url = '/posts/'
```

**Line-by-line:**

**Line 5: `fields = ['title', 'content', 'author']`**
- Which fields to show in form
- **Simple explanation:** "Show these fields in the form"

**Line 7: `success_url = '/posts/'`**
- Where to redirect after success
- **Simple explanation:** "After creating, go here"

### When to Use CBV vs FBV?

**Use Function-Based Views when:**
- Simple views
- Learning Django
- Need full control
- Custom logic

**Use Class-Based Views when:**
- Standard CRUD operations
- Want less code
- Need built-in features
- Following Django patterns

---

## 🎭 View Decorators

### What are Decorators?

**Simple explanation:**
Decorators are like "wrappers" that add functionality to views.

**Syntax:**
```python
@decorator_name
def my_view(request):
    return HttpResponse("Hello")
```

**The `@` symbol** = This is a decorator

### Common Decorators

#### 1. @login_required

**What it does:** Requires user to be logged in

**Example:**
```python
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def profile_view(request):
    return render(request, 'profile.html')
```

**What happens:**
- If user not logged in → Redirects to login page
- If user logged in → Shows the page

**Line-by-line:**

**Line 1: `from django.contrib.auth.decorators import login_required`**
- Imports login_required decorator
- **Simple explanation:** "Get the tool to require login"

**Line 4: `@login_required`**
- Decorator that requires login
- **Simple explanation:** "Only logged-in users can see this"

#### 2. @csrf_exempt

**What it does:** Disables CSRF protection (use carefully!)

**Example:**
```python
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def api_view(request):
    # Handle API request without CSRF token
    return JsonResponse({'status': 'ok'})
```

**⚠️ Warning:** Only use for APIs, not regular forms!

#### 3. @require_http_methods

**What it does:** Only allows specific HTTP methods

**Example:**
```python
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET", "POST"])
def my_view(request):
    return HttpResponse("Only GET or POST allowed")
```

**What happens:**
- GET or POST → Works
- PUT or DELETE → Returns 405 error

#### 4. @require_POST

**What it does:** Only allows POST requests

**Example:**
```python
from django.views.decorators.http import require_POST

@require_POST
def delete_view(request):
    # Only works with POST
    return HttpResponse("Deleted!")
```

### Combining Decorators

**You can use multiple decorators:**
```python
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

@login_required
@require_POST
def delete_post(request, post_id):
    # Must be logged in AND use POST
    # Delete the post
    return HttpResponseRedirect('/posts/')
```

**Order matters!** They execute from bottom to top.

---

## ✅ Complete View Examples

### Example 1: Blog List with Search

```python
from django.shortcuts import render
from .models import Post

def blog_list(request):
    posts = Post.objects.all()
    
    # Handle search
    search = request.GET.get('search', '')
    if search:
        posts = posts.filter(title__icontains=search)
    
    context = {
        'posts': posts,
        'search': search
    }
    return render(request, 'blog/list.html', context)
```

### Example 2: Contact Form

```python
from django.shortcuts import render, redirect
from django.contrib import messages

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Save to database or send email
        # ...
        
        messages.success(request, 'Thank you for contacting us!')
        return redirect('home')
    else:
        return render(request, 'contact.html')
```

### Example 3: Class-Based View with Custom Logic

```python
from django.views.generic import ListView
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(title__icontains=search)
        return queryset
```

---

## ✅ Checklist: Views Complete

Before moving to Step 9, make sure you can:

- [ ] Explain what a view is
- [ ] Create a function-based view
- [ ] Understand request and response objects
- [ ] Handle GET and POST requests
- [ ] Use basic class-based views
- [ ] Use view decorators
- [ ] Render templates with data

---

## 🐛 Common Problems

### Problem: "View function must take at least one argument"

**Solution:**
- Views must have `request` as first parameter
- `def my_view(request):` ✅
- `def my_view():` ❌

### Problem: "CSRF verification failed"

**Solution:**
- Add `{% csrf_token %}` to forms
- Or use `@csrf_exempt` (only for APIs!)

### Problem: "TemplateDoesNotExist"

**Solution:**
- Check template path is correct
- Check TEMPLATES setting in settings.py
- Make sure template file exists

---

## 🚀 Ready for Step 9?

Excellent! You now understand views!

Next, you'll learn about Templates - how to create beautiful HTML pages. Go to [Step 9: Templates](./step-9-templates.md)

---

## 💡 Pro Tips

1. **Keep views simple** - Move complex logic to separate functions
2. **Use render()** - Easier than HttpResponse for HTML
3. **Handle both GET and POST** - Most forms need this
4. **Use decorators** - They save time and add security
5. **Try class-based views** - They're powerful for standard operations
6. **Test your views** - Make sure they work with different inputs

---

## 📝 Quick Reference

```python
# Function-based view
def my_view(request):
    return HttpResponse("Hello")

# With template
def my_view(request):
    return render(request, 'template.html', {'data': data})

# Class-based view
class MyListView(ListView):
    model = MyModel
    template_name = 'list.html'

# With decorator
@login_required
def protected_view(request):
    return render(request, 'protected.html')
```

