from rest import client

class Session():

  def __init__(self, endpoint, user_email, password, subdomain, rest_client):
    self.endpoint = endpoint
    self.user_email = user_email
    self.password = password
    self.subdomain = subdomain
    self.rest_client = rest_client
    self.token = None

  def login(self):
    body = {
      "email": self.user_email,
      "password": self.password,
      "subdomain": self.subdomain
    }
    resp = self.rest_client.post(body, self.endpoint)
    if resp["status"] == 200:
      self.rest_client.set_token(resp["data"]["access_token"])
      return True
    return False

  def get_token(self):
    return self.token



  