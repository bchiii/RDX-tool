import json
from time import sleep


sleep(2)

file = open("network.json" or "network\network.json", "r") 
index = file.read()
index_py = json.loads(index)
network = index_py
file.close()





    
 