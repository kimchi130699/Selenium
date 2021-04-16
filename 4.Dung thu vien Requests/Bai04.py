import requests
# demo1 =>get requests
'''
response = requests.get('https://api.github.com')

#status requests thanh cong la 200
print('response.status_code:',response.status_code)

print(response.json()['current_user_url'])

#headers
print('headers :',response.headers ['Cache-Control'])
'''

# demo2 =>add param(query string)
'''
response = requests.get('https://api.github.com/search/respositories?q=requests+language:python')
print('total count',response.json()['total_count'])

response = requests.get(
    'https://api.github.com/search/respositories',
    params ={'q':'requests+language:python'},
)
print('total_count',response.json()['total_count'])
'''

#demo3 :thay doo requests headers
# response = requests.get(
#     'https://api.github.com/search/respositories',
#     params ={'q':'requests+language:python'},
#     headers={'Acecept':
#     'application/vnd.github.v3.text-match+json',
#     },
# )
# json_response = response.json()
# repository = json_response['items'][0]
# print(f'Text matches:{repository['text_matches']}')

#demo4 : Post data form
# response = requests.post('https://httpbin.org/post',data={'name':'kimchi','age':'21'})
# print(response.text)

#demo5: Post data json
# response = requests.post('https://httpbin.org/post',json={'name':'kimchi','age':'21'})
# print(response.text)

#proxies
#fake ip ->fake ip ca may
#fake ip qua proxy

proxies ={
    'http':'http://operator:operator@113.161.210.88:1080/',
    'https': 'http://operator:operator@113.161.210.88:1080/'

}
response = requests.get('https://api.myip.com',proxies = proxies)
print(response.jon())
myip = response.json()['ip']
print(myip)