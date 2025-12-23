# Step 2: Environment Setup

## 🎯 What You'll Learn

In this step, you'll learn:
- How to install Python
- How to create a virtual environment (your own isolated workspace)
- How to install Django
- How to set up your code editor
- How to use Django commands

---

## 📦 Part 1: Installing Python

### What is Python?

**Python** is a programming language - it's the language Django is written in. Think of it as the foundation of your house. You need Python before you can use Django.

### Why Do We Need Python?

Django is written in Python, so your computer needs Python installed to understand and run Django code.

**Analogy:**
- **Python** = The language you speak
- **Django** = A book written in that language
- You need to know the language to read the book!

### How to Check if Python is Already Installed

Before installing, let's check if you already have Python:

#### On Windows:
1. Open **Command Prompt** or **PowerShell**
2. Type: `python --version`
3. Press Enter

**What you might see:**
- ✅ `Python 3.9.7` (or similar) → You have Python! Skip to Part 2
- ❌ `'python' is not recognized` → You need to install Python

#### On Mac/Linux:
1. Open **Terminal**
2. Type: `python3 --version`
3. Press Enter

### Installing Python on Windows

**Step-by-step:**

1. **Go to the Python website:**
   - Visit: https://www.python.org/downloads/
   - Click the big yellow "Download Python" button

2. **Run the installer:**
   - Find the downloaded file (usually in Downloads folder)
   - Double-click it
   - **IMPORTANT**: Check the box that says "Add Python to PATH" ✅
   - Click "Install Now"

3. **Wait for installation:**
   - The installer will do its work
   - This might take a few minutes

4. **Verify installation:**
   - Open Command Prompt or PowerShell
   - Type: `python --version`
   - You should see something like: `Python 3.11.0`

**🎉 Success!** Python is now installed!

### Installing Python on Mac

**Option 1: Using the official installer**
1. Go to https://www.python.org/downloads/
2. Download the Mac installer
3. Run the installer
4. Follow the instructions

**Option 2: Using Homebrew (recommended for Mac)**
1. Open Terminal
2. Type: `brew install python3`
3. Press Enter
4. Wait for installation

### Installing Python on Linux

Most Linux systems come with Python, but you might need Python 3:

```bash
# On Ubuntu/Debian
sudo apt update
sudo apt install python3 python3-pip

# On Fedora
sudo dnf install python3 python3-pip
```

### What Version Do I Need?

- **Minimum**: Python 3.8
- **Recommended**: Python 3.9 or higher
- **Latest**: Always good to have the latest stable version

**How to check your version:**
```bash
python --version
# or
python3 --version
```

---

## 📦 Part 2: Understanding pip

### What is pip?

**pip** stands for "Pip Installs Packages" (or "Pip Installs Python").

**Simple explanation:**
- **pip** is a tool that installs Python packages (like Django)
- Think of it as an app store for Python tools
- It comes with Python automatically

### How to Check if pip is Installed

```bash
pip --version
# or
pip3 --version
```

You should see something like: `pip 23.0.1`

**If it doesn't work:**
- On Windows: `python -m pip --version`
- On Mac/Linux: `python3 -m pip --version`

---

## 🏠 Part 3: Creating Virtual Environments

### What is a Virtual Environment?

**Simple explanation:**
A virtual environment is like having a separate room in your house where you keep your Django project. Each project has its own room with its own tools.

**Why do we need it?**

**Problem without virtual environments:**
- You have Project A that needs Django version 3.0
- You have Project B that needs Django version 4.0
- They can't both use the same Django installation!

**Solution with virtual environments:**
- Project A has its own "room" with Django 3.0
- Project B has its own "room" with Django 4.0
- They don't interfere with each other!

**Real-world analogy:**
Think of a virtual environment like a lunchbox:
- Each project gets its own lunchbox
- Each lunchbox has its own food (packages)
- Food from one lunchbox doesn't mix with another

