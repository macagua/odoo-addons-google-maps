# -*- coding: utf-8 -*-
{
    'name': 'Partner Area (Google Maps Drawing demo implementation)',
    'version': '13.0.1.0.1',
    'author': 'Yopi Angi',
    'license': 'AGPL-3',
    'maintainer': 'Yopi Angi<yopiangi@gmail.com>',
    'support': 'yopiangi@gmail.com',
    'category': 'Hidden',
    'description': """
Partner Area
============
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
