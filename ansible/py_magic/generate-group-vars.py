import yaml
import re

def generate_group_vars(hostsName):
    with open('../terraform-scripts/all-private-ips') as stream:
        inputData = yaml.safe_load(stream)
    for j in hostsName:
        try:
            stream = open(f'./group_vars/{j}','r')
            outputData = yaml.safe_load(stream)
            stream.close()
        except:
            outputData = {}
            outputData.update({'replica_password': 'replicaPass'})
        for i in inputData:
            if re.search("-1$",i) and i.find(f'{j}') != -1:
                outputData["primary_address"] = inputData[i]
                stream = open(f'./group_vars/{j}','w')
                stream.write("---\n")
                yaml.safe_dump(outputData,stream, allow_unicode=True)
                stream.close
        del outputData
    return

def configure_etcd(etcdGroups):
    with open('../terraform-scripts/all-private-ips') as stream:
        inputData = yaml.safe_load(stream)
    for j in etcdGroups:
        with open(f'./group_vars/{j}') as stream:
            outputData = yaml.safe_load(stream)
        stream = open(f'./group_vars/{j}','w')
        outputData["etcd_map"] = {}
        for i in inputData:
            if i.startswith(f'{j}'):
                outputData["etcd_map"][i] = {'name': f'{i}', 'ip': inputData[i]}
        stream.write("---\n")
        yaml.safe_dump(outputData,stream, allow_unicode=True)
        stream.close
        

hostsName = ["postgres","patroni","stolon"]
generate_group_vars(hostsName)
etcdGroups = ["patroni", "stolon"]
configure_etcd(etcdGroups)