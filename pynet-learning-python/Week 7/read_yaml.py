
import yaml

# Import yaml file with list of IP addresses
filename = "my_devices_list.yml"
with open(filename) as f:
    output = yaml.load(f)

print(output)
print(type(output))
print(output[2])


# Import yaml file with Dictionary
filename_1 = "my_devices_dict.yml"
with open(filename_1) as f:
    output_dict = yaml.load(f)

print()
print('-'*80)
print(output_dict)
print(type(output_dict))
print(output_dict['rtr3'])