### Creating Your First Virtual Environment

**Step 1: Choose where to create it**

Create a folder for your Django projects:
```bash
# On Windows (PowerShell)
cd Desktop
mkdir DjangoProjects
cd DjangoProjects

# On Mac/Linux
cd ~/Desktop
mkdir DjangoProjects
cd DjangoProjects
```

**Step 2: Create the virtual environment**

```bash
# On Windows
python -m venv myenv

# On Mac/Linux
python3 -m venv myenv
```

**What just happened?**
- `python -m venv` = "Python, create a virtual environment"
- `myenv` = The name of your virtual environment (you can name it anything!)

**What was created?**
A folder called `myenv` with:
- Python interpreter (a copy of Python)
- pip (package installer)
- Other tools

### Activating the Virtual Environment

**Activating** means "entering the room" - you're telling your computer to use this specific environment.

#### On Windows (PowerShell):
```powershell
.\myenv\Scripts\Activate.ps1
```

**If you get an error about execution policy:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Then try activating again.

#### On Windows (Command Prompt):
```cmd
myenv\Scripts\activate
```

#### On Mac/Linux:
```bash
source myenv/bin/activate
```

**How do you know it's activated?**
You'll see `(myenv)` at the beginning of your command line:
```
(myenv) C:\Users\dell\Desktop\DjangoProjects>
```

**This means:** "I'm now working inside the myenv virtual environment!"

### Deactivating the Virtual Environment

When you're done working, you can "leave the room":

```bash
deactivate
```

The `(myenv)` will disappear, meaning you're back to your normal environment.

---

## 🎯 Part 4: Installing Django

### What is Django Installation?

Installing Django means downloading Django and putting it in your virtual environment so you can use it.

**Simple explanation:**
- Django is like a tool in a toolbox
- Installing Django = putting the tool in your toolbox (virtual environment)
- Once installed, you can use Django to build websites

### Installing Django Step-by-Step

**Step 1: Make sure your virtual environment is activated**

You should see `(myenv)` in your terminal. If not, activate it first!

**Step 2: Install Django**

```bash
pip install django
```

**What this command does:**
- `pip` = The installer tool
- `install` = "Put this in my environment"
- `django` = The package to install

**What happens:**
- pip downloads Django from the internet
- pip installs Django in your virtual environment
- This might take 1-2 minutes

**You'll see output like:**
```
Collecting django
  Downloading Django-4.2.7-py3-none-any.whl (8.0 MB)
Installing collected packages: django
Successfully installed django-4.2.7
```

**🎉 Success!** Django is now installed!

### Checking Django Installation

Make sure Django is installed correctly:

```bash
django-admin --version
```

You should see something like: `4.2.7`

**If it doesn't work:**
- Make sure your virtual environment is activated
- Try: `python -m django --version`

### Installing a Specific Django Version

Sometimes you need a specific version:

```bash
# Install Django version 4.2
pip install django==4.2.7

# Install the latest version
pip install django

# Upgrade to latest version
pip install --upgrade django
```

---

## 💻 Part 5: Setting Up Visual Studio Code (VS Code)

### What is a Code Editor?

A code editor is like a special word processor for writing code. It helps you write code more easily.

**Popular options:**
- **VS Code** (Visual Studio Code) - Most popular, free, recommended for this guide
- **PyCharm** - Made specifically for Python, has free version
- **Sublime Text** - Lightweight, fast
- **Atom** - Free, customizable

### Why VS Code?

**VS Code is recommended because:**
- ✅ **Free** - No cost
- ✅ **Works everywhere** - Windows, Mac, and Linux
- ✅ **Great for beginners** - Easy to use
- ✅ **Lots of extensions** - Add features easily
- ✅ **Built-in terminal** - Run commands without leaving the editor
- ✅ **Integrated Git** - Version control built-in
- ✅ **IntelliSense** - Code completion and suggestions
- ✅ **Debugging** - Find and fix errors easily

