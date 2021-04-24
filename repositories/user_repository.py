from db.run_sql import run_sql
from models.user import User

def save(user):
    sql = "INSERT INTO users (name, home_city, home_country,) VALUES (%s, %s, %s) RETURNING id"
    values = [user.name, user.home_city, user.home_country]
    results = run_sql(sql, values)
    user.id = results[0]['id']
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

def add_destination():
    destination = [] 
