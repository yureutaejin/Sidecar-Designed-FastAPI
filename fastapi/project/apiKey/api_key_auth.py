import json
import time
import os
import hashlib
from random import randint

api_key_directory = os.path.join(os.getcwd(), './config/api_key.json')

## api_key_generator. This function generates a random string of 32 characters. 
def key_generator(domain: str, origin: str, who: str, password: str, tier: str="client") -> dict:
    # hashing with hashlib.sha256
    chars = domain + who + password + str(randint(0, 100))
    hasher = hashlib.sha256()
    hasher.update(chars.encode('utf-8'))
    api_key = hasher.hexdigest()
    
    # open api_key.json file and write the api_key
    existing_data = json.load(open(api_key_directory, 'r'))
    try:
        print("check existing data")
        if len([i for i in existing_data["api-key-list"] if i["domain-char"]==domain if i["who-generate"]==who])>0:
            return {"error": "domain and who already exist"}
    except:
        pass
    new_data = {"domain-char": domain, "origin": origin, "api-key": api_key, "generate-date": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "who-generate": who, "developer-password": password, "tier": tier}
    existing_data["api-key-list"].append(new_data)
    json.dump(existing_data, open(api_key_directory, 'w'), indent=4)
    return new_data

def key_loader() -> list:
    existing_data = json.load(open(api_key_directory, 'r'))
    return existing_data["api-key-list"]

def key_deleter(domain:str, origin: str, who: str, developer_password: str) -> dict:
    existing_data = json.load(open(api_key_directory, 'r'))
    existing_data["api-key-list"] = [i for i in existing_data["api-key-list"] if i["domain-char"]!=domain if i["origin"]!=origin if i["who-generate"]!=who if i["developer-password"]!=developer_password]
    json.dump(existing_data, open(api_key_directory, 'w'), indent=4)
    return {"status": "delete success", "domain": domain, "origin": origin, "who": who, "developer_password": developer_password, "current_keys": existing_data["api-key-list"]}
    
    

# validating api_key from json file
def validate_api_key(api_key: str, api_key_list: list) -> bool:
    if len([i for i in api_key_list if i["api-key"]==api_key]) == 1:
        return True
    return False

def validate_origin(req_origin: str, api_key_list: list) -> bool:
    if len([i for i in api_key_list if i["origin"]==req_origin])==1:
        return True
    return False

    