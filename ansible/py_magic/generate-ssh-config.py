import json
import re

def write_file(data, config, proxyJump = False):
    for i in data:
        if proxyJump:
            jumpHost = re.sub(r'-\d+$','-1',i)
            config.write(f'Host {i}\n  Hostname {data[i]}\n  User rsamigullin\n  Port 22\n  ProxyJump rsamigullin@{jumpHost}:22\n\n')
        else:
            config.write(f'Host {i}\n  Hostname {data[i]}\n  User rsamigullin\n  Port 22\n\n')
    return

config = open("ssh-files/config", "w")
with open('../terraform-scripts/public-ips') as js:
    data = json.load(js)

config.write("Host *\n  StrictHostKeyChecking no\n  UserKnownHostsFile /dev/null\n\n")
write_file(data,config,False)

with open('../terraform-scripts/private-ips') as js:
    data = json.load(js)
write_file(data,config,True)
config.close()