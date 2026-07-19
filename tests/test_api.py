from fastapi.testclient import TestClient
from app.main import app
client = TestClient(app)

#Testing the root endpoint
def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "FizzBuzz API is running!"
    }

# Test the health endpoint
def test_health():
    response = client.get("/health")

    assert response.status_code == 200

    body = response.json()
    
    assert body["status"] == "healthy"
    assert body["service"] == "FizzBuzz Production"
    assert body["version"] == "1.0.0"
    
# Test the fizzbuzz endpoint
def test_fizzbuzz():
    response = client.get(
        "/fizzbuzz",
        params={
            "int1": 3,
            "int2": 5,
            "limit": 15,
            "str1": "Fizz",
            "str2": "Buzz"
        },
    )

    assert response.status_code == 200

    assert response.json() == [
        "1",
        "2",
        "Fizz",
        "4",
        "Buzz",
        "Fizz",
        "7",
        "8",
        "Fizz",
        "Buzz",
        "11",
        "Fizz",
        "13",
        "14",
        "FizzBuzz"
    ]

def test_invalid_limit():
    response = client.get(
        "/fizzbuzz",
        params={
            "int1": 3,
            "int2": 5,
            "limit": 0,
            "str1": "Fizz",
            "str2": "Buzz",
        },
    )
    
    assert response.status_code == 422

def test_statistics():
    for _ in range(2):
        client.get(
            "/fizzbuzz",
            params={
                "int1": 3,
                "int2": 5,
                "limit": 15,
                "str1": "Fizz",
                "str2": "Buzz",
            },
        )

    response = client.get("/statistics")

    assert response.status_code == 200

    body = response.json()

    assert body["int1"] == 3
    assert body["int2"] == 5
    assert body["limit"] == 15
    assert body["str1"] == "Fizz"
    assert body["str2"] == "Buzz"
    assert body["hits"] >= 2