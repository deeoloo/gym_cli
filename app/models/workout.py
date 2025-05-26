from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import  relationship
from datetime import datetime
from .base import Base, Session


class Workout(Base):
    __tablename__ = 'workouts'


    id = Column(Integer, primary_key= True)
    member_id= Column(Integer, ForeignKey('members.id'))
    duration = Column(Integer)
    date = Column(Date, default= datetime.now().date())
    workout_type= Column(String)

    member= relationship("Member", back_populates= "workouts")
    exercises = relationship("Exercise", back_populates="workout")

    @classmethod
    def create(cls, member_id, duration, workout_type):
        session = Session()
        try:
            workout = cls(member_id= member_id,
                          duration= duration,
                           workout_type= workout_type)
            session.add(workout)
            session.commit()
            return workout
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
    
    @classmethod
    def get_by_member(cls, member_id):
        from app.models.base import Session
        session = Session()
        return session.query(cls).filter_by(member_id=member_id).all()

    
    @property
    def calories_burned(self):
        return self.duration * 5
    ...