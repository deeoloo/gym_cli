from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import  relationship
from datetime import datetime
from .base import Base, Session


class Member(Base):
    __tablename__ = 'members'

    id = Column(Integer, primary_key= True)
    name = Column(String, nullable= False)
    email = Column(String, unique=  True)
    join_date = Column(DateTime, default=datetime.utcnow)
    workouts= relationship("Workout", back_populates= "member")

    @classmethod
    def create(cls, name, email):
        session = Session()
        try:
            member = cls(name=name, 
                         email=email,
                         join_date= join_date or datetime.utcnow())
            session.add(member)
            session.commit()
            return member
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
    
    @classmethod
    def get_all(cls):
        session = Session()
        members = session.query(cls).all()
        session.close()
        return members
    
    @classmethod
    def find_by_id(cls, member_id):
        session = Session()
        member = session.query(cls).get(member_id)
        session.close()
        return member
    
    # In member.py
    @classmethod
    def update_email(cls, member_id, new_email):
        session = Session()
        member = session.query(cls).get(member_id)
        member.email = new_email
        session.commit()

    @classmethod
    def delete(cls, member_id):
        session = Session()
        member = session.query(cls).get(member_id)
        session.delete(member)
        session.commit()
    
    @property
    def membership_duration(self):
        if self.join_date:
            return (datetime.now().date() - self.join_date.date()).days
        return 0
   
    ...

