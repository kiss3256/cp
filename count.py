import requests, json, threading, time

maxCode = 8000
baseUrl = 'http://localhost:5000/result/'


arrResult = {}
openDebug = False


def make_a_request(code):
  global arrResult
  try:
    response = requests.get(baseUrl + code)
    result = json.loads(response.text)
    key = result['turnNum'][8:]
    arrResult[key].append([int(x) for x in result['openNum'].split(',')])
  except Exception as e:
    print(' --- Error --- \n\t ' + str(e))



def init():
  global arrResult

  def three_bit(n):
    if n < 10:
      return '00' + str(n)
    if n < 100:
      return '0' + str(n)
    return str(n)


  for i in range(1, 121):
    arrResult[three_bit(i)] = []




def main():
  global arrResult, openDebug

  init()

  for i in range(maxCode):

    thread = threading.Thread(target=make_a_request, args=(str(i),))
    thread.start()
    # thread.join()

  time.sleep(30)

  try:
    file = open('count.json', 'w')
    file.write(str(arrResult))
    file.close()
  except Exception as e:
    print(' --- Error --- \n\t ' + str(e))



if __name__ == '__main__':
  main()