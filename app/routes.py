from flask import Blueprint

class Planet:

    def __init__(self, id, name, description, orbital_period):
        self.id = id
        self.name = name
        self.description = description 
        self.orbital_period = orbital_period 


planets = [Planet(1, "Mercury", "The smallest planet in the solar system", 88),
Planet(2, "Venus", "Sometimes called earth's sister planet", 225),
Planet(3, "Earth", "Only astronomical object known to harbor life", 365),
Planet(4, "Mars", "Named for the Roman god of war", 687),
Planet(5, "Jupiter", "Its larger than all of the other planetes combined", 4343),
Planet(6, "Saturn", "Has a prominent ring system", 10759),
Planet(7, "Uranus", "Named after the greek god of the sky", 30660),
Planet(8, "Neptune", "Furthest planet from the sun", 60225)  ]
