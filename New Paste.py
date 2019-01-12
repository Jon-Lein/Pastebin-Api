import requests

url = 'https://pastebin.com/api/api_post.php'

# required options
api_dev_key = ''
api_option = 'paste'
api_paste_code = 'Python Test'

# optional
user_key = ''
api_paste_name = 'Python api test'
# api_paste_format = ''
api_paste_private = '2'
api_paste_expire_date = 'N'

parameters = {
'api_dev_key' : api_dev_key,
'api_option' : api_option,
'api_paste_private' : api_paste_private, 
'api_user_key' : user_key, 
'api_paste_name' : api_paste_name, 
'api_paste_code' : api_paste_code,
}

r = requests.post(url, data=parameters)
print(r.text)
