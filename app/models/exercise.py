from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import  relationship
from datetime import datetime
from .base import Base, Session


class Exercise(Base):
    __tablename__ = 'exercises'

    id = Column(Integer, primary_key= True)
    workout_id= Column(Integer, ForeignKey('workouts.id'))
    name = Column(String)
    sets = Column(Integer)
    reps = Column(Integer)
    weight = Column(Integer)

    workout= relationship("Workout", back_populates= "exercises")
    

    @classmethod
    def create(cls, name, workout_id, sets, reps, weight):
        session = Session()
        try:
            exercise = cls(name=name,
                           workout_id= workout_id,
                           sets= sets,
                           reps= reps,
                           weight= weight)
            session.add(exercise)
            session.commit()
            return {"id": exercise.id, "name": exercise.name,"workout_id": exercise.workout_id, "sets":exercise.sets,"reps": exercise.reps, "weight":exercise.weight}
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    @classmethod
    def get_by_workout(cls,workout_id):
        from app.models.base import Session
        session = Session()
        return session.query(cls).filter_by(workout_id=workout_id).all()
    
    @property
    def volume(self):
        return self.sets * self.reps * self.weight
    ...