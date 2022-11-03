import pytest
from app import create_app
from app import db
from flask.signals import request_finished
from app.models.planet import Planet


@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def make_two_planets(app):

    mercury = Planet(name="Mercury",
       description="The smallest planet in the solar system", orbital_period=88)

    venus = Planet(name="Venus", description="Sometimes called earth's sister planet",
       orbital_period=225)

    db.session.add_all([mercury, venus])
    db.session.commit()