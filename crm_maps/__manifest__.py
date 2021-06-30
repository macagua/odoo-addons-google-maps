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
    'website': 'https://apps.odoo.com/apps/modules/13.0/crm_maps/',
    'depends': [
        'crm',
        'web_google_maps',
    ],
    'data': [
        'views/crm_lead.xml',
        'views/res_partner.xml',
    ],
    'demo': [],
    'images': [
        'static/description/icon.png',
    ],
    'installable': True
}
