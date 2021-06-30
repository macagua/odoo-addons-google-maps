# -*- coding: utf-8 -*-
{
    'name': 'CRM Google Maps',
    'version': '13.0.1.0.0',
    'author': 'Yopi Angi',
    'license': 'AGPL-3',
    'maintainer': 'Yopi Angi<yopiangi@gmail.com>',
    'support': 'yopiangi@gmail.com',
    'category': 'Sales/CRM',
    'description': """
CRM Google Maps
===============

Added Google Maps (google_map) view on CRM, widget Google autocomplete both address form and places, and geolocation button.
""",
    'depends': ['crm', 'web_google_maps'],
    'website': 'https://github.com/gityopie/odoo-addons',
    'data': [
        'views/crm_lead.xml',
        'views/res_partner.xml',
    ],
    'demo': [],
    'installable': True
}
