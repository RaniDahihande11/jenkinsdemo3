# import requests
# import pandas as pd
# #  to read data from api use requests

# # function to use read data from requests

# response = requests.get('https://jsonplaceholder.typicode.com/users0')
# data = response.json()

# df = pd.DataFrame(data)
# df = df[['id','name']]

# print(df)

import os
token = os.getenv("TOEKN")
print(f"TOEKN = ${token}")

if token=="1234":
    print('valid')
else:
    print('invalid')