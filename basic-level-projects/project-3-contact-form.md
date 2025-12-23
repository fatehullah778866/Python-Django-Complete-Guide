# Project 3: Contact Form Website

## 📋 Project Overview

**Project Name:** Contact Form Website  
**Difficulty Level:** ⭐ Beginner  
**Estimated Time:** 1-2 days  
**Prerequisites:** Steps 1-10 (Introduction through Forms)

## 🎯 Project Description

Build a beautiful contact form website with a landing page. This project focuses on forms, static files, user feedback, and creating a polished user experience.

## ✨ Features to Implement

### Core Features (Required)

1. **Contact Form**
   - Name field (required)
   - Email field (required, validated)
   - Subject field (required)
   - Message field (required, textarea)
   - Submit button
   - Form validation

2. **Contact Model**
   - Name (CharField)
   - Email (EmailField)
   - Subject (CharField)
   - Message (TextField)
   - Submitted date (DateTimeField)
   - Read status (BooleanField, default False)

3. **User Interface**
   - Beautiful landing page
   - Contact form page
   - Success page
   - Error handling
   - Navigation menu

4. **Static Files**
   - Custom CSS styling
   - Images/logo (optional)
   - Responsive design
   - Modern UI design

5. **User Feedback**
   - Success messages
   - Error messages
   - Form validation feedback
   - Thank you page

### Optional Features (Challenges)

1. **Email Integration**
   - Send email when form is submitted
   - Email notifications
   - Email templates

2. **Admin Panel**
   - View all submissions
   - Mark as read/unread
   - Reply to submissions (via email)
   - Filter by date, read status

3. **Form Enhancements**
   - Honeypot field (spam protection)
   - CAPTCHA (optional)
   - File upload (for attachments)

4. **Landing Page Features**
   - About section
   - Services/Portfolio section
   - Testimonials
   - Social media links

5. **Analytics**
   - Track form submissions
   - Submission statistics
   - Popular subjects

## 🏗️ Project Structure

```
contactwebsite/
├── manage.py
├── contactwebsite/
│   ├── settings.py
│   └── urls.py
├── contact/
│   ├── models.py          # Contact model
│   ├── views.py           # Views
│   ├── urls.py            # URLs
│   ├── forms.py           # ContactForm
│   ├── admin.py           # Admin config
│   ├── templates/
│   │   └── contact/
│   │       ├── base.html
│   │       ├── index.html
│   │       ├── contact.html
│   │       └── success.html
│   └── static/
│       └── contact/
│           ├── css/
│           │   └── style.css
│           └── images/
└── db.sqlite3
```

## 📝 Step-by-Step Plan

### Phase 1: Setup (30 minutes)
1. Create Django project
2. Create contact app
3. Configure settings
4. Set up static files
5. Configure URLs

### Phase 2: Model (30 minutes)
1. Create Contact model
2. Create migrations
3. Register in admin
4. Test via admin

### Phase 3: Forms (1 hour)
1. Create ContactForm
2. Add validation
3. Customize fields
4. Add widgets and styling
5. Test form

### Phase 4: Views (1 hour)
1. Home/Landing page view
2. Contact form view (GET/POST)
3. Success page view
4. Handle form submission
5. Save to database

### Phase 5: Templates (2 hours)
1. Base template
2. Landing page (index.html)
3. Contact form page
4. Success page
5. Error handling

### Phase 6: Styling (2 hours)
1. Create CSS file
2. Design landing page
3. Style contact form
4. Make responsive
5. Add animations (optional)

### Phase 7: Polish (1 hour)
1. Add messages framework
2. Improve error handling
3. Test all scenarios
4. Final styling touches
5. Deploy or share

## 🎓 Learning Objectives

By completing this project, you will:

- ✅ Master form creation and validation
- ✅ Work with static files (CSS, images)
- ✅ Create beautiful user interfaces
- ✅ Handle form submissions properly
- ✅ Use Django messages framework
- ✅ Design responsive layouts
- ✅ Create user-friendly forms
- ✅ Build a complete website

## 🔧 Technologies Used

- Django 4.2+
- Python 3.8+
- SQLite
- HTML5/CSS3
- JavaScript (optional)

## 📊 Database Schema

```
Contact
├── id (AutoField, Primary Key)
├── name (CharField, max_length=100)
├── email (EmailField)
├── subject (CharField, max_length=200)
├── message (TextField)
├── submitted_at (DateTimeField, auto_now_add)
└── is_read (BooleanField, default=False)
```

## 🎨 UI/UX Requirements

### Pages Needed

1. **Landing Page (Home)**
   - Hero section with title
   - About/Introduction section
   - Call-to-action button (link to contact)
   - Navigation menu
   - Footer

2. **Contact Form Page**
   - Form with all fields
   - Labels and placeholders
   - Validation error messages
   - Submit button
   - Styled form layout

3. **Success Page**
   - Thank you message
   - Confirmation details
   - Link back to home
   - Optional: Link to submit another

## ✅ Success Criteria

Your project is complete when:

- [ ] Landing page looks professional
- [ ] Contact form works correctly
- [ ] Form validation works
- [ ] Success page displays after submission
- [ ] Error messages show for invalid input
- [ ] Form data saves to database
- [ ] Admin can view submissions
- [ ] CSS styling is applied
- [ ] Website is responsive (mobile-friendly)
- [ ] Navigation works smoothly
- [ ] No console errors

## 🚀 Getting Started

1. Review this project plan
2. Complete Steps 1-10
3. Set up development environment
4. Follow step-by-step guide (when available)
5. Design first, code second
6. Focus on user experience

## 💡 Tips

- **Design matters** - Make it look good!
- Use CSS frameworks (Bootstrap, Tailwind) if you want
- Focus on form validation - it's crucial
- Test with real data
- Make error messages helpful
- Keep the design simple but elegant
- Mobile-first approach recommended

## 🎯 Next Steps

After completing this project:
- Add email functionality
- Enhance landing page
- Move to Project 4: Book Library
- Or deploy it online!

---

**Status:** 📝 Planned - Waiting for guide creation

