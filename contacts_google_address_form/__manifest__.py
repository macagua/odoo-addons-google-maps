# -*- coding: utf-8 -*-
{
    'name': 'Contacts Google Address Form',
    'version': '13.0.1.0.0',
    'author': 'Yopi Angi',
    'license': 'AGPL-3',
    'maintainer': 'Yopi Angi<yopiangi@gmail.com>',
    'support': 'yopiangi@gmail.com',
    'category': 'Base',
    'sequence': 1000,
    'description': """
Contacts Google Address Form
============================

Use Google Address Form autocomplete to help you find address. 
This added widget Google autocomplete address form on address fields on Contacts.
""",
    'depends': [
        'base_geolocalize',
        'web_google_maps',
    ],
    'website': 'https://apps.odoo.com/apps/modules/13.0/contacts_google_address_form/',
    'data': [
        'views/res_partner.xml',
    ],
    'demo': [],
    'images': [
        'static/description/icon.png',
    ],
    'installable': True
}
