from app.menus import main_menu, member_menu, workout_menu, exercise_menu, system_menu
from app.actions import (
    handle_member_actions,
    handle_workout_actions,
    handle_exercise_actions,
    handle_system_actions
)
from app.ui import GymUI, console


def setup():
    """Initialize the database (run this first)"""
    print("✅ Database created successfully!")


def start():
    """Start the Gym CLI system (staff interface)"""
    while True:
        choice = main_menu()

        # Member Management
        if choice == "1":
            while True:
                member_choice = member_menu()
                if member_choice == "5":
                    break
                handle_member_actions(member_choice)

        # Workout Management
        elif choice == "2":
            while True:
                workout_choice = workout_menu()
                if workout_choice == "3":
                    break
                handle_workout_actions(workout_choice)

        # Exercise Management
        elif choice == "3":
            while True:
                exercise_choice = exercise_menu()
                if exercise_choice == "3":
                    break
                handle_exercise_actions(exercise_choice)

        # System Tools
        elif choice == "4":
            while True:
                system_choice = system_menu()
                if system_choice == "3":
                    break
                handle_system_actions(system_choice)

        # Exit
        elif choice == "5":
            console.print("\n[bold]Goodbye! 👋[/bold]")
            break


if __name__ == "__main__":
    start()
