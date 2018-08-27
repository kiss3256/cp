import sys, math

from conenct import Connect


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


class User(object):
    def __init__(self):
        self.balance = 100
        self.last = [(None, 0), (None, 0), (None, 0), (None, 0), (None, 0)]
        self.lose = [0, 0, 0, 0, 0]

        client = Connect.get_connection()
        db = client["db_ssc"]
        self.col = db["ssc"]

    def cal(self, bag):
        last = self.last
        lose = self.lose
        for i in range(5):
            # print(last[i][0])
            if last[i][0] is not None:
                if last[i][0] == bag[i]:
                    self.balance += last[i][1] * 1.99
                    lose[i] = 0
                else:
                    lose[i] += 1
        # print(self.last, self.lose, self.balance)

    def buy(self, bag, combos):
        i = 0
        last = self.last
        lose = self.lose
        max_times = 10
        for x in bag:
            if x[1] and combos[i]:
                money = math.pow(2, min(max_times, lose[i] % max_times))
                self.balance -= money
                last[i] = (0 if x[0] else 1, money)
            else:
                last[i] = (None, 0)
                pass
            i += 1

    def run(self, term, switch):
        data = self.get(term)
        if data:
            big = to_big(data)
            self.cal(big)
            self.buy(zip(big, switch), self.look(term))
            print(term, self.balance)
            if self.balance < 0:
                print(term, 'die')
                sys.exit(0)
        # else:
        #     sys.exit(0)

    def look(self, term):
        a = self.get(term)
        b = self.get(term - 1)
        c = self.get(term - 2)

        if a and b and c:
            return three_combos(a, b, c)
        else:
            return False, False, False, False, False

    def get(self, term):
        return self.col.find_one({'term': term})


def main():
    u = User()

    term = 10735809
    for i in range(1000):
        u.run(term + i, (False, False, True, True, True))


if __name__ == '__main__':
    main()
