

```
# 🏋️‍♂️ Gym Management System (CLI-Based)

The **Gym Management System** is a proposed terminal-based application designed to help gym staff efficiently manage member records, workouts, and exercises through a structured command-line interface. The system will be built using Python, leveraging SQLAlchemy ORM for database operations and Rich for an enhanced CLI experience.

---

## 📌 Purpose

This system aims to digitize and simplify gym operations by offering a reliable and interactive way to manage gym members, track their workouts, and monitor individual exercise sessions. It will help gym staff focus more on fitness coaching by reducing the administrative burden.

---

## 🔧 Key Features

### 🎯 Member Management
- Add new gym members with name and email.
- View all members and membership durations.
- Search members by name or ID.
- Delete members from the system.

### 💪 Workout Tracking
- Record workouts for specific members.
- View all workouts associated with a member.

### 🏋️ Exercise Logging
- Add exercises to a specific workout session.
- View all exercises under a workout, including volume calculation.

### 📊 System Tools
- View system-wide statistics:
  - Total members
  - Total workouts
  - Average workouts per member
- Option to delete all data (reset functionality)

---

## 🛠️ Technology Stack

- **Python 3.8+**
- **SQLAlchemy** – ORM for database management
- **Rich** – Library for beautiful CLI rendering
- **SQLite** – Lightweight relational database
- **Virtual Environment** – `venv` or `pipenv` supported

---

## 🗂️ Project Structure

```

gym\_cli/
├── app/
│   ├── cli.py              # Main program entry point
│   ├── actions.py          # Business logic handlers
│   ├── menus.py            # CLI menu structure
│   ├── ui.py               # UI rendering and input helpers
│   ├── models/
│   │   ├── base.py         # Database session setup
│   │   ├── member.py       # Member model
│   │   ├── workout.py      # Workout model
│   │   └── exercise.py     # Exercise model
├── Pipfile / requirements.txt
└── README.md

````

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/gym_cli.git
cd gym_cli
````

### 2️⃣ Create a Virtual Environment

#### Option A: Using `venv`

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

#### Option B: Using `pipenv`

```bash
pipenv install
pipenv shell
```

### 3️⃣ Run the Application

```bash
python -m app.cli
```

---

## ✅ ORM Overview

The database models will include:

* `Member`: One-to-many relationship with `Workout`
* `Workout`: One-to-many relationship with `Exercise`
* `Exercise`: Contains logic to compute total volume

Each model will implement:

* `create()`
* `get_all()`
* `find_by_id()`
* `delete()`

---

## 🧪 Example CLI Menu

```
GYM MANAGEMENT SYSTEM

[1] Member Management
[2] Workout Management
[3] Exercise Management
[4] System Tools
[5] Exit

Choose:
```

---

## 🧹 Development Tools

To reset the system (dev use only), a utility will be provided to delete all database rows.

---

## 📝 License

This project will be released under the **MIT License**.

---

## 💬 Feedback

If you’d like to suggest improvements or report issues, please open an issue or submit a pull request.

```
