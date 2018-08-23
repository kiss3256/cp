import json
from logging import Logger
from req import Http

headers = {
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 '
                  'Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': '*/*',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
}

logger = None


class User(object):
    """docstring for User"""

    def __init__(self, arg):
        super(User, self).__init__()

        self.status = 'offline'
        self.lastBalance = 0
        self.nowBalance = 0
        self.reached = False

        self.session = Http.get_session()
        self.login(arg)

    def login(self, user):

        username, password = user

        global logger
        logger = Logger(username)

        data = [
            ('username', username),
            ('password', password),
        ]

        res = self.session.post('https://www-bb77.com/do_login', headers=headers, data=data)

        if res.status_code == 200:
            self.status = 'online'
            logger.info('登录成功')

    def buy(self, term, content, amount):
        data = [
        ]

        res = self.session.post('https://www-bb77.com/do_login', headers=headers, data=data)

        return res

    def balance(self):

        res = self.session.post('balance')
        data = json.loads(res.text)

        # update self.nowBalance

        if data:
            self.reached = True

    def run(self, strategy):
        logger.info('use', strategy)
