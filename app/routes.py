from flask import Blueprint, jsonify, make_response, request
from app import db
from .models.planet import Planet


# planets = [
#     Planet(1, "Mercury", "The smallest planet in the solar system", 88),
#     Planet(2, "Venus", "Sometimes called earth's sister planet", 225),
    # Planet(3, "Earth", "Only astronomical object known to harbor life", 365),
#     Planet(4, "Mars", "Named for the Roman god of war", 687),
#     Planet(5, "Jupiter", "Its larger than all of the other planets combined", 4343),
#     Planet(6, "Saturn", "Has a prominent ring system", 10759),
#     Planet(7, "Uranus", "Named after the greek god of the sky", 30660),
#     Planet(8, "Neptune", "Furthest planet from the sun", 60225),  
# ]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET", "POST"])
def handle_planets():
    if request.method == "GET":
        planets = Planet.query.all()
        planet_response = []
        for planet in planets:
            planet_response.append({
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "orbital_period": planet.orbital_period,
            })
        return jsonify(planet_response)

    elif request.method == "POST":
        request_body = request.get_json()
        new_planet = Planet(name=request_body["name"],
                            description = request_body["description"],
                            orbital_period=request_body["orbital_period"])
    
        db.session.add(new_planet)
        db.session.commit()
    
        return make_response(f"Planet {new_planet.name} successfully created")

# @planets_bp.route("/<planet_id>", methods = ["GET"])
# def get_single_planet(planet_id):
#     try:
#         planet_id = int(planet_id)
#     except:
#         return {"message": f"{planet_id} is invalid"}, 400
#     for planet in planets:
#         if planet.id == planet_id:
#             return vars(planet)
#     return {"message": f"planet not found: {planet_id}"}, 404
