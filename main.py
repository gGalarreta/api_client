import os
from os.path import join, dirname
from dotenv import load_dotenv
from rest import client
from rest import session
from errors import errors
from modules.assistance import events

if __name__ == '__main__':
    # Env ability configuration
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    url_app = os.getenv("API_URL")

    # Instance Client
    client = client.Client(url_app)

    # Instance Session
    user_email = "replace_with_eamil
    subdomain = "replace_with_subdomain"
    
    session = session.Session('/sessions', user_email, password, subdomain, client)

    employee_code_assistance = "8733"
    endpoint = "/employees/%s/events" % (employee_code_assistance)
    address = "Lago Nargis 34, Granada, Miguel Hidalgo, CDMX"
    latitude = 19.438748
    longitude = -99.186629


    if session.login():
        event = events.Events(endpoint, address, latitude, longitude, client)
        check_in = event.check_in()
        if check_in["status"] == 200:
            print(check_in["data"])
        else:
            print(check_in["description"])
        check_out = event.check_out()
        if check_out["status"] == 200:
            print(check_out["data"])
        else:
            print(check_out["description"])
    else :
        errors.LOGIN_ERROR

    # # Testing post method

    # body = {
    #   "email": user_email,
    #   "password": password,
    #   "subdomain": subdomain
    # }
    # print(client.post(body, '/sessions'))