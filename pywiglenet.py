"""
PyWiglenet: A Python wigle.net client
"""
__author__ = "Andres Tarantini"
__email__ = "atarantini@gmail.com"
__license__ = "GPLv3"

import json

import requests
from netaddr import EUI


def parse_address(mac_address):
    """
    Parse MAC address and return it splitted by ":"; it should support
    many formats (00000000000, 00-00-00-00-00-00, etc) as stated in
    netaddr documentation[1].

    :param mac_address:     String with a MAC address
    :return:                Object netaddr.EUI

    [1] https://netaddr.readthedocs.org/en/latest/tutorial_02.html#formatting
    """
    return unicode(EUI(mac_address)).replace("-", ":")


class Wigle:
    """
    Wigle class should be instanced with wigle.net username and password
    in order to perform authentication. Once authentication is made, the
    cookie is cached so it does not need to call subsequent requests for
    each query.
    """
    username = None
    password = None
    auth_cookie = False

    def __init__(self, username, password):
        """
        Wigle constructor

        :param username:    String with the username
        :param password:    String with the password
        """
        self.username = username
        self.password = password

    def get_auth_cookie(self):
        """
        Get authentication cookie that needs to be send on each
        query to the wigle.net API. The cookie is cached once
        authentication succeeds.

        :return:    String with authentication cookie if
                    authentication was success, false otherwise
        """
        if self.auth_cookie:
            return self.auth_cookie

        credentials = {
            "credential_0": self.username,
            "credential_1": self.password
        }

        try:
            response = requests.post(
                "https://wigle.net/api/v1/jsonLogin",
                data=credentials,
                allow_redirects=False
            )
            if response.status_code == 302:
                self.auth_cookie = response.headers['set-cookie'].split(";")[3].strip()
                return self.auth_cookie
        except Exception, e:
            print e

        return False

    def query_mac(self, mac):
        """
        Get information from wigle.net

        :param mac:     String with a MAC address
        :return:        List with results, where each element is a dictionary
                        with a Wigle.net API response if found, False otherwise
        """
        mac = parse_address(mac)
        response = requests.post(
            "https://wigle.net/api/v1/jsonLocation",
            headers={'Cookie': self.get_auth_cookie()},
            data={"netid": mac}
        )
        if response.status_code == 200:
            response_parsed = json.loads(response.text)
            if response_parsed.get("success", False):
                return response_parsed.get("result") if response_parsed.get("result") else False

        return False
