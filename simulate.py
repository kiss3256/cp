import requests, json, random, sys, os, math



def randBig():
    # return 'big'
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

def antiTag(t):
    return 'big' if t != 'big' else 'small'

def isTerm(last, now):
    return int(last) + 1 == int(now)


class Simulator(object):
    """docstring for Simulator"""
    def __init__(self):
        super(Simulator, self).__init__()
        self.nowBalc        = 100
        self.maxBalc        = 100
        self.minBalc        = 100
        self.lastBuy        = (0, 0, 0)
        self.baseCost       = 1
        self.recordResult   = (0, 0)
        self.loseTime       = 0
        self.maxLoseTime    = 3
        self.tapBuy         = 3

        # self.__init()
        self.__init_fsssc()

    def buy_new(self, term, big, cost):
        print(' 第 %s 期 买入 %s %d 元 ' % (term, big, cost))
        self.lastBuy = (term, big, cost)
        self.nowBalc -= cost

        if self.nowBalc <= 0:
            print(' 账户余额不足，程序退出 ')
            print(' 账户剩余金额 %f 最大金额 %f, 最小金额 %f ' % (self.nowBalc, self.maxBalc, self.minBalc))
            sys.exit(0)


    def calculate(self, data):

        term, big, cost = self.lastBuy
        if isTerm(term, data['turnNum']):
            if big == toBig(5, data['openNum']):
                self.nowBalc += round(1.99 * cost, 2)
                print(' 第 %s 期 中奖 %d 元，结算金额 %f 元' % (term, cost, self.nowBalc))
                self.loseTime = 0
            else:
                print(' 第 %s 期 %s 未中奖，结算金额 %f 元' % (data['turnNum'], toBig(5, data['openNum']), self.nowBalc))
                self.loseTime += 1
        else:
            print(' 第 %s 期 %s 未买入' % (data['turnNum'], toBig(5, data['openNum'])))


        if self.nowBalc > self.maxBalc:
            self.maxBalc = self.nowBalc
        if self.nowBalc < self.minBalc:
            self.minBalc = self.nowBalc

        self.lastBuy = (0, 0, 0)
        b, c = self.recordResult
        if c >= self.tapBuy:
            nextCost = self.baseCost * math.pow(2, self.loseTime % self.maxLoseTime)
            self.buy_new(data['turnNum'], antiTag(b), nextCost)

            


    def record(self, data):
        big = toBig(5, data['openNum'])
        b, c = self.recordResult
        if b == big:
            self.recordResult = (b, c+1)
        else:
            self.recordResult = (big, 1)




    def request(self, code):
        if code >= len(self.data):
            print(' 没有足够数据，程序退出 ')
            print(' 账户剩余金额 %f 最大金额 %f, 最小金额 %f ' % (self.nowBalc, self.maxBalc, self.minBalc))
            sys.exit(0)
        data = self.data[code]
        self.record(data)
        self.calculate(data)



    def __init(self):
        print(' 生成测试数据 ')
        rootPath = 'data/6hcp/'
        data = []
        path = os.listdir(rootPath)
        for x in path:
            with open(rootPath+x, 'r') as f:
                d = json.loads(f.readline())
                d.reverse()
                data += d

        self.data = data


    def __init_fsssc(self):
        print(' 生成测试数据 ')
        path = 'data/fsssc_data.json'
        with open(path, 'r') as f:
            d = json.loads(f.read())
            data = d['data']['detail']['LIST']
            data.reverse()
            self.data = data



def main():
    print(' 模拟程序开始 ')
    s = Simulator()
    c = 0
    while True:
        s.request(c)
        c += 1

if __name__ == '__main__':
    main()