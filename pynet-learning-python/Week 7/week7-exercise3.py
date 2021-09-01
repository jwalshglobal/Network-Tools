#!/usr/bin/env python
"""
3a. Create a YAML file that defines a list of interface names. Use the expanded form of YAML.

Use a Python script to read in this YAML list and print it to the screen.

The output of your Python script should be:
['Ethernet1', 'Ethernet2', 'Ethernet3', 'Ethernet4', 'Ethernet5', 'Ethernet6', 'Ethernet7', 'Management1', 'Vlan1']


3b. Expand the data structure defined earlier in exercise3a. This time you should have an 'interfaces' key that refers
 to a dictionary.

Use Python to read in this YAML data structure and print this to the screen.

The output of your Python script should look as follows (in other words, your YAML data structure should yield the
 following when read by Python). You YAML data structure should be written in expanded YAML format.

{'interfaces': {
    'Ethernet1': {'mode': 'access', 'vlan': 10},
    'Ethernet2': {'mode': 'access', 'vlan': 20},
    'Ethernet3': {'mode': 'trunk',
                  'native_vlan': 1,
                  'trunk_vlans': 'all'}
    }
}
"""
import yaml

filename = "interfaces_list.yml"
with open(filename) as f:
    output = yaml.load(f)

print(output)
print()
print('*'*80)

filename = "interfaces_dict.yml"
with open(filename) as f:
    output = yaml.load(f)

print(output)