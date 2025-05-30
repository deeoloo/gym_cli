import os
from app.actions import delete_all_rows

#delete_all_rows()

# menus.py
from app.ui import GymUI

def main_menu():
    return GymUI.show_menu(
        "GYM MANAGEMENT SYSTEM",
        {
            "[1]": "Member Management",
            "[2]": "Workout Management",
            "[3]": "Exercise Management",
            "[4]": "Exit"
        }
    )

def member_menu():
    return GymUI.show_menu(
        "MEMBER MANAGEMENT",
        {
            "[1]": "Add Member",
            "[2]": "List Members",
            "[3]": "View Member Details",
            "[4]": "Back to Main Menu"
        }
    )

def workout_menu():
    return GymUI.show_menu(
        "WORKOUT MANAGEMENT",
        {
            "[1]": "Record Workout",
            "[2]": "View Member Workouts",
            "[3]": "Back to Main Menu"
        }
    )

def exercise_menu():
    return GymUI.show_menu(
        "EXERCISE MANAGEMENT",
        {
            "[1]": "Add Exercise to Workout",
            "[2]": "View Workout Exercises",
            "[3]": "Back to Main Menu"
        }
    )