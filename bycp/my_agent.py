import requests, json, math
from conenct import Connect

import logging

logger = logging.getLogger('bycp.Leyton')
logger.setLevel(logging.DEBUG)

cookies = {
    'more': 'undefined',
    'PHPSESSID': '5m2v61efke2rn8o4bv26euj7p1',
    'page': 'jsssc',
    'goeasyNode': '10',
}

headers = {
    'Pragma': 'no-cache',
    'Origin': 'https://www-bb77.com',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/68.0.3440.106 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': '*/*',
    'Cache-Control': 'no-cache',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
    'Referer': 'https://www-bb77.com/home/jsssc/five_ball.html',
}


def to_big(data):
    a, b, c, d, e = data['n1'], data['n2'], data['n3'], data['n4'], data['n5']
    return (1 if a > 4 else 0,
            1 if b > 4 else 0,
            1 if c > 4 else 0,
            1 if d > 4 else 0,
            1 if e > 4 else 0,)


def three_combos(a, b, c):
    ra = to_big(a)
    rb = to_big(b)
    rc = to_big(c)
    return [all(x) for x in zip(ra, rb, rc)]


class Agent(object):
    def __init__(self):
        client = Connect.get_connection()
        bycp = client['bycp']
        self.db = bycp['bycp-ssc']

        self.last = [(None, 0), (None, 0), (None, 0), (None, 0), (None, 0)]
        self.lose = [0, 0, 0, 0, 0]

    def get(self, term):
        return self.db.find_one({'term': term})

    def set(self, data):
        self.db.update({'term': data['term']}, data, {'upsert': True})

    def look(self, term):
        a = self.get(term)
        b = self.get(term - 1)
        c = self.get(term - 2)

        if a and b and c:
            return three_combos(a, b, c)
        else:
            return False, False, False, False, False

    def lottery(self):
        data = {'term': 1235}
        # self.set(data)

        return data

    def settle(self, data):
        pass

    def buy(self, data):

        a = self.look(data['term'])
        print(a)

        print('----------------------------------------------')

    def run(self):
        data = self.lottery()
        self.settle(data)
        self.buy(data)
