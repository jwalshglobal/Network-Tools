#!/usr/bin/env python

from __future__ import print_function, unicode_literals
import jinja2

"""
 Using Jinja2 templating and a for-loop inside the template, generate the following configuration snippet:
vlan 501
   name blue501
vlan 502
   name blue502
vlan 503
   name blue503
vlan 504
   name blue504
vlan 505
   name blue505
vlan 506
   name blue506
vlan 507
   name blue507
vlan 508
   name blue508
"""

dict_item = {
    "501": "blue501",
    "502": "blue502",
    "503": "blue503",
}

template_vars = {"vlans": dict_item}

vlan_template = """
{% for key, value in vlans.items() -%} 
vlan {{ key }}
   name {{ value }}
{% endfor %} 
"""

output = jinja2.Template(vlan_template)
print(output.render(template_vars))


