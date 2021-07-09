
net_device = {}
net_device['ip_addr'] = '192.168.1.1'
print(net_device)

net_device2 = {}
net_device2 = {'ip_addr': '192.168.2.1'}
print(net_device2)

net_device['model'] = 'cisco'
print(net_device)

net_device['model'] = 'juniper'
print(net_device)

ios = 'ios'
net_device['device_type'] = ios
print (net_device)

#------------------------
# Methods

get_model = net_device.get('model')
print(get_model)

# return default value if there is an unknown key
get_model = net_device.get('unknown', 'default_model')
print(get_model)

print('*'*80)
print(dir(net_device))

print('*'*80)
print(net_device)
net_device.pop('model')
print(net_device)
net_device['version'] = '12.1.2'

# .update(dictionary)
print('*'*80)
for key in net_device.values():
    print(key)

print('*'*80)
for key in net_device:
    print(key)

print('*'*80)
for key, values in net_device.items():
    print(key)
    print(values)
    print('--------')

print('*'*80)
for k, v in net_device.items():
    print(k)
    print(v)
    print('--------')
