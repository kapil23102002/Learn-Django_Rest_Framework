import requests
import json

URL = "http://127.0.0.1:8000/api/student_deserializer/"

# for Create METHOD------------
def post_data():
    data = {
    'name' : 'kaka',
    'roll' : 15, 
    'city' : 'Kak',
    }
 
    json_data = json.dumps(data)

    r = requests.post(url= URL, data = json_data)

    data = r.json()
    print(data)
post_data() # render this post function

# for Update METHOD------------

def update_data():
    data = {
        'id':4, 
        'name' : 'Shruti',
        'city' : 'Ujjain'
        }
    
    json_data = json.dumps(data)
    r = requests.put(url= URL, data = json_data)

    data = r.json()
    print(data)
# update_data() # render this Update function

# for Delete METHOD------------

def delete_data():
    data = {
        'id':4
        }
    
    json_data = json.dumps(data)
    r = requests.delete(url= URL, data = json_data)

    data = r.json()
    print(data)
# delete_data() # render this Delete function