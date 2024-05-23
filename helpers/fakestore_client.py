import requests


class FakeStoreClient:

    def __init__(self, base_url):
        self.base_url = base_url
        self.headers = {"Accept": "application/json"}

    def get_all_carts(self, params=None, headers=None):
        response = requests.get(
            self.base_url + "/carts",
            params=params,
            headers=self.headers if headers == None else headers,
        )
        return response

    def get_cart(self, id: int, headers=None):
        response = requests.get(
            self.base_url + "/carts/%s" % id,
            headers=self.headers if headers == None else headers,
        )
        return response

    def get_user_carts(self, user_id: int, params=None, headers=None):
        response = requests.get(
            self.base_url + "/carts/user/%s" % user_id,
            params=params,
            headers=self.headers if headers == None else headers,
        )
        return response

    def add_cart(self, payload, headers=None):
        response = requests.post(
            self.base_url + "/carts",
            data=payload,
            headers=self.headers if headers == None else headers,
        )
        return response

    def update_cart(self, id: int, payload, headers=None):
        response = requests.put(
            self.base_url + "/carts/%s" % id,
            data=payload,
            headers=self.headers if headers == None else headers,
        )
        return response

    def delete_cart(self, id: int, headers=None):
        response = requests.delete(
            self.base_url + "/carts/%s" % id,
            headers=self.headers if headers == None else headers,
        )
        return response
