import requests
from errors import errors

class Client():

  API_URL = 'localhost:3000/api/v1'

  def __init__(self, url_app = API_URL):
    self.url_base = url_app
    self.token = None

  def set_token(self, token):
    self.token = token

  def get_token(self):
    return self.token

  def get(self, params, endpoint):
    resp = requests.get(self._url(endpoint), headers=self._get_headers())
    return self._response_handler(resp, 'get')

  def post(self, body, endpoint):
    resp = requests.post(self._url(endpoint), headers=self._get_headers(), json = body)
    return self._response_handler(resp, 'post')

  def _url(self, endpoint):
    return self.url_base + endpoint
  
  def _response_handler(self, resp, method):
    response = {
      'status': resp.status_code,
      'description': errors.INVALID_REQUEST
    }
    if resp.status_code == 200:
      response = {
        'status': resp.status_code,
        'data': resp.json()
      }
    return response

  def _get_headers(self):
    headers = {}
    if self.token != None:
      headers = {'Authorization': self.token}
    return headers

