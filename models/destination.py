class Destination:

    def __init__(self, user, country, city, visited=False, id=None):
        self.user = user
        self.country = country
        self.city = city
        self.visited = visited
        self.id = id

    def mark_visited(self):
        self.visited = True
