# Basic Level - Projects Plan

## 🎯 Overview

This document outlines the projects you'll build to practice and master Django. Each project builds on the previous one, gradually increasing in complexity and introducing new concepts.

**Learning Approach:**
- Start with simple projects
- Gradually add more features
- Practice all concepts learned in Steps 1-11
- Build real, working applications

---

## 📋 Project List

### Project 1: Personal Blog (Basic CRUD)
**Difficulty:** ⭐⭐ (Beginner)
**Estimated Time:** 2-3 days
**Status:** 📝 Planned

**What You'll Build:**
A simple blog where you can create, read, update, and delete blog posts.

**Features:**
- ✅ View all blog posts on homepage
- ✅ Create new blog posts
- ✅ View individual post details
- ✅ Edit existing posts
- ✅ Delete posts
- ✅ Basic styling with CSS
- ✅ Admin panel for managing posts

**Concepts You'll Practice:**
- Models (Post model with title, content, author, dates)
- Migrations (creating and applying)
- Views (function-based views for CRUD)
- URLs (routing and parameters)
- Templates (inheritance, displaying data)
- Forms (ModelForm for creating/editing)
- Admin interface (registering and customizing)

**What You'll Learn:**
- Complete CRUD operations
- How all Django pieces work together
- Basic template design
- Form handling

---

### Project 2: Todo List Application
**Difficulty:** ⭐⭐ (Beginner)
**Estimated Time:** 2-3 days
**Status:** 📝 Planned

**What You'll Build:**
A todo list app where users can add, complete, and delete tasks.

**Features:**
- ✅ Add new tasks
- ✅ Mark tasks as complete/incomplete
- ✅ Delete tasks
- ✅ Filter tasks (all, active, completed)
- ✅ Show task count
- ✅ Due dates for tasks
- ✅ Priority levels (high, medium, low)

**Concepts You'll Practice:**
- Models (Task model with status, priority, due_date)
- Boolean fields (is_completed)
- Date fields (due_date)
- Choices fields (priority choices)
- Filtering in views (active vs completed)
- Template conditionals (showing different states)
- Form validation (required fields)

**What You'll Learn:**
- Working with boolean fields
- Date handling
- Filtering and querying
- Status management
- User experience improvements

---

### Project 3: Contact Form Website
**Difficulty:** ⭐ (Very Beginner)
**Estimated Time:** 1-2 days
**Status:** 📝 Planned

**What You'll Build:**
A simple website with a contact form that saves messages to the database.

**Features:**
- ✅ Homepage with information
- ✅ Contact form (name, email, subject, message)
- ✅ Form validation
- ✅ Save messages to database
- ✅ View all messages in admin
- ✅ Success/error messages
- ✅ Basic email notification (optional)

**Concepts You'll Practice:**
- Regular forms (not ModelForm)
- Form validation (custom and built-in)
- Form rendering in templates
- Error handling
- Messages framework
- Redirects

**What You'll Learn:**
- Form creation from scratch
- Validation techniques
- User feedback (messages)
- Simple website structure

---

### Project 4: Book Library Manager
**Difficulty:** ⭐⭐⭐ (Intermediate)
**Estimated Time:** 3-4 days
**Status:** 📝 Planned

**What You'll Build:**
A library management system to track books, authors, and categories.

**Features:**
- ✅ Add books with details (title, author, ISBN, pages, category)
- ✅ Add authors
- ✅ Add categories
- ✅ View all books
- ✅ Search books by title/author
- ✅ Filter by category
- ✅ Book detail page
- ✅ Edit and delete books
- ✅ Relationships (ForeignKey: Book → Author, Book → Category)

**Concepts You'll Practice:**
- Multiple models (Book, Author, Category)
- ForeignKey relationships
- Many-to-one relationships
- Query filtering (search, filter)
- Related objects
- Model relationships
- Complex queries

**What You'll Learn:**
- Database relationships
- Working with related data
- Search functionality
- Filtering data
- Model design

---

### Project 5: Recipe Sharing Platform
**Difficulty:** ⭐⭐⭐ (Intermediate)
**Estimated Time:** 4-5 days
**Status:** 📝 Planned

**What You'll Build:**
A platform where users can share recipes with ingredients and instructions.

**Features:**
- ✅ Create recipes (title, description, prep time, cook time)
- ✅ Add ingredients (many ingredients per recipe)
- ✅ Add cooking instructions (step-by-step)
- ✅ View all recipes
- ✅ Recipe detail page
- ✅ Search recipes
- ✅ Filter by cooking time
- ✅ Categories (appetizer, main course, dessert)
- ✅ Image upload (optional)

**Concepts You'll Practice:**
- Complex models (Recipe, Ingredient, Instruction)
- Many-to-many relationships (Recipe ↔ Ingredient)
- One-to-many relationships (Recipe → Instructions)
- Text fields and formatting
- Integer fields (time in minutes)
- ImageField (if adding images)
- File uploads

**What You'll Learn:**
- Complex relationships
- Many-to-many fields
- Working with related models
- Data organization
- Advanced model design

