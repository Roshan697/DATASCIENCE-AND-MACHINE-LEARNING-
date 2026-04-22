## DATA SERIALIZATION
import json 
data = {
    'name':'roshan',
    'age': 100
}

json_str = json.dumps(data)
print(json_str)
print(type(json_str) )

parsed_data = json.loads(json_str)
print(parsed_data)
print(type(parsed_data))