#!/usr/bin/env python

from __future__ import print_function, unicode_literals
import jinja2

"""
 Using a conditional in a Jinja2 template, generate the following output:

crypto isakmp policy 10
 encr aes
 authentication pre-share
 group 5
crypto isakmp key my_key address 1.1.1.1 no-xauth
crypto isakmp keepalive 10 periodic

The encryption of aes, and the Diffie-Hellman group should be variables in the template.

Additionally this entire ISAKMP section should only be added if the isakmp_enable variable is set to True.

Your template should be inside your Python program for simplicity.

"""

crypto_vars = {
    "aes": True,
    "group_5": True
}

crypto_template = """
crypto isakmp policy 10
 {%- if aes %}
 encr aes
  {%- endif %}
 authentication pre-share
 {%- if group_5 %}
 group 5
 {%- endif %}
crypto isakmp key my_key address 1.1.1.1 no-xauth
crypto isakmp keepalive 10 periodic
"""

output = jinja2.Template(crypto_template)
print(output.render(crypto_vars))


