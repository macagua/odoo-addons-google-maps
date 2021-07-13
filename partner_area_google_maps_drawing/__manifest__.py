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

A Google Maps Drawing implementation for define the Partner Area for Sales app.

This module brings the features:

1. Let you define a Partner Area for Sales app, drawing shapes with a Google Maps Interface.
""",
    'depends': [
        'base',
        'web',
        'web_google_maps_drawing',
        'sale',
        'sale_management'
    ],
    'website': 'https://github.com/gityopie/odoo-addons/tree/13.0/',
    'data': [
        'security/ir.model.access.csv',
        'views/res_partner.xml',
        'views/res_partner_area.xml'
    ],
    'demo': [],
    'images': [
        'static/description/icon.png',
        'static/description/thumbnails.png',
    ],
    'installable': True
}
