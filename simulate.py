import requests, json, random, sys, os, math



def randBig():
    return 'big'
    return 'big' if random.randint(0, 1) else 'small'

def randOdd():
    return 'odd' if random.randint(0, 1) else 'even'

def toBig(pos, openNum):
    data = [int(x) for x in openNum.split(',')]
    if pos:
        return 'big' if data[pos-1] > 4 else 'small'
    else:
        return 'big' if sum(data) > 22 else 'small'

def toOdd(pos, openNum):
    data = [int(x) for x in openNum.split(',')]
    if pos:
        return 'odd' if data[pos-1] % 2 else 'even'
    else:
        return 'odd' if sum(data) % 2 else 'even'



class Simulator(object):
    """docstring for Simulator"""
    def __init__(self):
        super(Simulator, self).__init__()
        self.lastBalc = 500
        self.nowBalc = 500
        self.lastBuy = ()
        self.target = 200
        self.baseCost = 5
        self.count = 0

        self.__init()

    def buy_new(self, term, cost):
        self.lastBuy = (term, 5, randBig(), '', cost)
        self.nowBalc -= cost * 1


    def calculate(self, data):
        
        self.count += 1

        if self.lastBuy == ():
            # buy and return
            self.buy_new(data['turnNum'], self.baseCost)
        else:
            # calculate and buy new
            term, pos, big, odd, cost = self.lastBuy

            nextCost = 0
            if big == toBig(5, data['openNum']):
                self.nowBalc += 1.99 * cost
                nextCost = self.baseCost
            else:
                nextCost = cost * 2
            # if odd == toOdd(5, data['openNum']):
            #     self.nowBalc += 1.99 * cost

                if nextCost > math.pow(self.baseCost, 3):
                    nextCost = self.baseCost
                    self.lastBuy = ()
                    return None

            if self.nowBalc < 0:
                print(' died ')
                sys.exit(0)

            print(self.count)
            print(str(term) + ': ' + str(self.nowBalc))
            self.buy_new(data['turnNum'], nextCost)





    def request(self, code):
        # url = 'http://localhost:5000/result/'
        # response = requests.get(url + str(code))
        # data = json.loads(response.text)
        code %= len(self.data)
        data = self.data[code]
        self.calculate(data)


    def reached(self):
        if self.nowBalc - self.lastBalc > self.target:
            self.lastBalc = self.nowBalc
            print(' --- Reached --- ')
            return True

        return False


    def __init(self):
        rootPath = 'data/6hcp/'
        data = []
        path = os.listdir(rootPath)
        for x in path:
            with open(rootPath+x, 'r') as f:
                d = json.loads(f.readline())
                d.reverse()
                data += d

        self.data = data


def main():
    s = Simulator()
    c = 0
    while True:
        s.request(c)
        c += 1

if __name__ == '__main__':
    main()