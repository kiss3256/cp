import requests
from bs4 import BeautifulSoup
from conenct import Connect


def get_result(page):
    cookies = {
        'PHPSESSID': 'o50cnoien29aidlb6htfnv2r41',
        'goeasyNode': '6',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/68.0.3440.106 Safari/537.36',
    }

    response = requests.get('https://www-bb77.com/user/lottery_results/code/jsssc/p/' + str(page) + '.html',
                            headers=headers, cookies=cookies)

    soup = BeautifulSoup(response.text, features="lxml")

    trs = soup.select('tbody tr')
    for tr in trs:
        td = tr.select('td')
        term = td[0].text
        when = td[1].text
        n1 = td[2].select_one('b').text
        n2 = td[3].select_one('b').text
        n3 = td[4].select_one('b').text
        n4 = td[5].select_one('b').text
        n5 = td[6].select_one('b').text

        yield {'term': int(term), 'when': when, 'n1': int(n1), 'n2': int(n2), 'n3': int(n3), 'n4': int(n4), 'n5': int(n5)}


def main():
    data = []
    try:
        for i in range(1, 50):
            data += get_result(i)
            print(len(data))
    except IndexError:
        client = Connect.get_connection()
        bb77 = client["bb77"]
        col = bb77["om_ssc"]
        col.insert_many(data)


if __name__ == '__main__':
    main()
