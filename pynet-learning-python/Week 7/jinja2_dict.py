#!/usr/bin/env python

from __future__ import print_function, unicode_literals
import jinja2

bgp_vars = {
    "routers": {
        "sf_rtr1": "10.10.10.1",
        "sf_rtr2": "10.10.10.2",
        "sf_rtr3": "10.10.10.3",
        "denver_rtr1": "10.10.10",
        },

    "ip_list": [
        '192.168.1.1',
        '10.1.1.1'
    ]
}

z_template = '''
{%- for router_name, ip_addr in routers.items() %}
{{ router_name }} >>> {{ ip_addr }}
  {%- for ip_addr in ip_list %}
  {{ ip_addr }}
  {%- endfor %}
{%- endfor %}

#Reference Dict Key

{{ routers['sf_rtr1'] }}
'''

template = jinja2.Template(z_template)
print(template.render(bgp_vars))