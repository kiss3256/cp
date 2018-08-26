import requests, json

from conenct import Connect


def main():
    import requests

    cookies = {
        'pg_': '2|1:0|10:1535246735|3:pg_|648:eyJyZWdfdGltZSI6ICIyMDE4MDgwNDE0MzkzMyIsICJ1c2VyX2lkIjogIjQxMDcxOCIsICJzaG93X3BhcmVudF9xcSI6IDAsICJuaWNrX25hbWUiOiAiIiwgIm1vbmV5IjogIjAuNjIyIiwgInJlZ19pcCI6ICIxMDEuODUuMzQuMjExIiwgInVzZXJfdHlwZSI6ICIxIiwgImhhc19wcm94eV9ib251cyI6IGZhbHNlLCAidGllciI6ICIxMDAwMSIsICJ1c2VyX2NvZGUiOiAiODQ3MTAxIiwgImxvZ2luX2lwIjogIjExNi4yMzguMTc0LjIzNiIsICJ1X251bSI6ICJIcmdMcXVjSDZHM2xmbHpHTTUyOURxRjBCdE96ekVDYiIsICJ1c2VyX25hbWUiOiAia2lzczMyNTYiLCAicHJldl9sb2dpbl90aW1lIjogIjIwMTgwODI1MjAwNjU4IiwgIm1vbmV5X3R5cGUiOiAiMSIsICJwcmV2X2xvZ2luX2lwIjogIjExNi4yMzguMTc0LjIzNiIsICJlcnJvcl9jb2RlIjogMCwgImhhc19wcm94eV93YWdlIjogZmFsc2UsICJsb2dpbl90aW1lIjogIjIwMTgwODI2MDkxMDM1In0=|2d5f2bbd09facdc2fa02b38d4087b39af7a70e0f4fcc1d6006d0417e72d14fd5',
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

    data = [
        ('command', 'lottery_request_transmit_v2'),
        ('param', '{"lottery_id":"10110","count":3000,"command_id":23}'),
    ]

    response = requests.post('https://pg11b.com/controller/lottery', headers=headers, cookies=cookies, data=data)

    result = json.loads(response.text)
    client = Connect.get_connection()
    bb77 = client["bb77"]
    col = bb77["om_ssc"]

    data = []
    for x in result['data']['detail']['LIST']:
        term = int(x['CP_QS'])
        num = [int(n) for n in x['ZJHM'].split(',')]
        data.append({'term': term, 'n1': num[0], 'n2': num[1], 'n3': num[2], 'n4': num[3], 'n5': num[4]})

    col.insert_many(data)


if __name__ == '__main__':
    main()
