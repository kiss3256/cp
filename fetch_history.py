import requests


def get_history(date):


    headers = {
        'cookie': 'PHPSESSID=27p5o4smndapejab88fsk5l68o',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'referer': 'https://6hcp6.com/pc/game/history.html',
        'authority': '6hcp6.com',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = (
        ('data', date),
        ('game_id', '1'),
    )

    response = requests.get('https://6hcp6.com/pc/game/history', headers=headers, params=params)

    with open('data/6hcp/'+date, 'w') as f:
        f.write(response.text)



def get_date(month):
    ab = lambda x : str(x) if x > 9 else '0' + str(x)
    day = {
        1: [x for x in range(31)],
        2: [x for x in range(28)],
        3: [x for x in range(31)],
        4: [x for x in range(30)],
        5: [x for x in range(31)],
        6: [x for x in range(30)],
        7: [x for x in range(31)],
        8: [x for x in range(31)],
        9: [x for x in range(30)],
        10: [x for x in range(31)],
        11: [x for x in range(30)],
        12: [x for x in range(31)],
    }.get(month, 'error')
    for x in day:
        yield '2018-' + ab(month) + '-' + ab(x+1)
    yield 'end'


def main():
    for x in range(4, 9):
        date = get_date(x)
        day = next(date)
        while day is not 'end':
            get_history(day)
            day = next(date)


if __name__ == '__main__':
    main()