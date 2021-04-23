from models.city import City
from models.user import User
from models.country import Country


import repositories.user_repository as user_repository


# user_repository.delete_all()

user1 = User('Lina', 'Edinburgh', 'Scotland')
user_repository.save(user1)

user2 = User('Oscar Wilde', 'Dublin', 'Ireland')
user_repository.save(user2)

user3 = User('Peter Parker', 'New York', 'USA')
user_repository.save(user3)



