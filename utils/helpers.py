import requests
import json
import os

BASE_URL = 'https://automationexercise.com/'

resources_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../schema'))

def load_schema(file):
    with open(os.path.join(resources_path, file)) as file:
        schema = json.load(file)
        return schema

def send_request(base_url, method, endpoint, params=None, data=None, headers=None, json_payload=None):
    # Construct the full URL
    full_url = f"{base_url}/{endpoint}"

    # Lowercase the method to allow using it directly in the requests function call
    method = method.lower()

    # Using a dictionary to map method names to the actual requests library functions
    method_func = getattr(requests, method, None)
    if not method_func:
        raise ValueError(f"Invalid HTTP method: {method}")

    # Make the request
    try:
        response = method_func(full_url, params=params, data=data, headers=headers, json=json_payload)
        response.raise_for_status()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        # Handle HTTP errors (e.g., log, throw, return)
        return None
    except Exception as err:
        print(f"An error occurred: {err}")
        # Handle any other errors (e.g., log, throw, return)
        return None

    # Return response (or do any post-processing)
    return response