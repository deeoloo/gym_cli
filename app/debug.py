# app/debug.py
from sqlalchemy import inspect
from models import Base, Member, Workout, Exercise, Session, engine
from datetime import datetime

def print_database_schema():
    """Print all tables and their columns"""
    inspector = inspect(engine)
    print("\nDatabase Schema:")
    for table_name in inspector.get_table_names():
        print(f"\nTable: {table_name}")
        for column in inspector.get_columns(table_name):
            print(f"- {column['name']}: {column['type']}")

def print_all_data():
    """Print all records from all tables"""
    session = Session()
    
    print("\nMembers:")
    members = session.query(Member).all()
    for member in members:
        print(f"\nID: {member.id} | Name: {member.name} | Email: {member.email}")
        print(f"Workouts ({len(member.workouts)}):")
        for workout in member.workouts:
            print(f"  - {workout.date}: {workout.workout_type} ({workout.duration} mins)")
            for exercise in workout.exercises:
                print(f"    * {exercise.name}: {exercise.sets}x{exercise.reps} @ {exercise.weight}lbs")

    session.close()

def test_relationships():
    """Verify relationship functionality"""
    session = Session()
    
    # Create test data
    test_member = Member(name="Debug User", email="debug@test.com")
    session.add(test_member)
    session.commit()
    
    test_workout = Workout(
        member_id=test_member.id,
        duration=30,
        workout_type="DEBUG",
        date=datetime.now().date()
    )
    session.add(test_workout)
    
    test_exercise = Exercise(
        workout_id=test_workout.id,
        name="Debug Press",
        sets=3,
        reps=10,
        weight=135
    )
    session.add(test_exercise)
    session.commit()
    
    # Verify relationships
    member = session.query(Member).get(test_member.id)
    print("\nRelationship Test Results:")
    print(f"Member has {len(member.workouts)} workouts")
    print(f"First workout has {len(member.workouts[0].exercises)} exercises")
    
    # Cleanup
    session.delete(test_member)
    session.commit()
    session.close()

def check_database_connection():
    """Verify database connectivity"""
    try:
        conn = engine.connect()
        conn.close()
        print("✅ Database connection successful")
        return True
    except Exception as e:
        print(f"❌ Database connection failed: {str(e)}")
        return False

if __name__ == "__main__":
    print("=== Running Database Diagnostics ===")
    check_database_connection()
    print_database_schema()
    test_relationships()
    print_all_data()