import requests


class Http(object):
    @staticmethod
    def get_session():
        return requests.Session()
