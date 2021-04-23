from db.run_sql import run_sql

from models.city import City

def save(city):
    sql = "INSERT INTO cities (name) VALUES (%s) RETURNING id"
    values = [city.name]
    results = run_sql(sql, values)
    city.id = results[0]['id']
    return city

def delete_all():
    sql = "DELETE FROM users"
    run_sql(sql)
