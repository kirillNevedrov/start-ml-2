from sqlalchemy import func, desc, Column, Integer, String

from database import Base, SessionLocal

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    age = Column(Integer)
    city = Column(String)
    country = Column(String)
    exp_group = Column(Integer)
    gender = Column(Integer)
    os = Column(String)
    source = Column(String)

if __name__ == "__main__":
    session = SessionLocal()
    users_count = func.count(User.id)
    results = (
        session.query(User.country, User.os, users_count)
        .filter(User.exp_group == 3)
        .group_by(User.country, User.os)
        .having(users_count > 100)
        .order_by(desc(users_count))
        .all()
    )
    print(results)