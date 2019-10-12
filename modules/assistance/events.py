from rest import client
from errors import errors

class Events():

  def __init__(self, endpoint, address, latitude, longitude, rest_client):
    self.endpoint = endpoint
    self.address = address
    self.latitude = latitude
    self.longitude = longitude
    self.rest_client = rest_client
  
  def check_in(self):
    body = self._event_structure("check_in")
    resp = self.rest_client.post(body, self.endpoint)
    return self._response_handler(resp)

  def check_out(self):
    body = self._event_structure("check_out")
    resp = self.rest_client.post(body, self.endpoint)
    return self._response_handler(resp)

  def _event_structure(self, event_type):
    return {
      "event": {
        "event_type": event_type,
        "address": self.address,
        "latitude": self.latitude,
        "longitude": self.longitude
      }
    }

  def _response_handler(self, resp):
    response = {
      'status': resp["status"],
      'description': errors.INVALID_REQUEST
    }
    if resp["status"] == 200:
      response = {
        'status': resp["status"],
        'data': resp["data"]
      }
    return response