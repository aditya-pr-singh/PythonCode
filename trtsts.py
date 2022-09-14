import copy
import requests
import json


url = "https://api.spacexdata.com/v2/launchpads"
resp = requests.get(url)

import json


# Decode UTF-8 bytes to Unicode, and convert single quotes 
# to double quotes to make it valid JSON
my_json = resp.content.decode('utf8').replace("'", '"')
print('- ' * 20)

# Load the JSON to a Python list & dump it back out as formatted JSON
data = json.loads(my_json)
s = json.dumps(data, indent=4, sort_keys=True)

copy_dict = copy.deepcopy(data)
for value in source_list:
    my_dict =copy.deepcopy(copy_dict)
    my_dict['my_key']=some_val
    dict=list(mydict)
    exctraction0 = dict[0]