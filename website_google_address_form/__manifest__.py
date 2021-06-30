# -*- coding: utf-8 -*-
{
    'name': 'Website Google Address Form',
    'version': '13.0.1.0.1',
    'author': 'Yopi Angi',
    'license': 'AGPL-3',
    'maintainer': 'Yopi Angi<yopiangi@gmail.com>',
    'support': 'yopiangi@gmail.com',
    'category': 'Extra Tools',
    'description': """
Website Google Address Form
===========================

Enable Google Address Form Autocomplete on Website sale customer form
""",
    'depends': [
        'website_sale',
        'web_google_maps'
    ],
    'demo': [],
    'website': 'https://apps.odoo.com/apps/modules/12.0/website_google_address_form/',
    'data': [
        'views/template.xml',
        'views/res_config_settings.xml'
    ],
    'installable': True
}
