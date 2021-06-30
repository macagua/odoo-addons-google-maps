# -*- coding: utf-8 -*-
{
    'name': 'Contacts Google Places Autocomplete',
    'version': '13.0.1.0.0',
    'author': 'Yopi Angi',
    'license': 'AGPL-3',
    'maintainer': 'Yopi Angi<yopiangi@gmail.com>',
    'support': 'yopiangi@gmail.com',
    'category': 'Base',
    'sequence': 1000,
    'description': """
Contacts Google Places Autocomplete
===================================

Use Google Places Form autocomplete to help you find address.
Added widget Google autocomplete places to Contact's name.
""",
    'depends': [
        'base_geolocalize',
        'web_google_maps',
    ],
    'website': 'https://apps.odoo.com/apps/modules/13.0/contacts_google_places_autocomplete/',
    'data': [
        'views/res_partner.xml',
    ],
    'demo': [],
    'images': [
        'static/description/icon.png',
    ],
    'installable': True
}
