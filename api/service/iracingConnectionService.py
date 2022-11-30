import base64
import hashlib
import os
import requests
from dotenv import load_dotenv
from http.cookiejar import LWPCookieJar


class IRacingAPI:
    def __init__(self, username=None, encoded_password=None):
        self.authenticated = False
        self.session = requests.Session()
        self.base_url = "https://members-ng.iracing.com"

        self.username = username
        self.encoded_password = encoded_password

    def _build_url(self, endpoint):
        return self.base_url + endpoint

    def _create_login_encryption(self, username, password):
        initial_hash = hashlib.sha256((password + username.lower()).encode('utf-8')).digest()
        base_64_hash = base64.b64encode(initial_hash).decode('utf-8')
        return base_64_hash

    def _get_resource(self, endpoint, payload=None):
        request_url = self._build_url(endpoint)
        resource_obj, is_link = self._get_resource_or_link(request_url, payload=payload)
        if not is_link:
            return resource_obj
        r = self.session.get(resource_obj)
        if r.status_code != 200:
            raise RuntimeError(r.json())
        return r.json()

    def _get_resource_or_link(self, url, payload=None):
        if not self.authenticated:
            self._login()
            return self._get_resource_or_link(url, payload=payload)

        r = self.session.get(url, params=payload)

        if r.status_code == 401:
            # unauthorised, likely due to a timeout, retry after a login
            self.authenticated = False

        if r.status_code != 200:
            raise RuntimeError(r.json())
        data = r.json()
        if not isinstance(data, list) and "link" in data.keys():
            return [data["link"], True]
        else:
            return [data, False]

    def _login(self, cookie_file=None):
        if cookie_file:
            self.session.cookies = LWPCookieJar(cookie_file)
            if not os.path.exists(cookie_file):
                self.session.cookies.save()
            else:
                self.session.cookies.load(ignore_discard=True)
        headers = {'Content-Type': 'application/json'}
        data = {"email": self.username, "password": self.encoded_password}

        try:
            r = self.session.post('https://members-ng.iracing.com/auth', headers=headers, json=data, timeout=5.0)
        except requests.Timeout:
            raise RuntimeError("Login timed out")
        except requests.ConnectionError:
            raise RuntimeError("Connection error")
        else:
            response_data = r.json()
            if r.status_code == 200 and response_data['authcode']:
                if cookie_file:
                    self.session.cookies.save(ignore_discard=True)
                self.authenticated = True
                return "Logged in"
            else:
                raise RuntimeError("Error from iRacing: ", response_data)

    # API Methods
    def get_licenses(self):
        return self._get_resource("/data/lookup/licenses")

    def get_member_info(self):
        return self._get_resource("/data/member/info")

