# -*- coding: utf-8 -*-
{
    'name': 'Contacts Google Address Form Extended',
    'version': '13.0.1.0.1',
    'author': 'Yopi Angi',
    'license': 'AGPL-3',
    'maintainer': 'Yopi Angi<yopiangi@gmail.com>',
    'support': 'yopiangi@gmail.com',
    'category': 'Base',
    'sequence': 1000,
    'description': """
Contacts Google Address Form Extended
=====================================

Use Google Address Form autocomplete to help you find address.
Extented version of contacts_google_address_form that manage address number.
""",
    'depends': [
        'base_address_extended',
        'contacts_google_address_form',
        'web_google_maps',
    ],
    'website': 'https://github.com/gityopie/odoo-addons',
    'data': [
        'views/res_partner.xml',
        'views/template.xml',
    ],
    'demo': [],
    'installable': True,
}
