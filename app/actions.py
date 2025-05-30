# actions.py
from app.ui import GymUI
from app.models import Member, Workout, Exercise

def handle_member_actions(choice):
    if choice == "1":
        name = GymUI.get_input("Member name")
        email = GymUI.get_input("Email")
        try:
            data = Member.create(name=name, email=email)
            GymUI.show_message(f"Added member: {data['name']}", "success")
        except ValueError as ve:
            GymUI.show_message(f"Error: {ve}", "error")
        except Exception as e:
            GymUI.show_message("An unexpected error occurred", "error")
    
    elif choice == "2":
        members = Member.get_all()
        GymUI.show_table(
            data=[[m.id, m.name, f"{m.membership_duration} days"] for m in members],
            columns=["ID", "Name", "Membership Duration"]
        )
    
    elif choice == "3":
        query = GymUI.get_input("Enter Member ID or Name")

    try:
        if query.isdigit():
            member = Member.find_by_id(int(query))
            members = [member] if member else []
        else:
            members = Member.find_by_name(query)

        if not members:
            GymUI.show_message("Member not found!", "error")
        else:
            for member in members:
                GymUI.show_table(
                    data=[
                        ["Name", member.name],
                        ["Email", member.email],
                        ["Member Since", member.join_date]
                    ],
                    columns=["Property", "Value"]
                )
                workouts = Workout.get_by_member(member.id)
                if workouts:
                    GymUI.show_table(
                        data=[[w.date, w.workout_type, f"{w.duration} mins"] for w in workouts],
                        columns=["Date", "Type", "Duration"]
                    )

    except ValueError:
        GymUI.show_message("Invalid input", "error")

    GymUI.pause()


def handle_workout_actions(choice):
    if choice == "1":
        try:
            member_id = int(GymUI.get_input("Member ID"))
            duration = int(GymUI.get_input("Duration (minutes)"))
            workout_type = GymUI.get_input("Workout type")
            
            data = Workout.create(
                member_id=member_id,
                duration=duration,
                workout_type=workout_type
            )
            GymUI.show_message(
                f"Workout added for Member {data['member_id']} on {data['date']}",
                "success"
            )
        except Exception as e:
            GymUI.show_message(f"Error: {str(e)}", "error")
    
    elif choice == "2":
        try:
            member_id = int(GymUI.get_input("Member ID"))
            workouts = Workout.get_by_member(member_id)
            
            if workouts:
                GymUI.show_table(
                    ["Date", "Type", "Duration"],
                    [[w.date, w.workout_type, f"{w.duration} mins"] for w in workouts]
                )
            else:
                GymUI.show_message("No workouts found for this member", "info")
        except ValueError:
            GymUI.show_message("Invalid Member ID", "error")
    
    GymUI.pause()

def handle_exercise_actions(choice):
    if choice == "1":
        try:
            workout_id = int(GymUI.get_input("Workout ID"))
            name = GymUI.get_input("Exercise name")
            sets = int(GymUI.get_input("Number of sets"))
            reps = int(GymUI.get_input("Reps per set"))
            weight = int(GymUI.get_input("Weight (lbs)"))
            
            data = Exercise.create(
                workout_id=workout_id,
                name=name,
                sets=sets,
                reps=reps,
                weight=weight
            )
            GymUI.show_message(
                f"Added {data['name']} with {data['reps']} reps to Workout {data['workout_id']}",
                "success"
            )
        except Exception as e:
            GymUI.show_message(f"Error: {str(e)}", "error")
    
    elif choice == "2":
        try:
            workout_id = int(GymUI.get_input("Workout ID"))
            exercises = Exercise.get_by_workout(workout_id)
            
            if exercises:
                GymUI.show_table(
                    ["Exercise", "Sets", "Reps", "Weight", "Volume"],
                    [
                        [ex.name, ex.sets, ex.reps, f"{ex.weight} lbs", f"{ex.volume} lbs"]
                        for ex in exercises
                    ]
                )
            else:
                GymUI.show_message("No exercises found for this workout", "info")
        except ValueError:
            GymUI.show_message("Invalid Workout ID", "error")
    
    GymUI.pause()

def delete_all_rows():
    from app.models.base import Session
    session = Session()
    try:
        session.query(Exercise).delete()
        session.query(Workout).delete()
        session.query(Member).delete()
        session.commit()
        GymUI.show_message("✓ All rows deleted successfully", "success")
    except Exception as e:
        session.rollback()
        GymUI.show_message(f"✗ Error: {e}", "error")
    finally:
        session.close()