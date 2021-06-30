# -*- coding: utf-8 -*-
{
    'name': 'Partner Area Google Maps Drawing',
    'version': '13.0.1.0.1',
    'author': 'Yopi Angi <yopiangi@gmail.com>',
    'license': 'AGPL-3',
    'maintainer': 'Yopi Angi<yopiangi@gmail.com>',
    'support': 'yopiangi@gmail.com',
    'category': 'Hidden',
    'description': """
Partner Area
============

A Google Maps Drawing implementation for define the Partner Area for sale.

This module brings the features:

1. Let you define a Partner Area for sale app, drawing shapes with a Google Maps Interface.
""",
    'depends': [
        'web_google_maps_drawing',
        'sale'
    ],
    'website': 'https://github.com/gityopie/odoo-addons',
    'data': [
        'security/ir.model.access.csv',
        'views/res_partner.xml',
        'views/res_partner_area.xml'
    ],
    'demo': [],
    'installable': True
}
