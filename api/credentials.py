import os

class Api_Token:
    def __init__(self, username = os.environ.get("API_USERNAME"), password = os.environ.get("API_PASSWORD"), api_token = os.environ.get("API_TOKEN")):
        self.username = username
        self.password = password
        self.api_token = api_token

    def token_code(self):
        return self.api_token

    def user_name(self):
        return self.username

    def user_pass(self):
        return self.password


if __name__ == "__main__":
    test = Api_Token(
        username = os.environ.get("API_USERNAME"),
        password = os.environ.get("API_PASSWORD"),
        api_token= os.environ.get("API_TOKEN")
    )

    print(test.token_code())
    print(test.user_name())
    print(test.user_pass())