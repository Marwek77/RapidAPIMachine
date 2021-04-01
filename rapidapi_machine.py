import json
import requests


class RapidApiMachine:

    def __init__(self, method, endpoint, arguments):
        self.method = method
        self.endpoint = endpoint
        self.arguments = arguments

    @staticmethod
    def rapid_api_key_build():
        with open("rapid_api_key_vault.bin", encoding="utf-8") as binary_file:
            # Read the whole file at once
            rapid_api_key = binary_file.read()
        return rapid_api_key

    @staticmethod
    def header_buid(rapid_api_key, endpoint_host):
        headers = {
            'x-rapidapi-key': rapid_api_key,
            'x-rapidapi-host': endpoint_host
        }
        return headers

    @staticmethod
    def call_response_get(method, url, headers, params):
        call_get = requests.request(method=method, url=url, headers=headers, params=params)
        return call_get

    @staticmethod
    def call_response_post(method, url, payload, headers):
        call_post = requests.request(method=method, url=url, data=payload, headers=headers)
        return call_post

    def endpoint_host_build(self):
        # build endpoint_host from endpoint for headers
        string_a = self.endpoint.partition("https://")
        string_b = string_a[2].rpartition(".com")
        endpoint_host = "".join((string_b[0], ".com"))
        print(self.endpoint)
        print(endpoint_host)
        return endpoint_host

    def decision(self, headers):
        global response
        if self.method == "GET":
            response = self.call_response_get(self.method, self.endpoint, headers, self.arguments)
        elif self.method == "POST":
            response = self.call_response_post(self.method, self.endpoint, self.arguments, headers)
        else:
            print("Wrong method")

    def jprint(self, response):
        text = response.json()
        form = json.dumps(text, sort_keys=True, indent=4)
        return print(form)

    def get_api_machine_data(self):
        global response
        rapid_api_key = self.rapid_api_key_build()
        endpoint_host = self.endpoint_host_build()
        headers = self.header_buid(rapid_api_key, endpoint_host)
        self.decision(headers)
        self.jprint(response)
