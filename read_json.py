import json
import os     

def get_json_value(file="parameter.json", table="parameter", parameter="ticker_list"):
    with open(file, 'r') as parameter_json:
        if os.path.getsize(file) > 0:
            dic = json.load(parameter_json)
            return dic[table][parameter]
        else:
            return "Parameter.json is empty"