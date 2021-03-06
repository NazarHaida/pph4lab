from sqlalchemy import Column, Boolean, Integer, String, DateTime, ForeignKey

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+mysqlconnector://root:MyZno26112003@localhost:3306/lab8dtbs", echo=True)

Base = declarative_base()
metadata = Base.metadata

class User(Base):
    __tablename__ = 'user'
    idUser = Column(Integer, primary_key=True)
    name = Column(String(45))
    surname = Column(String(45))
    username = Column(String(45))
    password = Column(String(200))

    def __repr__(self):
        return f"{self.idUser}, {self.name}, {self.surname}, {self.username}, {self.password}"

class Reservation(Base):
    __tablename__ = 'reservation'
    idReservation = Column(Integer, primary_key=True)
    title = Column(String(45))
    from_date = Column(DateTime)
    to_date = Column(DateTime)
    User_idUser = Column(Integer, ForeignKey('user.idUser'))
    Audience_idAudience = Column(Integer, ForeignKey('audience.idAudience'))

    user = relationship("User")
    audience = relationship("Audience")

    def __repr__(self):
        return f"{self.idReservation}, {self.title}, {self.date}, {self.User_idUser}, {self.Audience_idAudience}"

class Audience(Base):
    __tablename__ = "audience"
    idAudience = Column(Integer, primary_key=True)
    number = Column(Integer)
    amount_of_places = Column(Integer)
    status = Column(Boolean)


    def __repr__(self):
        return f"{self.idAudience}, {self.number}, {self.amount_of_places}, {self.status}, {self.reservation_date}"




# Base.metadata.create_all(engine)
