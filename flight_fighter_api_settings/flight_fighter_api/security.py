import hashlib
import json

def make_hash_sha384(data):
    data_json = json.dumps(data)
    data_json_str_temporary = str(data_json)
    data_json_str = "".join(data_json_str_temporary.split())
    hasher = hashlib.sha384()
    hasher.update(data_json_str.encode())
    return hasher.hexdigest()