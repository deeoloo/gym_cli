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
        import re
        session = Session()
        try:
            clean_email = email.strip().lower()
        
       
            if not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", clean_email):
                raise ValueError("Invalid email format.")

        
            existing = session.query(cls).filter(cls.email.ilike(clean_email)).first()
            if existing:
                raise ValueError("Email already exists. Please use a different email")

            member = cls(name=name.strip(), email=clean_email)
            session.add(member)
            session.commit()
            return {"id": member.id, "name": member.name, "email": member.email}
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
    
    @classmethod
    def get_all(cls):
        session = Session()
        members = session.query(cls).all()
    # Force-load attributes before closing session
        for m in members:
            _ = m.name, m.email, m.join_date  # Preloads all needed attributes
        session.close()
        return members
    
    @classmethod
    def find_by_id(cls, member_id):
        session = Session()
        member = session.query(cls).get(member_id)
        session.close()
        return member
    
    @classmethod
    def find_by_name(cls, name):
        session = Session()
        try:
            return session.query(cls).filter(cls.name.ilike(f"%{name.strip()}%")).all()
        finally:
            session.close()

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

