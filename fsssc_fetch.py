import requests



cookies = {
    'pg_': '2|1:0|10:1534852272|3:pg_|648:eyJyZWdfdGltZSI6ICIyMDE4MDgwNDE0MzkzMyIsICJ1c2VyX2lkIjogIjQxMDcxOCIsICJzaG93X3BhcmVudF9xcSI6IDAsICJuaWNrX25hbWUiOiAiIiwgIm1vbmV5IjogIjAuNjIyIiwgInVzZXJfdHlwZSI6ICIxIiwgImhhc19wcm94eV9ib251cyI6IGZhbHNlLCAicHJldl9sb2dpbl90aW1lIjogIjIwMTgwODIxMDEwNTI0IiwgInVzZXJfY29kZSI6ICI4NDcxMDEiLCAiZXJyb3JfY29kZSI6IDAsICJsb2dpbl9pcCI6ICIxMTYuMjM4LjE3NC4yMzYiLCAibW9uZXlfdHlwZSI6ICIxIiwgInRpZXIiOiAiMTAwMDEiLCAicmVnX2lwIjogIjEwMS44NS4zNC4yMTEiLCAicHJldl9sb2dpbl9pcCI6ICIxMTYuMjM4LjE3NC4yMzYiLCAibG9naW5fdGltZSI6ICIyMDE4MDgyMTE5NDg1OCIsICJ1c2VyX25hbWUiOiAia2lzczMyNTYiLCAiaGFzX3Byb3h5X3dhZ2UiOiBmYWxzZSwgInVfbnVtIjogIk9Ia0pRNnBzdWNEdGxUcDlrajlrUmNHNHo4ZENHaE1CIn0=|ebd66aaab8a96fbb5e4e8b1ec81cafcdd85a656e5175a1ae2eec376a200ed95a',
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
  ('param', '{"lottery_id":"10110","count":30000,"command_id":23}'),
]

response = requests.post('https://pg11b.com/controller/lottery', headers=headers, cookies=cookies, data=data)

with open('fsssc_data.json', 'w') as file:
    file.write(response.text)
