from hashlib import md5
from __main__ import lock
from json import load,dump

def add_hash(string:str):
    hashed = hash(string)
    with lock:

        with open("data/hashes.json","r") as file: data = load(file)
        
        if hashed not in data:
            data[hashed] = string
            with open("data/hashes.json","w") as file: dump(data,file,indent=4)
        return hashed

def get_hash(hashed:str):
    with lock:

        with open("data/hashes.json","r") as file: data = load(file)
        
        return data[hashed] if hashed in data else "Not In DB"

def hash(string:str):
    return md5(string.encode()).hexdigest()