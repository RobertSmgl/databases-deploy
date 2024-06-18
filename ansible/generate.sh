#!/bin/bash

python3 py_magic/create-inventory.py 
python3 py_magic/generate-ssh-config.py
python3 py_magic/generate-host-vars.py
python3 py_magic/generate-group-vars.py