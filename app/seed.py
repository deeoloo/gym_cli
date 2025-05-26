import click
from datetime import datetime

from app.models import Member, Workout, Exercise
from app.models.base import init_db
from app.menus import main_menu, member_menu, workout_menu, exercise_menu


def handle_member_actions(choice):
    if choice == "1":
        name = click.prompt("Member name")
        email = click.prompt("Email")
        try:
            member = Member.create(name=name, email=email)
            click.echo(f"Added member: {member.name}")
        except Exception as e:
            click.echo(f"Error: {str(e)}")

    elif choice == "2":
        members = Member.get_all()
        for member in members:
            click.echo(f"{member.id}: {member.name} - Member for {member.membership_duration} days")

    elif choice == "3":
        member_id = click.prompt("Member ID", type=int)
        member = Member.find_by_id(member_id)
        if member:
            click.echo(f"\nMember: {member.name}")
            click.echo(f"Email: {member.email}")
            click.echo(f"Member since: {member.join_date}")
            workouts = Workout.get_by_member(member.id)
            click.echo(f"\nWorkouts ({len(workouts)}):")
            for workout in workouts:
                click.echo(f"- {workout.workout_type} ({workout.duration} mins)")
        else:
            click.echo("Member not found!")

    click.pause()


def handle_workout_actions(choice):
    if choice == "1":
        member_id = click.prompt("Member ID", type=int)
        duration = click.prompt("Duration (minutes)", type=int)
        workout_type = click.prompt("Workout type")
        try:
            workout = Workout.create(member_id, duration, workout_type)
            click.echo(f"Recorded {workout.workout_type} workout")
        except Exception as e:
            click.echo(f"Error: {str(e)}")

    elif choice == "2":
        member_id = click.prompt("Member ID", type=int)
        workouts = Workout.get_by_member(member_id)
        for workout in workouts:
            click.echo(f"{workout.date}: {workout.workout_type} - {workout.duration} mins")

    click.pause()


def handle_exercise_actions(choice):
    if choice == "1":
        workout_id = click.prompt("Workout ID", type=int)
        name = click.prompt("Exercise name")
        sets = click.prompt("Number of sets", type=int)
        reps = click.prompt("Reps per set", type=int)
        weight = click.prompt("Weight (lbs)", type=int)
        try:
            exercise = Exercise.create(workout_id, name, sets, reps, weight)
            click.echo(f"Added {exercise.name} (Volume: {exercise.volume} lbs)")
        except Exception as e:
            click.echo(f"Error: {str(e)}")

    elif choice == "2":
        workout_id = click.prompt("Workout ID", type=int)
        # TODO: Implement exercise viewing logic

    click.pause()


def run_app():
    while True:
        choice = main_menu()

        if choice == "1":
            while True:
                sub = member_menu()
                if sub == "4":
                    break
                handle_member_actions(sub)

        elif choice == "2":
            while True:
                sub = workout_menu()
                if sub == "3":
                    break
                handle_workout_actions(sub)

        elif choice == "3":
            while True:
                sub = exercise_menu()
                if sub == "3":
                    break
                handle_exercise_actions(sub)

        elif choice == "4":
            click.echo("Goodbye! 👋")
            break

        else:
            click.echo("Invalid choice.")
            click.pause()


if __name__ == "__main__":
    print("Initializing DB...")
    init_db()
    print("Database initialized successfully.\n")

    run_app()
