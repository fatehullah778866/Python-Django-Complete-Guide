# Project 6: Event Management System

## 📋 Project Overview

**Project Name:** Event Management System  
**Difficulty Level:** ⭐⭐⭐ Intermediate-Advanced  
**Estimated Time:** 5-6 days  
**Prerequisites:** Steps 1-11 (All basic-level concepts)

## 🎯 Project Description

Build a comprehensive event management system with date/time handling, filtering, statistics, and complex queries. This is the most advanced basic-level project.

## ✨ Features to Implement

### Core Features (Required)

1. **Event Management**
   - Create events with date/time
   - View all events
   - View event details
   - Edit events
   - Delete events
   - Filter events (upcoming, past, today)

2. **Event Model**
   - Title (CharField)
   - Description (TextField)
   - Event date (DateTimeField)
   - Location (CharField)
   - Capacity (IntegerField)
   - Category (ForeignKey)
   - Organizer (CharField)
   - Created date

3. **Category Management**
   - Event categories (Conference, Workshop, Meetup, etc.)
   - Filter by category
   - Category statistics

4. **Date/Time Features**
   - Filter upcoming events
   - Filter past events
   - Filter today's events
   - Filter this week's events
   - Sort by date

5. **Statistics Dashboard**
   - Total events
   - Upcoming events count
   - Past events count
   - Events by category
   - Events this month
   - Most popular categories

6. **Search & Filter**
   - Search by title/description
   - Filter by date range
   - Filter by category
   - Filter by location
   - Combined filters

### Optional Features (Challenges)

1. **RSVP System**
   - RSVP to events
   - Track attendees
   - Capacity management
   - Waitlist (if capacity full)

2. **Event Status**
   - Published/Draft
   - Cancelled
   - Postponed
   - Status management

3. **Advanced Filtering**
   - Filter by month
   - Filter by year
   - Filter by location
   - Custom date ranges
   - Multiple filters combined

4. **Calendar View**
   - Monthly calendar
   - Events on calendar
   - Click to view event

5. **Notifications**
   - Upcoming events reminder
   - Event updates
   - Email notifications (if you know email)

6. **Event Details Enhancement**
   - Event image
   - Event tags
   - Related events
   - Event duration
   - Recurring events (advanced)

7. **Analytics**
   - Event attendance trends
   - Popular event times
   - Popular locations
   - Category popularity

## 🏗️ Project Structure

```
eventmanager/
├── manage.py
├── eventmanager/
│   ├── settings.py
│   └── urls.py
├── events/
│   ├── models.py          # Event, Category models
│   ├── views.py           # All views with complex queries
│   ├── urls.py            # URLs
│   ├── forms.py           # EventForm
│   ├── admin.py           # Admin config
│   ├── templates/
│   │   └── events/
│   │       ├── base.html
│   │       ├── event_list.html
│   │       ├── event_detail.html
│   │       ├── event_form.html
│   │       ├── dashboard.html
│   │       └── filter_results.html
│   └── static/
│       └── events/
│           └── css/
│               └── style.css
└── db.sqlite3
```

## 📝 Step-by-Step Plan

### Phase 1: Setup (30 minutes)
1. Create Django project
2. Create events app
3. Configure settings
4. Set up timezone
5. Configure URLs

### Phase 2: Models (2 hours)
1. Create Category model
2. Create Event model with DateTimeField
3. Add proper field types
4. Create migrations
5. Register in admin
6. Add test data with various dates

### Phase 3: Forms (1.5 hours)
1. Create EventForm
2. Handle DateTimeField in forms
3. Add date/time widgets
4. Form validation
5. Test date input

### Phase 4: Views - Basic (2 hours)
1. Event list view
2. Event detail view
3. Event create view
4. Event update view
5. Event delete view

### Phase 5: Views - Advanced (3 hours)
1. Filter upcoming events
2. Filter past events
3. Filter today's events
4. Filter this week's events
5. Search functionality
6. Combined filters
7. Statistics view

### Phase 6: Templates (4 hours)
1. Base template
2. Event list with filters
3. Event detail
4. Event form with date picker
5. Dashboard/Statistics page
6. Filter results page
7. Responsive design

### Phase 7: Advanced Features (3 hours)
1. Implement all filters
2. Add statistics
3. Date calculations
4. Query optimization
5. Admin enhancements

### Phase 8: Polish (2 hours)
1. Improve UI/UX
2. Add helpful messages
3. Test edge cases
4. Optimize queries
5. Final touches

## 🎓 Learning Objectives

By completing this project, you will:

- ✅ Master DateTimeField handling
- ✅ Work with date/time queries
- ✅ Implement complex filtering
- ✅ Use date calculations
- ✅ Create statistics and aggregations
- ✅ Optimize database queries
- ✅ Handle timezones
- ✅ Build complex views
- ✅ Create advanced user interfaces

## 🔧 Technologies Used

- Django 4.2+
- Python 3.8+
- SQLite
- HTML/CSS
- JavaScript (for date pickers)
- Django ORM (advanced queries)

## 📊 Database Schema

```
Category
├── id (AutoField, Primary Key)
├── name (CharField, max_length=50, unique=True)
└── description (TextField, optional)

Event
├── id (AutoField, Primary Key)
├── title (CharField, max_length=200)
├── description (TextField)
├── event_date (DateTimeField)
├── location (CharField, max_length=200)
├── capacity (IntegerField, optional)
├── organizer (CharField, max_length=100)
├── category (ForeignKey → Category)
├── created_at (DateTimeField, auto_now_add)
└── updated_at (DateTimeField, auto_now)
```

## 🎨 UI/UX Requirements

### Pages Needed

1. **Event List Page**
   - All events or filtered events
   - Event cards with date/time
   - Location
   - Category badge
   - Filter buttons (All, Upcoming, Past, Today)
   - Search bar
   - Category filter
   - Sort options

2. **Event Detail Page**
   - Full event information
   - Date and time (formatted)
   - Location
   - Category
   - Description
   - Capacity info
   - Edit/Delete buttons

3. **Event Form**
   - Title input
   - Description textarea
   - Event date/time picker
   - Location input
   - Capacity input
   - Organizer input
   - Category dropdown

4. **Dashboard/Statistics**
   - Total events
   - Upcoming count
   - Past count
   - Events by category (chart/table)
   - Recent events
   - This month's events

## ✅ Success Criteria

Your project is complete when:

- [ ] Can create events with date/time
- [ ] Can view all events
- [ ] Can filter upcoming events
- [ ] Can filter past events
- [ ] Can filter today's events
- [ ] Can search events
- [ ] Can filter by category
- [ ] Statistics are accurate
- [ ] Date/time displays correctly
- [ ] Forms handle dates properly
- [ ] All queries work efficiently
- [ ] UI is user-friendly

## 🚀 Getting Started

1. Review this project plan
2. Complete all basic-level steps
3. Understand DateTimeField
4. Review date/time queries
5. Follow step-by-step guide (when available)
6. Build incrementally
7. Test date filtering thoroughly

## 💡 Tips

- **Understand timezones** - Django handles them
- Use `timezone.now()` for current time
- Test with various dates (past, present, future)
- Use `__gte`, `__lte` for date comparisons
- Optimize queries with `select_related`
- Make date inputs user-friendly
- Handle timezone-aware datetimes
- Test edge cases (midnight, year boundaries)

## 🎯 Next Steps

After completing this project:
- Add optional features
- Move to intermediate level
- Or enhance with authentication
- Deploy your projects!

---

**Status:** 📝 Planned - Waiting for guide creation

