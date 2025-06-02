from app.ui import GymUI

def main_menu():
    error = None
    while True:
        choice = GymUI.show_menu(
            "GYM MANAGEMENT SYSTEM",
            {
                "1": "Member Management",
                "2": "Workout Management",
                "3": "Exercise Management",
                "4": "System Tools",
                "5": "Exit"
            },
            error_message=error
        )
        if choice in ["1", "2", "3", "4", "5"]:
            return choice
        error = "Invalid. Please enter a valid choice."


def member_menu():
    error = None
    while True:
        choice = GymUI.show_menu(
            "MEMBER MANAGEMENT",
            {
                "1": "Add Member",
                "2": "List Members",
                "3": "View Member Details",
                "4": "Delete a Member",
                "5": "Back"
            },
            error_message=error
        )
        if choice in ["1", "2", "3", "4", "5"]:
            return choice
        error = "Invalid. Please enter a valid choice."


def workout_menu():
    error = None
    while True:
        choice = GymUI.show_menu(
            "WORKOUT MANAGEMENT",
            {
                "1": "Record Workout",
                "2": "View Member Workouts",
                "3": "Back"
            },
            error_message=error
        )
        if choice in ["1", "2", "3"]:
            return choice
        error = "Invalid. Please enter a valid choice."


def exercise_menu():
    error = None
    while True:
        choice = GymUI.show_menu(
            "EXERCISE MANAGEMENT",
            {
                "1": "Add Exercise to Workout",
                "2": "View Workout Exercises",
                "3": "Back"
            },
            error_message=error
        )
        if choice in ["1", "2", "3"]:
            return choice
        error = "Invalid. Please enter a valid choice."


def system_menu():
    error = None
    while True:
        choice = GymUI.show_menu(
            "SYSTEM TOOLS",
            {
                "1": "System Statistics",
                "2": "Delete All Data",
                "3": "Back"
            },
            error_message=error
        )
        if choice in ["1", "2", "3"]:
            return choice
        error = "Invalid. Please enter a valid choice."
