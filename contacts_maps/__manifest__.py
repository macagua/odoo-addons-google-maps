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
    'website': 'https://apps.odoo.com/apps/modules/13.0/contacts_maps/',
    'depends': [
        'contacts',
        'base_geolocalize',
        'web_google_maps',
        'google_marker_icon_picker'
    ],
    'data': [
        'views/res_partner.xml',
    ],
    'demo': [],
    'images': [
        'static/description/icon.png',
    ],
    'installable': True
}