### Installing VS Code

**Step 1: Download VS Code**

1. Go to: https://code.visualstudio.com/
2. Click "Download for Windows" (or your operating system)
3. The download will start automatically

**Step 2: Install VS Code**

1. **Run the installer:**
   - Find the downloaded file (usually in Downloads folder)
   - Double-click `VSCodeUserSetup-x64-*.exe`

2. **During installation:**
   - ✅ Check "Add to PATH" (important!)
   - ✅ Check "Create desktop icon" (optional but helpful)
   - ✅ Check "Add 'Open with Code' action to Windows Explorer" (helpful!)

3. **Complete installation:**
   - Click "Finish"
   - VS Code will open automatically

**Step 3: Verify Installation**

1. Open Command Prompt or PowerShell
2. Type: `code --version`
3. You should see the version number (like `1.85.0`)

**If it doesn't work:**
- Restart your computer
- Or manually add VS Code to PATH

### Setting Up VS Code for Django Development

#### Step 1: Open VS Code

1. **From Start Menu:**
   - Click Start
   - Type "Visual Studio Code"
   - Click to open

2. **From Command Line:**
   ```powershell
   code
   ```

3. **From File Explorer:**
   - Right-click a folder
   - Select "Open with Code" (if you checked this during installation)

#### Step 2: Install Essential Extensions

**What are Extensions?**
Extensions add features to VS Code. Think of them as apps for your code editor.

**How to Install Extensions:**

1. **Open Extensions Panel:**
   - Click the Extensions icon (square icon on left sidebar)
   - Or press `Ctrl+Shift+X`

2. **Install Python Extension (REQUIRED):**
   - Search for: `Python`
   - Find the one by **Microsoft** (has Microsoft logo)
   - Click **Install**
   - **This is the most important extension!**

3. **Install Django Extension (Recommended):**
   - Search for: `Django`
   - Install: **"Django"** by Baptiste Darthenay
   - Provides Django template syntax highlighting

4. **Other Useful Extensions:**
   - **Python Docstring Generator** - Auto-generate documentation
   - **Error Lens** - Shows errors inline
   - **GitLens** - Better Git integration
   - **Prettier** - Code formatter
   - **Auto Rename Tag** - Rename HTML tags automatically

#### Step 3: Configure Python Interpreter

**What is a Python Interpreter?**
The Python interpreter is the program that runs your Python code. You need to tell VS Code which Python to use (the one in your virtual environment).

**How to Select Interpreter:**

**Method 1: Using Command Palette**
1. Press `Ctrl+Shift+P` (Windows) or `Cmd+Shift+P` (Mac)
2. Type: `Python: Select Interpreter`
3. Press Enter
4. Choose the one in your virtual environment:
   - Look for: `.\myenv\Scripts\python.exe` or `myenv\Scripts\python.exe`
   - It should show `('.venv': venv)` or similar

**Method 2: Using Status Bar**
1. Look at the bottom-right of VS Code
2. You'll see the Python version (like "Python 3.11.0")
3. Click it
4. Select your virtual environment's Python

**Method 3: When Opening a Project**
1. Open your Django project folder in VS Code
2. VS Code will ask: "Select a Python interpreter"
3. Choose your virtual environment's Python

**How to Verify:**
- Look at the bottom-right corner
- You should see: `Python 3.x.x ('myenv': venv)`
- This means VS Code is using your virtual environment!

#### Step 4: Open Your Django Project in VS Code

**Method 1: From VS Code**
1. Click **File** → **Open Folder**
2. Navigate to your Django project folder
3. Click **Select Folder**

**Method 2: From Command Line**
```powershell
# Navigate to your project
cd C:\Users\dell\Desktop\Django\myfirstproject

# Open in VS Code
code .
```

**Method 3: From File Explorer**
1. Navigate to your project folder
2. Right-click the folder
3. Select **"Open with Code"**

#### Step 5: Using VS Code Integrated Terminal

