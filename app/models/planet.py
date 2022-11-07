from app import db


class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    orbital_period = db.Column(db.Integer)
    moon_id = db.Column(db.Integer, db.ForeignKey('moon.id'))
    moon = db.relationship("Moon", back_populates="planets")

    def to_dict(self):
        planet_as_dict = {}
        planet_as_dict["id"] = self.id,
        planet_as_dict["name"] = self.title
        planet_as_dict["description"] = self.description
        planet_as_dict["orbital_period"] = self.orbital_period

    @classmethod
    def from_dict(cls, planet_data):
        new_planet = Planet(name=planet_data["name"],
                        description=planet_data["description"])
        return new_planet