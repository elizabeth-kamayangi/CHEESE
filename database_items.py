from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base,Restaurant,MenuItem
engine=create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind=engine
DBsession=sessionmaker(bind=engine)
session=DBsession()
myFirstRestaurant=Restaurant(name='PizzaPalace')
session.add(myFirstRestaurant)
session.commit()
session.query(Restaurant).all()
cheesepizza=MenuItem(name='cheesepizza',description='made with all natural ingredients',course='Entree',price='$8.99',
restaurant=myFirstRestaurant)
session.add(cheesepizza)
session.commit()
session.query(MenuItem).all()
veggieBurgers=session.query(MenuItem).filter_by(name='Veggie Burger')
for veggieBurger in veggieBurgers:
    print (veggieBurger.id)
    print (veggieBurger.price)
    print (veggieBurger.restaurant.name)
    print ("\:n")
UrbanveggieBurger=session.query(MenuItem).filter_by(id=10).one()
print (UrbanveggieBurger.price)
UrbanveggieBurger.price='$2.99'
session.add(UrbanveggieBurger)
session.commit
veggieBurgers=session.query(MenuItem).filter_by(name='Veggie Burger')
for veggieBurger in veggieBurgers:
    print(veggieBurger.id)
    print(veggieBurger.price)
    print(veggieBurger.restaurant.name)
    print("\:n")