**What is Integrated Terminal?**
VS Code has a terminal built-in, so you don't need to switch between windows!

**How to Open Terminal:**

1. **Using Menu:**
   - Click **Terminal** → **New Terminal**
   - Or press `Ctrl+` ` (backtick key, usually above Tab)

2. **Using Keyboard Shortcut:**
   - `Ctrl+Shift+` ` (backtick)
   - Or `Ctrl+J` (opens terminal panel)

**Terminal Features:**
- ✅ Multiple terminals (click `+` to add more)
- ✅ Split terminals (right-click → Split)
- ✅ Terminal selection dropdown
- ✅ Automatic activation of virtual environment (if configured)

**Using Terminal in VS Code:**
```powershell
# Terminal opens in your project folder automatically
# You can run Django commands directly:

python manage.py runserver
python manage.py makemigrations
python manage.py migrate
```

#### Step 6: VS Code Settings for Django

**Create Workspace Settings:**

1. Press `Ctrl+Shift+P`
2. Type: `Preferences: Open Workspace Settings (JSON)`
3. Add these settings:

```json
{
    "python.defaultInterpreterPath": "${workspaceFolder}/myenv/Scripts/python.exe",
    "python.terminal.activateEnvironment": true,
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": false,
    "python.linting.flake8Enabled": true,
    "python.formatting.provider": "black",
    "editor.formatOnSave": true,
    "files.autoSave": "afterDelay",
    "files.autoSaveDelay": 1000,
    "[python]": {
        "editor.defaultFormatter": "ms-python.black-formatter",
        "editor.tabSize": 4
    },
    "[html]": {
        "editor.tabSize": 2
    },
    "[css]": {
        "editor.tabSize": 2
    }
}
```

**What these settings do:**
- **`python.defaultInterpreterPath`** - Use virtual environment Python
- **`python.terminal.activateEnvironment`** - Auto-activate venv in terminal
- **`python.linting.enabled`** - Show code errors
- **`editor.formatOnSave`** - Format code when you save
- **`files.autoSave`** - Save files automatically

#### Step 7: Useful VS Code Keyboard Shortcuts

**Essential Shortcuts for Django Development:**

| Action | Windows/Linux | Mac |
|--------|---------------|-----|
| Open Command Palette | `Ctrl+Shift+P` | `Cmd+Shift+P` |
| Open Terminal | `Ctrl+` ` | `Ctrl+` ` |
| Save File | `Ctrl+S` | `Cmd+S` |
| Save All | `Ctrl+K S` | `Cmd+K S` |
| Find in File | `Ctrl+F` | `Cmd+F` |
| Find in All Files | `Ctrl+Shift+F` | `Cmd+Shift+F` |
| Go to Line | `Ctrl+G` | `Cmd+G` |
| Go to Definition | `F12` | `F12` |
| Show References | `Shift+F12` | `Shift+F12` |
| Rename Symbol | `F2` | `F2` |
| Format Document | `Shift+Alt+F` | `Shift+Option+F` |
| Comment Line | `Ctrl+/` | `Cmd+/` |
| Duplicate Line | `Shift+Alt+Down` | `Shift+Option+Down` |
| Move Line Up/Down | `Alt+Up/Down` | `Option+Up/Down` |
| Multi-cursor | `Alt+Click` | `Option+Click` |
| Close Tab | `Ctrl+W` | `Cmd+W` |
| Reopen Closed Tab | `Ctrl+Shift+T` | `Cmd+Shift+T` |

**Django-Specific Tips:**
- Use `Ctrl+P` to quickly open files
- Use `Ctrl+Shift+O` to navigate symbols in current file
- Use `Ctrl+T` to search across all files

#### Step 8: VS Code Features for Django

**1. IntelliSense (Code Completion)**
- VS Code suggests code as you type
- Press `Ctrl+Space` to trigger manually
- Shows function parameters, documentation