---

### Project 6: Student Grade Tracker
**Difficulty:** ⭐⭐⭐ (Intermediate)
**Estimated Time:** 3-4 days
**Status:** 📝 Planned

**What You'll Build:**
A system to track students, courses, and their grades.

**Features:**
- ✅ Add students (name, email, student ID)
- ✅ Add courses (name, code, credits)
- ✅ Add grades (student, course, score, date)
- ✅ View student's all grades
- ✅ View course's all grades
- ✅ Calculate GPA (optional)
- ✅ Filter by student or course
- ✅ Grade statistics

**Concepts You'll Practice:**
- Multiple models (Student, Course, Grade)
- ForeignKey relationships (Grade → Student, Grade → Course)
- Decimal fields (for scores)
- Calculations in views
- Aggregations
- Complex queries
- Data relationships

**What You'll Learn:**
- Complex data relationships
- Calculations in Django
- Aggregations
- Data analysis basics
- Report generation

---

### Project 7: Event Management System
**Difficulty:** ⭐⭐⭐⭐ (Advanced Beginner)
**Estimated Time:** 4-5 days
**Status:** 📝 Planned

**What You'll Build:**
A system to manage events, attendees, and event details.

**Features:**
- ✅ Create events (title, description, date, time, location)
- ✅ Add attendees to events
- ✅ View all events
- ✅ View event details with attendee list
- ✅ Filter events by date
- ✅ Search events
- ✅ Event categories
- ✅ Capacity limits
- ✅ Registration status

**Concepts You'll Practice:**
- Event model with DateTimeField
- Many-to-many (Event ↔ Attendee)
- Date/time handling
- Filtering by date
- Capacity management
- Status fields
- Complex views

**What You'll Learn:**
- Date/time operations
- Many-to-many relationships
- Capacity management
- Event planning logic
- Advanced filtering

---

### Project 8: Product Catalog (E-commerce Basics)
**Difficulty:** ⭐⭐⭐⭐ (Advanced Beginner)
**Estimated Time:** 5-6 days
**Status:** 📝 Planned

**What You'll Build:**
A product catalog for an online store (viewing only, no checkout).

**Features:**
- ✅ Add products (name, description, price, image, category)
- ✅ Add categories
- ✅ View all products
- ✅ Product detail page
- ✅ Filter by category
- ✅ Search products
- ✅ Price range filtering
- ✅ Sort by price (low to high, high to low)
- ✅ Product availability (in stock/out of stock)

**Concepts You'll Practice:**
- Product and Category models
- DecimalField (for prices)
- ImageField (product images)
- File uploads
- Advanced filtering
- Sorting
- Search functionality
- Boolean fields (in_stock)

**What You'll Learn:**
- E-commerce basics
- Image handling
- Price management
- Advanced queries
- Sorting and filtering
- Search implementation

---

## 🎓 Learning Progression

### Phase 1: Foundation (Projects 1-3)
**Focus:** Basic CRUD, Forms, Simple Models

- **Project 1:** Personal Blog - Master basic CRUD
- **Project 2:** Todo List - Add status and filtering
- **Project 3:** Contact Form - Focus on forms

**Skills Gained:**
- Complete CRUD operations
- Form handling
- Basic model design
- Template creation

### Phase 2: Relationships (Projects 4-6)
**Focus:** Model Relationships, Complex Queries

- **Project 4:** Book Library - ForeignKey relationships
- **Project 5:** Recipe Platform - Many-to-many relationships
- **Project 6:** Grade Tracker - Complex relationships and calculations

**Skills Gained:**
- Database relationships
- ForeignKey usage
- Many-to-many fields
- Complex queries
- Data filtering

### Phase 3: Advanced Features (Projects 7-8)
**Focus:** Advanced Features, Real-world Applications

- **Project 7:** Event Management - Date/time, capacity
- **Project 8:** Product Catalog - Images, sorting, advanced filtering

**Skills Gained:**
- Date/time handling
- File/image uploads
- Advanced filtering
- Sorting
- Real-world application design

---

## 📊 Project Comparison

| Project | Models | Relationships | Forms | Difficulty | Time |
|---------|--------|---------------|-------|------------|------|
| Personal Blog | 1 | None | ModelForm | ⭐⭐ | 2-3 days |
| Todo List | 1 | None | ModelForm | ⭐⭐ | 2-3 days |
| Contact Form | 1 | None | Regular Form | ⭐ | 1-2 days |
| Book Library | 3 | ForeignKey | ModelForm | ⭐⭐⭐ | 3-4 days |
| Recipe Platform | 3+ | Many-to-Many | ModelForm | ⭐⭐⭐ | 4-5 days |
| Grade Tracker | 3 | ForeignKey | ModelForm | ⭐⭐⭐ | 3-4 days |
| Event Management | 2+ | Many-to-Many | ModelForm | ⭐⭐⭐⭐ | 4-5 days |
| Product Catalog | 2+ | ForeignKey | ModelForm | ⭐⭐⭐⭐ | 5-6 days |

---

## 🎯 Project Selection Guide

