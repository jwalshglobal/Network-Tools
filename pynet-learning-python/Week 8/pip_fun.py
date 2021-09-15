# Install packages with pip

# pip install netmiko

import netmiko

print(netmiko.__version__)

# pip install netmiko==2.0.1

# Upgrade netmiko AND all dependencies
# pip install --upgrade netmiko

# Install from Github
pip install git+https://github.com/ktbyers/netmiko.git@develop

# install same pip and python together that path is using
# python -m pip install netmiko