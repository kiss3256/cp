import requests, json, math

cookies = {
    'pg_': '2|1:0|10:1535247006|3:pg_|648:eyJyZWdfdGltZSI6ICIyMDE4MDgwNDE0MzkzMyIsICJ1c2VyX2lkIjogIjQxMDcxOCIsICJzaG93X3BhcmVudF9xcSI6IDAsICJuaWNrX25hbWUiOiAiIiwgIm1vbmV5IjogIjAuNjIyIiwgInVzZXJfdHlwZSI6ICIxIiwgImhhc19wcm94eV9ib251cyI6IGZhbHNlLCAicHJldl9sb2dpbl90aW1lIjogIjIwMTgwODI1MjAwNjU4IiwgInVzZXJfY29kZSI6ICI4NDcxMDEiLCAiZXJyb3JfY29kZSI6IDAsICJsb2dpbl9pcCI6ICIxMTYuMjM4LjE3NC4yMzYiLCAibW9uZXlfdHlwZSI6ICIxIiwgInRpZXIiOiAiMTAwMDEiLCAicmVnX2lwIjogIjEwMS44NS4zNC4yMTEiLCAicHJldl9sb2dpbl9pcCI6ICIxMTYuMjM4LjE3NC4yMzYiLCAibG9naW5fdGltZSI6ICIyMDE4MDgyNjA5MTAzNSIsICJ1c2VyX25hbWUiOiAia2lzczMyNTYiLCAiaGFzX3Byb3h5X3dhZ2UiOiBmYWxzZSwgInVfbnVtIjogIkhyZ0xxdWNINkczbGZsekdNNTI5RHFGMEJ0T3p6RUNiIn0=|342710e2574b885f1ba91a14139420a0b7988f31ae573bf47146e3d2317f2d4a',
}

headers = {
    'Pragma': 'no-cache',
    'Origin': 'https://pg11b.com',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': '*/*',
    'Cache-Control': 'no-cache',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
    'Referer': 'https://pg11b.com/',
}


def all_big(a, b, c):
    if a > 4 and b > 4 and c > 4:
        return 'small'
    if a < 5 and b < 5 and c < 5:
        return 'big'
    return None


def three_combos(data):
    r1, r2, r3 = data
    a1 = [int(a) for a in r1['ZJHM'].split(',')]
    a2 = [int(a) for a in r2['ZJHM'].split(',')]
    a3 = [int(a) for a in r3['ZJHM'].split(',')]
    b1 = all_big(a1[0], a2[0], a3[0])
    b2 = all_big(a1[1], a2[1], a3[1])
    b3 = all_big(a1[2], a2[2], a3[2])
    b4 = all_big(a1[3], a2[3], a3[3])
    b5 = all_big(a1[4], a2[4], a3[4])

    return (b1, b2, b3, b4, b5)


def to_big(n):
    return 'big' if n > 4 else 'small'


def result(data):
    dd = data[0]
    return [to_big(int(a)) for a in dd['ZJHM'].split(',')]


class Agent(object):
    __last_buy = (0, (None, 0), (None, 0), (None, 0), (None, 0), (None, 0))
    __result = [0, 0, 0, 0, 0]

    def lottery(self):
        data = [
            ('command', 'lottery_request_transmit_v2'),
            ('param', '{"lottery_id":"10110","count":3,"command_id":23}'),
        ]

        response = requests.post('https://pg11b.com/controller/lottery', headers=headers, cookies=cookies, data=data)
        result = json.loads(response.text)
        data = result['data']['detail']['LIST']

        last_term = self.__last_buy[0]
        now_term = data[0]['CP_QS']
        if int(last_term) + 1 == int(now_term):
            print(data)

        return data

    def settle(self, data):
        last_term = self.__last_buy[0]
        now_term = data[0]['CP_QS']
        if int(last_term) + 1 == int(now_term):
            t, b1, b2, b3, b4, b5 = self.__last_buy
            r1, r2, r3, r4, r5 = result(data)
            if b1[0] == r1:
                self.__result[0] = 0
            elif b1[0] is None:
                pass
            else:
                self.__result[0] += 1
            if b2[0] == r2:
                self.__result[1] = 0
            elif b2[0] is None:
                pass
            else:
                self.__result[1] += 1
            if b3[0] == r3:
                self.__result[2] = 0
            elif b3[0] is None:
                pass
            else:
                self.__result[2] += 1
            if b4[0] == r4:
                self.__result[3] = 0
            elif b4[0] is None:
                pass
            else:
                self.__result[3] += 1
            if b5[0] == r5:
                self.__result[4] = 0
            elif b5[0] is None:
                pass
            else:
                self.__result[4] += 1

            self.balance()

        if int(now_term) - int(last_term) > 1:
            self.__last_buy = (0, (None, 0), (None, 0), (None, 0), (None, 0), (None, 0))
            self.__result = [0, 0, 0, 0, 0]

    def buy(self, data):
        last_term = self.__last_buy[0]
        now_term = data[0]['CP_QS']
        if int(last_term) != int(now_term):
            a, b, c, d, e = three_combos(data)

            r1, r2, r3, r4, r5 = self.__result

            ap = math.pow(2, min(r1 % 4, 3))
            bp = math.pow(2, min(r2 % 4, 3))
            cp = math.pow(2, min(r3 % 4, 3))
            dp = math.pow(2, min(r4 % 4, 3))
            ep = math.pow(2, min(r5 % 4, 3))
            print(a, b, c, d, e, '\t', ap, bp, cp, dp, ep)

            self.__last_buy = (data[0]['CP_QS'], (a, ap), (b, bp), (c, cp), (d, dp), (e, ep))

            if e == 'big':

                data = [
                    ('command', 'lottery_logon_request_transmit_v2'),
                    ('param', '{"device_type":1,"use_sys_odds":0,"bet_info":[{"room_id":"0","lottery_id":"10110","issue":"'+str(int(now_term) + 1)+'","method_id":"700010","bet_num":0,"bet_text":"\u5927","odds":"1.998","bet_money":'+str(int(ep))+',"isChecked":true,"$$hashKey":"object:75947"}],"command_id":601}'),
                ]

                response = requests.post('https://pg11b.com/controller/lottery', headers=headers, cookies=cookies,
                                     data=data)

                print(response.text)

            if e == 'small':

                data = [
                    ('command', 'lottery_logon_request_transmit_v2'),
                    ('param', '{"device_type":1,"use_sys_odds":0,"bet_info":[{"room_id":"0","lottery_id":"10110","issue":"'+str(int(now_term) + 1)+'","method_id":"700010","bet_num":1,"bet_text":"\u5C0F","odds":"1.998","bet_money":'+str(int(ep))+',"isChecked":true,"$$hashKey":"object:88759"}],"command_id":601}'),
                ]

                response = requests.post('https://pg11b.com/controller/lottery', headers=headers, cookies=cookies,
                                     data=data)

                print(response.text)

            if e is None:
                pass
            
            print('----------------------------------------------')

    def balance(self):
        response = requests.post('https://pg11b.com/controller/user/get/get_user_balance/410718', headers=headers,
                                 cookies=cookies)
        print(response.text)
