from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_root():
    res = client.get("/")
    print(res)
    assert res.json().get("message") == "Have your fun!!"
    assert res.json() == {"message": "Have your fun!!"}
    assert res.status_code == 200
