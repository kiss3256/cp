import json, os
from matplotlib import pyplot as plt


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

def main():
  rootPath = 'data/6hcp/'
  data = []
  path = os.listdir(rootPath)
  for x in path:
      with open(rootPath+x, 'r') as f:
          d = json.loads(f.readline())
          d.reverse()
          data += d
  print(len(data))

  result = [0 for x in range(14)]
  last = ''
  count = 0
  for x in data:
    big = toBig(5, x['openNum'])
    if big == last:
      count += 1
    else:
      
      result[count+1] += 1

      last = big
      count = 0

  plt.plot([x/sum(result[1:]) for x in result[1:]])
  plt.show()


if __name__ == '__main__':
  main()