from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import *


session = sessionmaker(bind=engine)

add_user = User(idUser=1, name="Augustin", surname="Porebryk", username="billy12v", password="32133234")
add_user2 = User(idUser=2, name="Vasyl", surname="Vasyliev", username="fullmaster", password="23415672")

add_audience = Audience(idAudience=1, number=212, amount_of_places=10, status=1, reservation_date='2021-08-30')
add_audience2 = Audience(idAudience=2, number=213, amount_of_places=10, status=1, reservation_date='2021-09-01')

add_reservation = Reservation(idReservation=1, title="SAPR Project Review", date='2021-10-28', User_idUser=1, Audience_idAudience=1)
add_reservation2 = Reservation(idReservation=2, title="AIS Project Review", date='2021-10-26', User_idUser=2, Audience_idAudience=2)

ss = session()

ss.add(add_user)
ss.add(add_user2)
ss.add(add_audience)
ss.add(add_audience2)
ss.add(add_reservation)
ss.add(add_reservation2)



ss.commit()