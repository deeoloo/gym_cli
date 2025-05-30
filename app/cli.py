import os
from app.menus import main_menu, member_menu, workout_menu, exercise_menu
from app.actions import handle_member_actions, handle_workout_actions, handle_exercise_actions

def setup():
    """Initialize the database (run this first)"""
    print("✅ Database created successfully!")

def start():
    """Start the interactive gym management system"""
    while True:
        choice = main_menu()
        
        # Member management
        if choice == "1":
            while True:
                member_choice = member_menu()
                if member_choice == "4":  # Back to main menu
                    break
                handle_member_actions(member_choice)
        
        # Workout management
        elif choice == "2":
            while True:
                workout_choice = workout_menu()
                if workout_choice == "3":  # Back to main menu
                    break
                handle_workout_actions(workout_choice)
        
        # Exercise management
        elif choice == "3":
            while True:
                exercise_choice = exercise_menu()
                if exercise_choice == "3":  # Back to main menu
                    break
                handle_exercise_actions(exercise_choice)
        
        # Exit
        elif choice == "4":
            print("\nGoodbye! 👋")
            break

if __name__ == '__main__':
    start()