**2. Go to Definition**
- Right-click on any function/class
- Select "Go to Definition" or press `F12`
- Jumps to where it's defined

**3. Peek Definition**
- Right-click → "Peek Definition" or `Alt+F12`
- Shows definition without leaving current file

**4. Find All References**
- Right-click → "Find All References" or `Shift+F12`
- Shows everywhere a function/class is used

**5. Code Formatting**
- Right-click → "Format Document" or `Shift+Alt+F`
- Automatically formats your code

**6. Integrated Debugging**
- Set breakpoints by clicking left of line numbers
- Press `F5` to start debugging
- Step through code line by line

**7. Git Integration**
- See file changes in Source Control panel (left sidebar)
- Commit and push directly from VS Code
- Visual diff viewer

#### Step 9: Creating VS Code Tasks for Django

**What are Tasks?**
Tasks let you run commands with keyboard shortcuts.

**Create Django Tasks:**

1. Press `Ctrl+Shift+P`
2. Type: `Tasks: Configure Task`
3. Select "Create tasks.json file from template"
4. Choose "Others"
5. Replace with:

```json
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Django: Run Server",
            "type": "shell",
            "command": "python manage.py runserver",
            "group": {
                "kind": "build",
                "isDefault": true
            },
            "presentation": {
                "reveal": "always",
                "panel": "new"
            }
        },
        {
            "label": "Django: Make Migrations",
            "type": "shell",
            "command": "python manage.py makemigrations",
            "group": "build"
        },
        {
            "label": "Django: Migrate",
            "type": "shell",
            "command": "python manage.py migrate",
            "group": "build"
        }
    ]
}
```

**How to Run Tasks:**
- Press `Ctrl+Shift+P`
- Type: `Tasks: Run Task`
- Select the task you want

**Or use keyboard shortcut:**
- `Ctrl+Shift+B` runs the default task (Run Server)

### VS Code Workspace for Django Project

**Recommended Folder Structure in VS Code:**

```
myfirstproject/          ← Root folder (open this in VS Code)
├── .vscode/             ← VS Code settings (auto-created)
│   └── settings.json
├── myfirstproject/      ← Django project folder
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── blog/                ← Your app
│   ├── models.py
│   ├── views.py
│   └── ...
├── manage.py
└── db.sqlite3
```

**Best Practices:**
1. ✅ Always open the project root folder (where `manage.py` is)
2. ✅ Use the integrated terminal for Django commands
3. ✅ Keep virtual environment activated
4. ✅ Use Git for version control (VS Code has built-in Git)
5. ✅ Install recommended extensions
6. ✅ Configure Python interpreter correctly

### Troubleshooting VS Code Issues

**Problem: "Python extension not working"**
- Solution: Reload VS Code (`Ctrl+Shift+P` → "Reload Window")
- Make sure Python is installed correctly

**Problem: "Terminal not activating virtual environment"**
- Solution: Check `python.terminal.activateEnvironment` setting
- Manually activate: `.\myenv\Scripts\Activate.ps1`

**Problem: "IntelliSense not working"**
- Solution: Select correct Python interpreter
- Reload VS Code window

**Problem: "Can't find Django commands"**
- Solution: Make sure virtual environment is activated
- Check Django is installed: `pip list | findstr django`

### Quick VS Code Setup Checklist

Before starting Django development, make sure:

- [ ] VS Code is installed
- [ ] Python extension is installed
- [ ] Django extension is installed (optional)
- [ ] Virtual environment is created
- [ ] Python interpreter is selected (virtual environment)
- [ ] Project folder is open in VS Code
- [ ] Integrated terminal is working
- [ ] Can run `python manage.py --version` in terminal

---

## 🛠️ Part 6: Understanding Django Commands

### What are Django Commands?

Django commands are special instructions you give to Django to do things like:
- Create a project
- Start a server
- Create database tables
- And much more!

### Two Main Ways to Run Django Commands

