# Project 1: Personal Blog

## 📋 Project Overview

**Project Name:** Personal Blog  
**Difficulty Level:** ⭐ Beginner  
**Estimated Time:** 2-3 days  
**Prerequisites:** Steps 1-9 (Introduction through Templates)

## 🎯 Project Description

Build a complete personal blog application where you can create, read, update, and delete blog posts. This is your first complete Django project that brings together all the basic concepts you've learned.

## ✨ Features to Implement

### Core Features (Required)

1. **Blog Post Management**
   - Create new blog posts
   - View all blog posts (list view)
   - View individual blog post (detail view)
   - Edit existing blog posts
   - Delete blog posts
   - Confirmation before deletion

2. **Post Model**
   - Title (CharField, max 200 characters)
   - Content (TextField)
   - Author (CharField, max 100 characters)
   - Created date (DateTimeField, auto-set)
   - Updated date (DateTimeField, auto-update)

3. **User Interface**
   - Homepage showing all posts
   - Individual post detail page
   - Create/Edit post form
   - Delete confirmation page
   - Navigation menu
   - Basic CSS styling

4. **Django Admin**
   - Register Post model
   - Customize admin display
   - Add search and filters

### Optional Features (Challenges)

1. **Categories**
   - Add category field to posts
   - Filter posts by category
   - Category model with relationship

2. **Tags**
   - Add tags to posts (Many-to-Many)
   - Filter by tags
   - Tag cloud display

3. **Excerpt/Summary**
   - Add excerpt field
   - Show excerpt on list page
   - Full content on detail page

4. **Pagination**
   - Show 5-10 posts per page
   - Previous/Next navigation

5. **Search**
   - Search posts by title or content
   - Search results page

6. **Styling**
   - Better CSS design
   - Responsive layout (mobile-friendly)
   - Custom fonts and colors

## 🏗️ Project Structure

```
myblog/
├── manage.py
├── myblog/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── blog/
│   ├── models.py          # Post model
│   ├── views.py           # All CRUD views
│   ├── urls.py            # Blog URLs
│   ├── forms.py           # PostForm (ModelForm)
│   ├── admin.py           # Admin configuration
│   └── templates/
│       └── blog/
│           ├── base.html
│           ├── post_list.html
│           ├── post_detail.html
│           ├── post_form.html
│           └── post_confirm_delete.html
└── db.sqlite3
```

## 📝 Step-by-Step Plan

### Phase 1: Setup (30 minutes)
1. Create Django project
2. Create blog app
3. Register app in settings
4. Set up basic URLs

### Phase 2: Model (30 minutes)
1. Create Post model
2. Create and apply migrations
3. Register in admin
4. Create superuser
5. Add test data via admin

### Phase 3: Views & URLs (1 hour)
1. Create post_list view
2. Create post_detail view
3. Create post_create view
4. Create post_update view
5. Create post_delete view
6. Set up URLs for all views

### Phase 4: Forms (30 minutes)
1. Create PostForm (ModelForm)
2. Customize form fields
3. Add form validation

### Phase 5: Templates (2 hours)
1. Create base template
2. Create post_list template
3. Create post_detail template
4. Create post_form template
5. Create delete confirmation template
6. Add basic CSS styling

### Phase 6: Testing & Polish (1 hour)
1. Test all CRUD operations
2. Fix any bugs
3. Improve styling
4. Add navigation
5. Test user experience

## 🎓 Learning Objectives

By completing this project, you will:

- ✅ Understand complete CRUD operations
- ✅ Practice Model-View-Template pattern
- ✅ Use ModelForms effectively
- ✅ Create and organize templates
- ✅ Set up URL routing
- ✅ Customize Django admin
- ✅ Handle form submissions
- ✅ Build a complete working application

## 🔧 Technologies Used

- Django 4.2+
- Python 3.8+
- SQLite (default database)
- HTML/CSS
- Django Template Language

## 📊 Database Schema

```
Post
├── id (AutoField, Primary Key)
├── title (CharField, max_length=200)
├── content (TextField)
├── author (CharField, max_length=100)
├── created_at (DateTimeField)
└── updated_at (DateTimeField)
```

## 🎨 UI/UX Requirements

### Pages Needed

1. **Homepage (Post List)**
   - Show all posts
   - Post title (link to detail)
   - Author name
   - Created date
   - Excerpt/preview
   - "Create New Post" button
   - Edit/Delete links for each post

2. **Post Detail Page**
   - Full post title
   - Author and date
   - Full content
   - Edit button
   - Delete button
   - Back to list link

3. **Create/Edit Post Form**
   - Title input
   - Content textarea
   - Author input
   - Save button
   - Cancel button
   - Form validation errors

4. **Delete Confirmation**
   - Post title
   - Warning message
   - Confirm button
   - Cancel button

## ✅ Success Criteria

Your project is complete when:

- [ ] Can create new posts
- [ ] Can view all posts on homepage
- [ ] Can view individual post details
- [ ] Can edit existing posts
- [ ] Can delete posts (with confirmation)
- [ ] All forms validate correctly
- [ ] Admin panel works for managing posts
- [ ] Navigation works between pages
- [ ] Basic styling is applied
- [ ] No errors in browser console
- [ ] All URLs work correctly

## 🚀 Getting Started

1. Review this project plan
2. Make sure you've completed Steps 1-9
3. Set up your development environment
4. Follow the step-by-step guide (when available)
5. Build the project feature by feature
6. Test everything thoroughly

## 💡 Tips

- Start with the model, then views, then templates
- Test each feature as you build it
- Use Django admin to add test data
- Keep your code organized
- Commit to Git regularly
- Don't worry about perfect styling initially

## 🎯 Next Steps

After completing this project:
- Try the optional features (categories, tags)
- Move to Project 2: Todo List
- Or enhance this project with more features

---

**Status:** 📝 Planned - Waiting for guide creation

