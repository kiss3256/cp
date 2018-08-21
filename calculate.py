import json
from matplotlib import pyplot as plt

arrData = []


def init():
  global arrData

  file = open('count.json', 'r')
  result = file.read()
  arrData = json.loads(result)
  file.close()


def count():
  global arrData
  count = 0
  for x in arrData:
    count += len(arrData[x])
  return count


def b5_term(term):
  global arrData

  def three_bit(n):
    if n < 10:
      return '00' + str(n)
    if n < 100:
      return '0' + str(n)
    return str(n)

  if term > 120:
    print(' --- Error --- \n\t term error')
    return False
  term = three_bit(term)

  result = [0 for i in range(10)]
  data = arrData[term]
  for i in range(len(data)):
    n = data[i][-1]
    result[n] += 1
  
  plt.plot(result, 'o')
  plt.ylabel(str(len(data)) + ' times fifth ball number: ')
  plt.ylim(0, 30)
  plt.show()


def b5_all_120():
  global arrData

  result = [0 for i in range(10)]
  for x in arrData:
    data = arrData[x]
    for i in range(len(data)):
      n = data[i][-1]
      result[n] += 1
  
  plt.plot(result, 'o')
  plt.ylabel(str(count()) + ' times fifth ball number: ')
  plt.ylim(0, 1000)
  plt.show()


def main():
  init()
  b5_all_120()
  
  


if __name__ == '__main__':
  main()