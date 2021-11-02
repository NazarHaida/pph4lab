from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import *


session = sessionmaker(bind=engine)

add_user = User(idUser=1, name="Augustin", surname="Porebryk", username="billy12v", password="32133234")
add_user2 = User(idUser=2, name="Vasyl", surname="Vasyliev", username="fullmaster", password="23415672")

add_audience = Audience(idAudience=1, number=212, amount_of_places=10, status=1)
add_audience2 = Audience(idAudience=2, number=213, amount_of_places=10, status=1)

add_reservation = Reservation(idReservation=1, title="SAPR Project Review", start_of_reservation='2021-10-28', end_of_reservation='2021-11-03',User_idUser=1, Audience_idAudience=1)
add_reservation2 = Reservation(idReservation=2, title="AIS Project Review", start_of_reservation='2021-10-26', end_of_reservation='2021-11-01', User_idUser=2, Audience_idAudience=2)
add_reservation3 = Reservation(idReservation=3, title="AIS Project", start_of_reservation='2021-12-30', end_of_reservation='2021-12-01', User_idUser=2, Audience_idAudience=1)
ss = session()

ss.add(add_user)
ss.add(add_user2)
ss.add(add_audience)
ss.add(add_audience2)
ss.add(add_reservation)
ss.add(add_reservation2)
ss.add(add_reservation3)


ss.commit()