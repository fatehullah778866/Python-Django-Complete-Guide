# Project 4: Book Library Manager

## 📋 Project Overview

**Project Name:** Book Library Manager  
**Difficulty Level:** ⭐⭐ Intermediate  
**Estimated Time:** 3-4 days  
**Prerequisites:** Steps 1-11 (All basic-level concepts)

## 🎯 Project Description

Build a comprehensive library management system with books, authors, and categories. This project focuses on model relationships (ForeignKey, ManyToMany) and complex queries.

## ✨ Features to Implement

### Core Features (Required)

1. **Book Management**
   - Add books with details
   - View all books
   - View book details
   - Edit books
   - Delete books
   - Search books

2. **Author Management**
   - Add authors
   - View all authors
   - View author details (with their books)
   - Edit authors
   - Delete authors

3. **Category Management**
   - Add categories
   - View categories
   - Assign categories to books
   - Filter books by category

4. **Models & Relationships**
   - Book model (ForeignKey to Author, ManyToMany to Category)
   - Author model
   - Category model
   - Proper relationships

5. **Advanced Features**
   - Search functionality
   - Filter by author
   - Filter by category
   - Book statistics
   - Author statistics

### Optional Features (Challenges)

1. **Book Ratings**
   - Add rating field
   - Average rating calculation
   - Sort by rating

2. **Book Status**
   - Available/Borrowed/Reserved
   - Track book availability
   - Borrowing history

3. **Advanced Search**
   - Search by title, author, category
   - Advanced filters
   - Search results highlighting

4. **Pagination**
   - Paginate book list
   - Paginate author list

5. **Statistics Dashboard**
   - Total books
   - Total authors
   - Books per category
   - Most popular authors
   - Recently added books

6. **Book Details Enhancement**
   - ISBN display
   - Publication date
   - Page count
   - Book cover image (optional)

## 🏗️ Project Structure

```
library/
├── manage.py
├── library/
│   ├── settings.py
│   └── urls.py
├── books/
│   ├── models.py          # Book, Author, Category models
│   ├── views.py           # All views
│   ├── urls.py            # URLs
│   ├── forms.py           # BookForm, AuthorForm
│   ├── admin.py           # Admin config
│   └── templates/
│       └── books/
│           ├── base.html
│           ├── book_list.html
│           ├── book_detail.html
│           ├── book_form.html
│           ├── author_list.html
│           ├── author_detail.html
│           └── category_list.html
└── db.sqlite3
```

## 📝 Step-by-Step Plan

### Phase 1: Setup (30 minutes)
1. Create Django project
2. Create books app
3. Configure settings
4. Set up URLs

### Phase 2: Models (2 hours)
1. Create Author model
2. Create Category model
3. Create Book model with relationships
4. Create migrations
5. Register all in admin
6. Add test data

### Phase 3: Forms (1.5 hours)
1. Create AuthorForm
2. Create CategoryForm
3. Create BookForm (with relationships)
4. Customize form fields
5. Handle ManyToMany in forms

### Phase 4: Views (3 hours)
1. Book list view (with filters)
2. Book detail view
3. Book create/edit/delete views
4. Author list view
5. Author detail view (with books)
6. Author create/edit/delete views
7. Category views
8. Search view

### Phase 5: Templates (3 hours)
1. Base template
2. Book list template
3. Book detail template
4. Book form template
5. Author templates
6. Category templates
7. Search results template
8. Navigation and filters

### Phase 6: Advanced Features (2 hours)
1. Implement search
2. Add filtering
3. Add statistics
4. Improve admin
5. Polish UI

## 🎓 Learning Objectives

By completing this project, you will:

- ✅ Master model relationships (ForeignKey, ManyToMany)
- ✅ Understand related objects
- ✅ Work with complex queries
- ✅ Handle ManyToMany in forms
- ✅ Create related object views
- ✅ Implement search and filtering
- ✅ Use select_related and prefetch_related
- ✅ Build complex data models

## 🔧 Technologies Used

- Django 4.2+
- Python 3.8+
- SQLite
- HTML/CSS
- Django ORM (advanced queries)

## 📊 Database Schema

```
Author
├── id (AutoField, Primary Key)
├── name (CharField, max_length=100)
├── bio (TextField, optional)
├── birth_date (DateField, optional)
└── nationality (CharField, optional)

Category
├── id (AutoField, Primary Key)
├── name (CharField, max_length=50, unique=True)
└── description (TextField, optional)

Book
├── id (AutoField, Primary Key)
├── title (CharField, max_length=200)
├── author (ForeignKey → Author)
├── isbn (CharField, max_length=13, unique, optional)
├── publication_date (DateField, optional)
├── pages (IntegerField, optional)
├── description (TextField, optional)
├── categories (ManyToMany → Category)
├── created_at (DateTimeField, auto_now_add)
└── updated_at (DateTimeField, auto_now)
```

## 🎨 UI/UX Requirements

### Pages Needed

1. **Book List Page**
   - All books with cover/title
   - Author name
   - Categories
   - Search bar
   - Filter by author dropdown
   - Filter by category
   - Add Book button

2. **Book Detail Page**
   - Full book information
   - Author (link to author page)
   - Categories (links)
   - Description
   - Edit/Delete buttons

3. **Author List Page**
   - All authors
   - Book count per author
   - Add Author button

4. **Author Detail Page**
   - Author information
   - List of all books by author
   - Edit/Delete buttons

5. **Book Form**
   - Title, Author (dropdown)
   - ISBN, Publication date
   - Pages, Description
   - Categories (checkboxes)
   - Save/Cancel buttons

## ✅ Success Criteria

Your project is complete when:

- [ ] Can create books with author and categories
- [ ] Can view all books
- [ ] Can view book details
- [ ] Can edit and delete books
- [ ] Can manage authors
- [ ] Can manage categories
- [ ] Can search books
- [ ] Can filter by author
- [ ] Can filter by category
- [ ] Author detail shows their books
- [ ] Relationships work correctly
- [ ] Admin panel works for all models

## 🚀 Getting Started

1. Review this project plan
2. Complete all basic-level steps
3. Understand model relationships
4. Follow step-by-step guide (when available)
5. Build models first, then views
6. Test relationships thoroughly

## 💡 Tips

- **Start with models** - Get relationships right first
- Use `select_related` for ForeignKey
- Use `prefetch_related` for ManyToMany
- Test with sample data
- Make sure forms handle relationships correctly
- Use admin to add test data easily
- Focus on understanding relationships

## 🎯 Next Steps

After completing this project:
- Add optional features
- Move to Project 5: Recipe Platform
- Or enhance with more relationships

---

**Status:** 📝 Planned - Waiting for guide creation

