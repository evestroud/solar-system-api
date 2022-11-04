from flask import Blueprint, jsonify, make_response, request, abort
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

@planets_bp.route("", methods=["GET"])
def handle_planets():
    queries = request.args.to_dict()
    query_list = []

    for param in queries:
        if param == "id":
            query_list.append(Planet.id.contains(queries[param]))
        elif param == "name":
            query_list.append(Planet.name.contains(queries[param]))
        elif param == "description":
            query_list.append(Planet.description.contains(queries[param]))
        elif param == "orbital_period":
            query_list.append(Planet.orbital_period.contains(queries[param]))
            

    planets = Planet.query.filter_by(**queries)
    planet_response = []
    for planet in planets:
        planet_response.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "orbital_period": planet.orbital_period,
        })
    return jsonify(planet_response)

    
@planets_bp.route("", methods=["POST"])
def create_planet():

    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"],
                        description = request_body["description"],
                        orbital_period=request_body["orbital_period"])
    
    db.session.add(new_planet)
    db.session.commit()
    
    return make_response(jsonify(f"Planet {new_planet.name} successfully created"), 201)



#Validate planet - return response message if planet not found or invalid
def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message":f"{planet_id} is invalid"}, 400))

    planet = Planet.query.get(planet_id)

    if not planet:
        abort(make_response({"message":f"{planet_id} not found"}, 404))
    
    return planet 

#Get single planets info
@planets_bp.route("/<planet_id>", methods = ["GET"])
def handle_planet(planet_id):
   
    planet = validate_planet(planet_id)

    if request.method == "GET":

        return { "id": planet.id,
        "name": planet.name,
        "description": planet.description,
        "orbital_period": planet.orbital_period
         }

#Update a planets info
@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_planet(planet_id)

    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.orbital_period = request_body["orbital_period"]

    db.session.commit()

    return make_response(jsonify(f"Planet #{planet.id} successfully updated"))

#Delete a planet
@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_planet(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet #{planet.id} successfully deleted")



#     try:
#         planet_id = int(planet_id)
#     except:
#         return {"message": f"{planet_id} is invalid"}, 400
#     for planet in planets:
#         if planet.id == planet_id:
#             return vars(planet)
#     return {"message": f"planet not found: {planet_id}"}, 404
