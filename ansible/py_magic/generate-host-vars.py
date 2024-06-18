import json
import yaml
import re

def add_host_vars(hostsMap,hostsName):
    resultMap = {}
    for i in hostsMap:
        resultMap = {}
        hostFile = open(f'./host_vars/{i}', 'w')
        hostFile.write("---\n")
        resultMap["ansible_private_ip"] = f'{hostsMap[i]}'
        resultMap["replication_allow"] = []
        for z in hostsMap:
            temp = re.sub(r'-\d+$', '', i)
            if z.find(f'{temp}') == -1:
                continue
            resultMap["replication_allow"].append(hostsMap[z])
        if re.search("-1$",i):
            resultMap.update({'slave': "no"})
        else:
            resultMap.update({'slave': "yes"})
        yaml.safe_dump(resultMap,hostFile, allow_unicode=True)
        hostFile.close()
        del resultMap
    return


with open('../terraform-scripts/all-private-ips') as js:
    data = json.load(js)
hostsName = ["postgres","patroni","stolon"]
add_host_vars(data,hostsName)