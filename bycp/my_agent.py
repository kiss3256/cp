import requests, json, math
from conenct import Connect

client = Connect.get_connection()
bycp = client['bycp']
db = bycp['bycp-ssc']

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


def all_big(a, b, c):
    if a > 4 and b > 4 and c > 4:
        return 'small'
    if a < 5 and b < 5 and c < 5:
        return 'big'
    return None


def three_combos(data, data1, data2):
    a1 = [int(a) for a in data['open_code']]
    a2 = [int(a) for a in data1['open_code']]
    a3 = [int(a) for a in data2['open_code']]
    b1 = all_big(a1[0], a2[0], a3[0])
    b2 = all_big(a1[1], a2[1], a3[1])
    b3 = all_big(a1[2], a2[2], a3[2])
    b4 = all_big(a1[3], a2[3], a3[3])
    b5 = all_big(a1[4], a2[4], a3[4])

    return (b1, b2, b3, b4, b5)


class Agent(object):
    

    def lottery(self):


    def settle(self, data):


    def buy(self, data):

        if e == 'big':
            data = [
                ('orders[0][title]', '\u7B2C\u4E94\u7403'),
                ('orders[0][num]', '\u7B2C\u4E94\u7403 \u5927'),
                ('orders[0][content]', 'B'),
                ('orders[0][play]', 'B5'),
                ('orders[0][code]', 'jsssc'),
                ('orders[0][odds]', '1.999'),
                ('orders[0][money]', str(int(ep))),
                ('orders[0][check]', 'true'),
                ('code', 'jsssc'),
                ('drawNumber', str(int(now_term) + 1)),
            ]


            print('买大')

            # response = requests.post('https://www-bb77.com/bets', headers=headers, cookies=cookies, data=data)
            #
            # print(response.text)

        if e == 'small':
            data = [
                ('orders[0][title]', '\u7B2C\u4E94\u7403'),
                ('orders[0][num]', '\u7B2C\u4E94\u7403 \u5C0F'),
                ('orders[0][content]', 'B'),
                ('orders[0][play]', 'B5'),
                ('orders[0][code]', 'jsssc'),
                ('orders[0][odds]', '1.999'),
                ('orders[0][money]', str(int(ep))),
                ('orders[0][check]', 'true'),
                ('code', 'jsssc'),
                ('drawNumber', str(int(now_term) + 1)),
            ]

            print('买小')
            # response = requests.post('https://www-bb77.com/bets', headers=headers, cookies=cookies, data=data)
            #
            # print(response.text)

        if e is None:
            pass

        print('----------------------------------------------')
