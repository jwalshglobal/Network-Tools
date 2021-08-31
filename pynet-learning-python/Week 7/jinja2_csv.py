#!/usr/bin/env python

from __future__ import print_function, unicode_literals
import jinja2
import csv

cvs_file = "bgp_variables.csv"
with open(cvs_file) as f:
    read_csv = csv.DictReader(f)
    print(read_csv)
    for bgp_vars in read_csv:
        advertised_routes = bgp_vars['advertised_routes']
        advertised_routes = advertised_routes.split()
        #print(advertised_routes)
        bgp_vars['advertised_routes'] = advertised_routes
        #print(advertised_routes)

        #need to change to file type .j2
        template_file = 'nxos_bgp_csv.txt'
        with open(template_file) as f:
            bgp_template = f.read()

        template = jinja2.Template(bgp_template)
        print()
        print('-' * 80)
        print(template.render(bgp_vars))
        print()