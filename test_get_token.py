import requests
from datetime import datetime
def test_get_token():
 url="http://192.168.0.162:8084/api/LoginAPI/generatetoken"
 params={
     "username": "Maker1",
     "password": "Pass@1234",
     "requestdatetime": datetime.now()
 }
 response=requests.get( url,params=params)
 if response.status_code==200:
     try:
         data=response.json()
         print("Response Data: ",data)
     except requests.exceptions.JSONDecodeError:
         print("Response not in JSON")
 else:
     print(response.status_code)
     print(response.text)
 assert isinstance(data, dict)
 assert "statusCode" in data
 assert "statusdesc" in data
 assert "token" in data