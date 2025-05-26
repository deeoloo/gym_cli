import click

def main_menu():
    click.clear()
    click.echo("\nGym Management System")
    click.echo("1. Member Management")
    click.echo("2. Workout Management")
    click.echo("3. Exercise Management")
    click.echo("4. Exit")
    return click.prompt("Choose an option:", type=str)

def member_menu():
    click.clear()
    click.echo("\nMember Management")
    click.echo("1. Add Member")
    click.echo("2. List Members")
    click.echo("3. View Member Details")
    click.echo("4. Back to Main Menu")
    return click.prompt("Choose an option:", type=str)

def workout_menu():
    click.clear()
    click.echo("\nWorkout Management")
    click.echo("1. Record Workout")
    click.echo("2. View Member Workouts")
    click.echo("3. Back to Main Menu")
    return click.prompt("Choose an option:", type=str)

def exercise_menu():
    click.clear()
    click.echo("\nExercise Management")
    click.echo("1. Add Exercise to Workout")
    click.echo("2. View Workout Exercises")
    click.echo("3. Back to Main Menu")
    return click.prompt("Choose an option:", type=str)