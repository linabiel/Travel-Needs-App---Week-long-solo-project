from db.run_sql import run_sql
from models.destination import Destination
from models.user import User
from models.country import Country
from models.city import City
from repositories import user_repository, city_repository, country_repository

def save(destination):
    sql = "INSERT INTO destinations (user_id, country_id, city_id) VALUES (%s, %s, %s) RETURNING id"
    values = [destination.user.id, destination.country.id, destination.city.id]
    results = run_sql(sql, values)
    destination.id = results[0]['id']
    return destination


def select_all():
    destinations = []
    sql = "SELECT * FROM destinations"
    results = run_sql(sql)

    for row in results:
        user = user_repository.select(row['user_id'])
        country = country_repository(row['country_id'])
        city = city_repository(row['city_id'])
        destination = Destination(user, country, city)
        destinations.append(destination)
    return destinations


# def select(id):
#     destination = None
#     sql = "SELECT * FROM destinations WHERE id = %s"
#     values = [id]
#     result = run_sql(sql, values)[0]

#     if result is not None:
#         destination = Destination(result['destination.user_id'], result['destination.country_id'], result['destination.city_id'], result['id'])
#     return destination

def delete(id):
    sql = "DELETE FROM destinations WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM destinations"
    run_sql(sql)