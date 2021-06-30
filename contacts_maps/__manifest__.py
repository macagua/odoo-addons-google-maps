# -*- coding: utf-8 -*-
{
    'name': 'Contacts Google Maps',
    'version': '13.0.1.0.1',
    'author': 'Yopi Angi',
    'license': 'AGPL-3',
    'maintainer': 'Yopi Angi<yopiangi@gmail.com>',
    'support': 'yopiangi@gmail.com',
    'category': 'Tools',
    'description': """
Contacts Google Maps
====================

Added Google Maps view on Contacts.
""",
    'depends': [
        'contacts',
        'base_geolocalize',
        'web_google_maps',
        'google_marker_icon_picker'
    ],
    'website': 'https://github.com/gityopie/odoo-addons',
    'data': [
        'views/res_partner.xml',
    ],
    'demo': [],
    'installable': True
}
