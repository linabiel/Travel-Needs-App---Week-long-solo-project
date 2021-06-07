Travel Needs

The app Travel Needs helps Oscal Wilde, Peter Parker and Me to track our dream destinations: places we visited and palces we still want to travel to.

Tools Used: 
  HTML/CSS
  Python
  Flask
  PostgreSQl

MVP:
  The app allows the user to track countries and cities they want to visit and those they have visited.
  The user can create and edit countries
  Each country has one or more cities to visit
  The user can create and delete entries for cities
  The app allows the user to mark destinations as visited or still to see

Extensions:
  Have separate pages for destinations visited and those still to visit
  Search for destination by city or country



Run Commands:
  psql -d travel_needs -f db/travel_needs.sql
  python3 console.py
  flask run
