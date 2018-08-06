import requests, json

balance = 1000
code = 0
lastBuy = ''
unit = 10
url = 'http://localhost:5000/result/'
def result(code):
    response = requests.get(url + str(code))
    return json.loads(response.text)


def toBig(str):
    arr = str.split(',')
    sum = 0
    for x in range(5):
        a = int(arr[x])
        sum += a
    if sum > 22:
        return 'big'
    else:
        return 'small'


def main():
    global code, balance, lastBuy, unit
    while True:
        try:
            data = result(code)
            openNum = data.get('openNum')

            if lastBuy:
                if toBig(openNum) == lastBuy:
                    balance += 1.99 * unit
                    unit = 1
                else:
                    if unit < pow(2, 5):
                        unit *= 2
                        code += 10
            lastBuy = toBig(openNum)
            if balance > 1200:
                print('----------------------------')
                balance -= 100
            print( balance )
            balance -= unit

            code += 1
            if balance < 0:
                return -1
        except Exception as e:
            print('error', code, openNum, balance)
            return -1


if __name__ == '__main__':
    main()