# Project 5: Recipe Sharing Platform

## 📋 Project Overview

**Project Name:** Recipe Sharing Platform  
**Difficulty Level:** ⭐⭐ Intermediate  
**Estimated Time:** 4-5 days  
**Prerequisites:** Steps 1-11 (All basic-level concepts)

## 🎯 Project Description

Build a recipe sharing platform where users can create, view, and search recipes with images. This project focuses on file uploads, image handling, and rich content management.

## ✨ Features to Implement

### Core Features (Required)

1. **Recipe Management**
   - Create recipes with images
   - View all recipes
   - View recipe details
   - Edit recipes
   - Delete recipes
   - Search recipes

2. **Recipe Model**
   - Title (CharField)
   - Description (TextField)
   - Image (ImageField)
   - Ingredients (TextField or JSON)
   - Instructions (TextField)
   - Cooking time (IntegerField, minutes)
   - Servings (IntegerField)
   - Difficulty (CharField with choices)
   - Category (ForeignKey)
   - Created date

3. **Category Management**
   - Categories (Breakfast, Lunch, Dinner, Dessert, etc.)
   - Filter recipes by category
   - Category pages

4. **File Uploads**
   - Upload recipe images
   - Display images
   - Handle image validation
   - Image resizing (optional)

5. **User Interface**
   - Recipe cards with images
   - Recipe detail page
   - Category navigation
   - Search functionality
   - Pagination

### Optional Features (Challenges)

1. **Advanced Image Handling**
   - Multiple images per recipe
   - Image gallery
   - Thumbnail generation
   - Image optimization

2. **Recipe Features**
   - Recipe ratings
   - Favorite recipes
   - Recipe tags
   - Related recipes

3. **Search & Filter**
   - Search by ingredients
   - Filter by cooking time
   - Filter by difficulty
   - Filter by category
   - Advanced search

4. **Recipe Display**
   - Print-friendly version
   - Share recipe (social media)
   - Recipe nutrition info (optional)
   - Cooking tips section

5. **User Features**
   - User accounts (if you know authentication)
   - User's recipe collection
   - Recipe comments (if you know authentication)

6. **Statistics**
   - Most viewed recipes
   - Popular categories
   - Recent recipes
   - Recipe count by category

## 🏗️ Project Structure

```
recipeplatform/
├── manage.py
├── recipeplatform/
│   ├── settings.py
│   └── urls.py
├── recipes/
│   ├── models.py          # Recipe, Category models
│   ├── views.py           # All views
│   ├── urls.py            # URLs
│   ├── forms.py           # RecipeForm
│   ├── admin.py           # Admin config
│   ├── templates/
│   │   └── recipes/
│   │       ├── base.html
│   │       ├── recipe_list.html
│   │       ├── recipe_detail.html
│   │       ├── recipe_form.html
│   │       └── category_list.html
│   └── static/
│       └── recipes/
│           └── css/
│               └── style.css
├── media/                 # User-uploaded files
│   └── recipe_images/
└── db.sqlite3
```

## 📝 Step-by-Step Plan

### Phase 1: Setup (1 hour)
1. Create Django project
2. Create recipes app
3. Configure media files
4. Install Pillow (for images)
5. Configure settings

### Phase 2: Models (2 hours)
1. Create Category model
2. Create Recipe model with ImageField
3. Set up media file handling
4. Create migrations
5. Register in admin
6. Test image upload in admin

### Phase 3: Forms (2 hours)
1. Create RecipeForm (ModelForm)
2. Handle ImageField
3. Add form validation
4. Customize form layout
5. Test file upload

### Phase 4: Views (3 hours)
1. Recipe list view (with pagination)
2. Recipe detail view
3. Recipe create view (with file upload)
4. Recipe update view
5. Recipe delete view
6. Category views
7. Search view

### Phase 5: Templates (4 hours)
1. Base template
2. Recipe list (card layout)
3. Recipe detail (with image)
4. Recipe form (with file upload)
5. Category pages
6. Search results
7. Responsive design

### Phase 6: Media & Static (2 hours)
1. Configure media URLs
2. Test image uploads
3. Display images in templates
4. Add CSS styling
5. Make responsive

### Phase 7: Polish (2 hours)
1. Add pagination
2. Improve search
3. Add filters
4. Enhance UI
5. Test everything

## 🎓 Learning Objectives

By completing this project, you will:

- ✅ Master file and image uploads
- ✅ Work with ImageField and FileField
- ✅ Configure media files
- ✅ Handle file validation
- ✅ Display uploaded images
- ✅ Implement pagination
- ✅ Create rich content forms
- ✅ Build image-heavy applications

## 🔧 Technologies Used

- Django 4.2+
- Python 3.8+
- Pillow (for image handling)
- SQLite
- HTML/CSS
- JavaScript (optional)

## 📊 Database Schema

```
Category
├── id (AutoField, Primary Key)
├── name (CharField, max_length=50, unique=True)
└── slug (SlugField, unique=True)

Recipe
├── id (AutoField, Primary Key)
├── title (CharField, max_length=200)
├── description (TextField)
├── image (ImageField, upload_to='recipe_images/')
├── ingredients (TextField)
├── instructions (TextField)
├── cooking_time (IntegerField, minutes)
├── servings (IntegerField)
├── difficulty (CharField, choices: Easy/Medium/Hard)
├── category (ForeignKey → Category)
├── created_at (DateTimeField, auto_now_add)
└── updated_at (DateTimeField, auto_now)
```

## 🎨 UI/UX Requirements

### Pages Needed

1. **Recipe List Page**
   - Recipe cards with images
   - Recipe title
   - Category
   - Cooking time
   - Difficulty badge
   - Pagination
   - Category filter
   - Search bar

2. **Recipe Detail Page**
   - Large recipe image
   - Full recipe information
   - Ingredients list
   - Step-by-step instructions
   - Cooking time and servings
   - Category link
   - Edit/Delete buttons

3. **Recipe Form**
   - Title input
   - Description textarea
   - Image upload field
   - Ingredients textarea
   - Instructions textarea
   - Cooking time, servings inputs
   - Difficulty dropdown
   - Category dropdown
   - Image preview (optional)

4. **Category Pages**
   - Recipes in that category
   - Category description
   - Recipe cards

## ✅ Success Criteria

Your project is complete when:

- [ ] Can upload recipe images
- [ ] Images display correctly
- [ ] Can create recipes with all fields
- [ ] Can view all recipes
- [ ] Can view recipe details
- [ ] Can edit recipes
- [ ] Can delete recipes
- [ ] Can filter by category
- [ ] Can search recipes
- [ ] Pagination works
- [ ] Media files are served correctly
- [ ] Forms validate correctly
- [ ] UI looks good

## 🚀 Getting Started

1. Review this project plan
2. Complete all basic-level steps
3. Install Pillow: `pip install Pillow`
4. Understand file uploads
5. Follow step-by-step guide (when available)
6. Test image uploads early

## 💡 Tips

- **Install Pillow first** - Required for ImageField
- Configure MEDIA_URL and MEDIA_ROOT correctly
- Test image uploads in admin first
- Use proper image validation
- Handle missing images gracefully
- Optimize images if possible
- Make sure media files are served in development
- Use responsive images

## 🎯 Next Steps

After completing this project:
- Add multiple images
- Add image optimization
- Move to Project 6: Event Management
- Or enhance with more features

---

**Status:** 📝 Planned - Waiting for guide creation

