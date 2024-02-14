import requests

def test_hello_world():
    url = "http://localhost:5000/"
    response = requests.get(url)
    assert response.status_code == 200
    assert response.text == "Hello, World!"
    print("The function ran successfully")

if __name__ == "__main__":
    test_hello_world()