import requests
import json

URL = "http://127.0.0.1:8000/api/student_deserializer/"

data = {
 'name' : 'Rohit',
    'roll' : 105, 
    'city' : 'Ganga Nagar'}
   


json_data = json.dumps(data)

r = requests.post(url= URL, data = json_data)

data = r.json()
print(data)