#### 1. `django-admin` - The Global Command

**What it is:**
A command-line tool that comes with Django.

**Where to use it:**
- Works from anywhere (if Django is installed)
- Usually used to create new projects

**Example:**
```bash
django-admin startproject myproject
```

**Breaking it down:**
- `django-admin` = The command tool
- `startproject` = "Create a new project"
- `myproject` = The name of your project

#### 2. `manage.py` - The Project Command

**What it is:**
A special file in each Django project that runs commands for that specific project.

**Where to use it:**
- Only works inside a Django project folder
- Used for project-specific tasks

**Example:**
```bash
python manage.py runserver
```

**Breaking it down:**
- `python` = Run Python
- `manage.py` = The management file
- `runserver` = "Start the development server"

### Common Django Commands

Here are some commands you'll use often:

#### Creating a Project
```bash
django-admin startproject myproject
```
**What it does:** Creates a new Django project called "myproject"

#### Creating an App
```bash
python manage.py startapp myapp
```
**What it does:** Creates a new app (a part of your project) called "myapp"

#### Running the Server
```bash
python manage.py runserver
```
**What it does:** Starts a web server so you can see your website

#### Creating Database Tables
```bash
python manage.py migrate
```
**What it does:** Creates database tables based on your models

#### Creating a Superuser (Admin)
```bash
python manage.py createsuperuser
```
**What it does:** Creates an admin user so you can access the admin panel

### Understanding Command Structure

**General format:**
```bash
[command] [action] [options]
```

**Example:**
```bash
python manage.py runserver 8000
```

**Breaking it down:**
- `python manage.py` = The command tool
- `runserver` = The action (what to do)
- `8000` = Option (which port to use)

---

## ✅ Checklist: Environment Setup Complete

Before moving to Step 3, make sure you can:

- [ ] Check Python version: `python --version`
- [ ] Check pip version: `pip --version`
- [ ] Create a virtual environment: `python -m venv myenv`
- [ ] Activate virtual environment: `.\myenv\Scripts\Activate.ps1` (Windows) or `source myenv/bin/activate` (Mac/Linux)
- [ ] Install Django: `pip install django`
- [ ] Check Django version: `django-admin --version`
- [ ] Open VS Code and install Python extension
- [ ] Understand the difference between `django-admin` and `manage.py`

---

## 🐛 Troubleshooting Common Problems

### Problem: "python is not recognized"

**Solution:**
- Python is not installed or not in PATH
- Reinstall Python and check "Add Python to PATH"
- Or use `py` instead of `python` on Windows

### Problem: "pip is not recognized"

**Solution:**
- Try `python -m pip` instead of just `pip`
- Or `python3 -m pip` on Mac/Linux

### Problem: "django-admin is not recognized"

**Solution:**
- Make sure virtual environment is activated
- Make sure Django is installed: `pip install django`
- Try `python -m django` instead

### Problem: "Cannot activate virtual environment"

**Solution (Windows PowerShell):**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**Solution (Windows CMD):**
- Use Command Prompt instead of PowerShell
- Or use: `myenv\Scripts\activate.bat`

---

## 🎓 Key Concepts Summary

1. **Python** = Programming language Django is written in
2. **pip** = Tool to install Python packages
3. **Virtual Environment** = Isolated workspace for each project
4. **Django Installation** = Putting Django in your virtual environment
5. **django-admin** = Global Django command tool
6. **manage.py** = Project-specific Django command tool

---

## 🚀 Ready for Step 3?

Excellent! Your environment is set up and ready. 

Next, you'll create your first Django project! Go to [Step 3: Your First Django Project](./step-3-first-django-project.md)

---

## 💡 Pro Tips

1. **Always activate your virtual environment** before working on Django projects
2. **Keep your virtual environment activated** while working
3. **Use `deactivate`** when you're done working
4. **One virtual environment per project** is a good practice
5. **Update Django regularly**: `pip install --upgrade django`

