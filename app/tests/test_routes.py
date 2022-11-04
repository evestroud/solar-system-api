def test_get_all_planets_with_empty_db(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_all_planets_with_two_planets(client, make_two_planets):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == [{"id": 1,
	"name": "Mercury",
    "description": "The smallest planet in the solar system",
    "orbital_period": 88
	},
    {"id": 2,
	"name": "Venus",
    "description": "Sometimes called earth's sister planet",
    "orbital_period": 225
	}]

def test_create_one_planet(client):
    # Act
    response = client.post("/planets", json={
        "name": "Planet",
        "description": "Pluto is a planet again",
        "orbital_period": 60
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == "Planet Planet successfully created"
