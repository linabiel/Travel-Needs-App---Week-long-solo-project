from models.city import City
from models.user import User
from models.country import Country

from repositories import user_repository, country_repository, city_repository

user_repository.delete_all()
city_repository.delete_all()
country_repository.delete_all()

user1 = User('Lina', 'Edinburgh', 'Scotland')
user_repository.save(user1)

user2 = User('Oscar Wilde', 'Dublin', 'Ireland')
user_repository.save(user2)

user3 = User('Peter Parker', 'New York', 'USA')
user_repository.save(user3)


city1 = City('Berlin')
city_repository.save(city1)

city2 = City('Paris')
city_repository.save(city2)

city3 = City('Buenos Aires')
city_repository.save(city3)

country1 = Country('Germany')
country_repository.save(country1)

country2 = Country('France')
country_repository.save(country2)

country3 = Country('Argentina')
country_repository.save(country3)