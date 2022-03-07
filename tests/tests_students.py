def test_getone(client):
    response = client.get("/students/12")

    assert response.status_code == 200


def test_getall(client):
    url = "/students"
    response = client.get(url)

    assert response.status_code == 200
    # assert len(response.json) == 0


def test_create(client):
    new_student_json = {"sid": "13", "enrolled": True, "name": "dazy", "classs": "science", "age": "24",
                        "des": "class 10 student", "fd": "2022-03-03T17:00:26.214Z"}

    response = client.post("/students", json=new_student_json)
    assert response.status_code == 201


def test_update(client):
    new_student_json = {"id": "12", "enrolled": True, "name": "dazy", "classs": "commerce", "age": "24",
                        "des": "class 10 student", "fd": "2022-03-03T17:00:26.214Z"}
    response = client.put('/students/13', json=new_student_json)
    assert response.status_code == 200


def test_delete(client):
    response = client.delete('/students/12')
    assert response.status_code == 204
