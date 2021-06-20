from db.run_sql import run_sql
from models.destination import Destination
from models.user import User

def save(user):
    sql = "INSERT INTO users (name, home_city, home_country) VALUES (%s, %s, %s) RETURNING id"
    values = [user.name, user.home_city, user.home_country]
    results = run_sql(sql, values)
    # user.id = results[0]['id']
    return user

def delete_all():
    sql = "DELETE FROM users"
    run_sql(sql)

def select_all():
    users = []
    sql = "SELECT * FROM users"
    results = run_sql(sql)

    for row in results:
        user = User(row['name'], row['home_city'], row['home_country'], row['id'])
        users.append(user)
    return users

def select(id):
    user = None
    sql = "SELECT * FROM users WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        user = User(result['name'], result['home_city'], result['home_country'], result['id'])
    return user

def delete(id):
    sql = "DELETE FROM users WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def destinations(user):
    destinations = []

    sql = "SELECT countries.name, cities.name, users.name FROM countries INNER JOIN destinations ON " \
          "destinations.country_id = countries.id INNER JOIN cities ON cities.country_id = countries.id INNER JOIN " \
          "users ON destinations.user_id = users.id WHERE destinations.user_id = %s "
    values = [user.id]
    results = run_sql(sql, values)

    for row in results:
        destination = Destination(row['user'], row['country'], row['city'], row['visited'], row['id'])
        destinations.append(destination)
    return destinations
