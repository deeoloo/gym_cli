import click
from .models.member import Member
from .models.workout import Workout
from .models.exercise import Exercise
from .menus import main_menu, member_menu, workout_menu, exercise_menu
from .actions import handle_member_actions, handle_workout_actions, handle_exercise_actions

@click.group()
def cli():
    """Gym Management System CLI"""
    pass

@cli.command()
def start():
    """Start the interactive CLI"""
    while True:
        choice = main_menu()
        
        if choice == "1":  # Members
            member_choice = member_menu()
            handle_member_actions(member_choice)
        
        elif choice == "2":  # Workouts
            workout_choice = workout_menu()
            handle_workout_actions(workout_choice)
        
        elif choice == "3":  # Exercises
            exercise_choice = exercise_menu()
            handle_exercise_actions(exercise_choice)
        
        elif choice == "4":  # Exit
            click.echo("Goodbye!")
            break

if __name__ == '__main__':
    cli()