import requests
import json
import os

BASE_URL = 'https://automationexercise.com/'

resources_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../schema'))

def load_schema(file):
    with open(os.path.join(resources_path, file)) as file:
        schema = json.load(file)
        return schema

def send_request(endpoint, method, **kwargs):
    method = method.lower()
    method_func = getattr(requests, method)
    response = method_func(BASE_URL + endpoint, **kwargs)
    return response