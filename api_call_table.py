import requests

url = 'https://somesitethatacceptsapicalls/api/table/{tablename}/'

user = 'username'
pwd = 'password'

headers = {"Content-Type":"application/json","Accept":"application/json"}

response = requests.get(url, auth=(user, pwd), headers=headers )

# Check for HTTP codes other than 200
if response.status_code != 200: 
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
    exit()

data = response.json()
print(data)
