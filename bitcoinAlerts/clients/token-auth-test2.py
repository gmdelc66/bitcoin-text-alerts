import requests

local_host = "http://127.0.0.1:8000/"


def client():
    # data = {
    #     "username": "rest_test_user",
    #     "password1": "asdasdasd123",
    #     "password2": "asdasdasd123"
    # }

    # response = requests.post(
    #     local_host+"api/rest-auth/registration", data=data)
    token_h = "Token 68dd1b27fcac7c731125157a72c93ae0e1603d98"
    headers = {
        "Authorization": token_h
    }
    response = requests.get(local_host+"api/profiles/", headers=headers)
    print("Status Code: ", response.status_code)
    response.data = response.json()
    print(response.data)


if __name__ == "__main__":
    client()
