import json
import yaml
import re

def splitByHosts(hostsName, hostsMap):
    for i in hostsName:
        resultMap = {}
        resultMap[i] = {}
        resultMap[i]["hosts"] = {}
        inventoryFile = open(f'./inventory/{i}-hosts.yaml', 'w') 
        for j in hostsMap:
            if j.find(f'{i}') == -1:
                continue
            resultMap[i]["hosts"][j] = {}
            resultMap[i]["hosts"][j]["ansible_user"] = "rsamigullin"
            resultMap[i]["hosts"][j]["ansible_ssh_common_args"] = "-o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no"
        yaml.safe_dump(resultMap,inventoryFile, allow_unicode=True)
        inventoryFile.close()
        del resultMap
    return

hostsName = ["postgres","patroni","stolon"]

with open('../terraform-scripts/public-ips') as js:
    data = json.load(js)

masterMap = {}
masterMap["master"] = {}
masterMap["master"]["hosts"] = {}

for i in data:
    masterMap["master"]["hosts"][i] = {}
    masterMap["master"]["hosts"][i]["ansible_host"] = data[i] 
    masterMap["master"]["hosts"][i]["ansible_user"] = "rsamigullin"
    # masterMap["master"]["hosts"][i]["ansible_become"] = "false"
    masterMap["master"]["hosts"][i]["ansible_ssh_common_args"] = "-o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no"


with open('inventory/master-hosts.yaml', 'w') as yml:
    yaml.safe_dump(masterMap, yml, allow_unicode=True)

with open('../terraform-scripts/private-ips') as js:
    data.update(json.load(js))
splitByHosts(hostsName, data)