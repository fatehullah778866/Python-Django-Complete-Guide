# Project 2: Todo List Application

## 📋 Project Overview

**Project Name:** Todo List Application  
**Difficulty Level:** ⭐⭐ Beginner-Intermediate  
**Estimated Time:** 2-3 days  
**Prerequisites:** Steps 1-10 (Introduction through Forms)

## 🎯 Project Description

Build a functional todo list application where users can manage their tasks. This project focuses heavily on forms, form validation, and user interaction patterns.

## ✨ Features to Implement

### Core Features (Required)

1. **Task Management**
   - Add new tasks
   - View all tasks
   - Mark tasks as complete/incomplete
   - Edit existing tasks
   - Delete tasks
   - See task count (total, completed, pending)

2. **Task Model**
   - Title (CharField, required)
   - Description (TextField, optional)
   - Completed (BooleanField, default False)
   - Created date (DateTimeField)
   - Due date (DateField, optional)
   - Priority (CharField with choices: Low, Medium, High)

3. **User Interface**
   - Task list with checkboxes
   - Filter buttons (All, Active, Completed)
   - Add task form
   - Edit task form
   - Delete confirmation
   - Task statistics display

4. **Form Features**
   - Form validation
   - Error messages
   - Success messages
   - Pre-filled forms for editing

### Optional Features (Challenges)

1. **Search Functionality**
   - Search tasks by title or description
   - Real-time search results

2. **Sorting**
   - Sort by date (newest/oldest)
   - Sort by priority
   - Sort by completion status

3. **Categories/Tags**
   - Add categories to tasks
   - Filter by category
   - Color-coded categories

4. **Due Date Alerts**
   - Highlight overdue tasks
   - Show tasks due today
   - Show tasks due this week

5. **Bulk Operations**
   - Select multiple tasks
   - Mark multiple as complete
   - Delete multiple tasks

6. **Statistics Dashboard**
   - Total tasks
   - Completed percentage
   - Tasks by priority
   - Completion trends

## 🏗️ Project Structure

```
todolist/
├── manage.py
├── todolist/
│   ├── settings.py
│   └── urls.py
├── tasks/
│   ├── models.py          # Task model
│   ├── views.py           # All views
│   ├── urls.py            # Task URLs
│   ├── forms.py           # TaskForm
│   ├── admin.py           # Admin config
│   └── templates/
│       └── tasks/
│           ├── base.html
│           ├── task_list.html
│           ├── task_form.html
│           └── task_confirm_delete.html
└── db.sqlite3
```

## 📝 Step-by-Step Plan

### Phase 1: Setup (30 minutes)
1. Create Django project
2. Create tasks app
3. Configure settings
4. Set up URLs

### Phase 2: Model (45 minutes)
1. Create Task model with all fields
2. Add choices for priority
3. Create migrations
4. Register in admin
5. Add test data

### Phase 3: Forms (1 hour)
1. Create TaskForm (ModelForm)
2. Customize form fields
3. Add validation
4. Customize widgets
5. Add help text

### Phase 4: Views (2 hours)
1. Task list view (with filtering)
2. Task create view
3. Task update view
4. Task delete view
5. Toggle complete view
6. Filter views (all, active, completed)

### Phase 5: Templates (2 hours)
1. Base template with navigation
2. Task list template with filters
3. Task form template
4. Delete confirmation
5. Statistics display
6. CSS styling

### Phase 6: Testing & Enhancement (1 hour)
1. Test all features
2. Add success/error messages
3. Improve UX
4. Add JavaScript (optional)
5. Polish styling

## 🎓 Learning Objectives

By completing this project, you will:

- ✅ Master Django Forms and ModelForms
- ✅ Understand form validation
- ✅ Handle GET and POST requests
- ✅ Implement filtering and searching
- ✅ Use BooleanField effectively
- ✅ Work with choices in models
- ✅ Create interactive user interfaces
- ✅ Handle form errors gracefully

## 🔧 Technologies Used

- Django 4.2+
- Python 3.8+
- SQLite
- HTML/CSS
- JavaScript (optional, for enhancements)

## 📊 Database Schema

```
Task
├── id (AutoField, Primary Key)
├── title (CharField, max_length=200, required)
├── description (TextField, optional)
├── completed (BooleanField, default=False)
├── priority (CharField, choices: Low/Medium/High)
├── due_date (DateField, optional)
├── created_at (DateTimeField, auto_now_add)
└── updated_at (DateTimeField, auto_now)
```

## 🎨 UI/UX Requirements

### Pages Needed

1. **Task List Page**
   - List of all tasks
   - Checkbox to mark complete/incomplete
   - Task title, description, priority, due date
   - Filter buttons (All, Active, Completed)
   - Add Task button
   - Edit/Delete links
   - Statistics section

2. **Add/Edit Task Form**
   - Title input (required)
   - Description textarea
   - Priority dropdown
   - Due date picker
   - Completed checkbox (for edit only)
   - Save button
   - Cancel button

3. **Delete Confirmation**
   - Task details
   - Warning message
   - Confirm/Cancel buttons

## ✅ Success Criteria

Your project is complete when:

- [ ] Can add new tasks
- [ ] Can view all tasks
- [ ] Can mark tasks as complete/incomplete
- [ ] Can edit tasks
- [ ] Can delete tasks
- [ ] Can filter tasks (All, Active, Completed)
- [ ] Form validation works correctly
- [ ] Success/error messages display
- [ ] Statistics are accurate
- [ ] UI is user-friendly
- [ ] All features work without errors

## 🚀 Getting Started

1. Review this project plan
2. Complete Steps 1-10 (especially Forms)
3. Set up development environment
4. Follow step-by-step guide (when available)
5. Build incrementally
6. Test each feature

## 💡 Tips

- Focus on forms - this project is about form handling
- Make the UI intuitive - users should understand how to use it
- Add helpful validation messages
- Use ModelForms to save time
- Test edge cases (empty forms, invalid data)
- Make filtering work smoothly

## 🎯 Next Steps

After completing this project:
- Add optional features
- Move to Project 3: Contact Form
- Or enhance with JavaScript for better UX

---

**Status:** 📝 Planned - Waiting for guide creation

