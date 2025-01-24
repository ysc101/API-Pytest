import requests

from auth_token import bearer_token
def test_updatepayeedata():
 url="http://192.168.0.162:8084/api/PayeeDetailsAPI/updatedpayeedata"

 headers={"Authorization":f"Bearer {bearer_token}"}

 payload={
  "ecsdate": "2025-01-24T12:55:36.271Z",
  "ecsnumber":5464,
  "beneficiaryname": "Rajan Dudhale",
  "beneficiarybankifsccode": "MAHB0000015",
  "beneficiaryaccountno": "11",
  "uniquepartykey": "okij123"
  }
 response = requests.post(url, headers=headers, json=payload)
 assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"
 if response.status_code == 200:
  try:
   data = response.json()
   print("Response Data: ", data)
  except requests.exceptions.JSONDecodeError:
   print("Response not in JSON")
  except requests.exceptions.HTTPError:
   print("HTTP Request not found")
 else:
  print("Response Code: ", response.status_code)
  print(response.text)