### Start Here If:
- **New to Django:** Start with Project 1 (Personal Blog)
- **Want to practice forms:** Start with Project 3 (Contact Form)
- **Comfortable with basics:** Start with Project 4 (Book Library)

### Recommended Order:
1. **Project 1: Personal Blog** - Learn CRUD
2. **Project 3: Contact Form** - Master forms
3. **Project 2: Todo List** - Add status management
4. **Project 4: Book Library** - Learn relationships
5. **Project 5: Recipe Platform** - Complex relationships
6. **Project 6: Grade Tracker** - Calculations
7. **Project 7: Event Management** - Advanced features
8. **Project 8: Product Catalog** - Real-world application

---

## 📝 Project Requirements Template

Each project will include:

### 1. Project Overview
- What you're building
- Why you're building it
- What you'll learn

### 2. Features List
- Detailed feature requirements
- User stories
- Acceptance criteria

### 3. Step-by-Step Guide
- Model creation
- View creation
- URL configuration
- Template creation
- Form creation
- Testing instructions

### 4. Code Examples
- Complete code for each file
- Line-by-line explanations
- Best practices

### 5. Challenges & Extensions
- Additional features to add
- Practice exercises
- Ideas for improvement

### 6. Solution Files
- Complete working code
- Reference implementation
- Common mistakes to avoid

---

## 🚀 Getting Started

**When you're ready to start a project:**

1. **Choose a project** from the list above
2. **Read the project requirements** in detail
3. **Set up a new Django project** (follow Step 3 guide)
4. **Follow the step-by-step instructions**
5. **Test your application** thoroughly
6. **Try the challenges** to extend functionality

**Remember:**
- ✅ Take your time
- ✅ Understand each step
- ✅ Test frequently
- ✅ Don't skip steps
- ✅ Ask for help if stuck
- ✅ Experiment and learn!

---

## 📚 What Each Project Teaches

### Core Concepts Coverage:

**Models:**
- ✅ Basic models (Projects 1-3)
- ✅ ForeignKey relationships (Projects 4, 6, 8)
- ✅ Many-to-many relationships (Projects 5, 7)
- ✅ Complex model design (Projects 5-8)

**Views:**
- ✅ Function-based views (All projects)
- ✅ CRUD operations (Projects 1-8)
- ✅ Filtering and searching (Projects 4-8)
- ✅ Complex queries (Projects 6-8)

**Forms:**
- ✅ ModelForms (Projects 1, 2, 4-8)
- ✅ Regular forms (Project 3)
- ✅ Form validation (All projects)
- ✅ Custom widgets (Projects 5, 8)

**Templates:**
- ✅ Template inheritance (All projects)
- ✅ Displaying data (All projects)
- ✅ Forms in templates (All projects)
- ✅ Filtering and loops (Projects 2, 4-8)

**URLs:**
- ✅ Basic routing (All projects)
- ✅ URL parameters (All projects)
- ✅ Named URLs (All projects)
- ✅ URL namespaces (Projects 4-8)

---

## 🎉 Success Criteria

**You've mastered basic-level Django when you can:**
- ✅ Build a complete CRUD application
- ✅ Create models with relationships
- ✅ Handle forms and validation
- ✅ Design and implement templates
- ✅ Use Django admin effectively
- ✅ Debug common issues
- ✅ Follow Django best practices

**After completing these projects, you'll be ready for:**
- Intermediate-level Django topics
- User authentication
- REST APIs
- Advanced features
- Real-world projects

---

## 📅 Project Timeline (Suggested)

**Week 1-2:** Projects 1-3 (Foundation)
- Personal Blog
- Contact Form
- Todo List

**Week 3-4:** Projects 4-5 (Relationships)
- Book Library
- Recipe Platform

**Week 5-6:** Projects 6-7 (Advanced)
- Grade Tracker
- Event Management

**Week 7-8:** Project 8 (Real-world)
- Product Catalog

**Total Time:** 7-8 weeks for all projects

**Note:** Adjust timeline based on your learning pace!

---

## 💡 Tips for Success

1. **Start Simple:** Begin with Project 1, don't skip ahead
2. **Complete Each Project:** Finish one before starting the next
3. **Understand, Don't Copy:** Make sure you understand the code
4. **Experiment:** Try adding your own features
5. **Test Everything:** Make sure all features work
6. **Ask Questions:** Use the concepts learned in Steps 1-11
7. **Take Breaks:** Don't rush, learning takes time
8. **Celebrate Progress:** Each completed project is an achievement!

---

## 🔄 Project Status

- 📝 **Planned** - Project is planned, guide not yet created
- 📝 **In Progress** - Guide is being written
- ✅ **Ready** - Project guide is complete and ready to use
- 🎉 **Completed** - You've finished this project!

**Current Status:** All projects are planned and ready to be created one by one.

---

## 📞 Next Steps

**When you're ready:**
1. Tell me which project you want to start with
2. I'll create a detailed step-by-step guide for that project
3. Follow the guide to build your project
4. Move to the next project when ready

**Let's build something amazing!** 🚀

