# -*- coding: utf-8 -*-
{
    'name': 'Web Google Maps Drawing',
    'version': '13.0.1.0.0',
    'author': 'Yopi Angi',
    'license': 'AGPL-3',
    'maintainer': 'Yopi Angi',
    'support': 'yopiangi@gmail.com',
    'category': 'Extra Tools',
    'description': """
Web Google Maps Drawing
=======================

Allows users to draw polygons, rectangles, and circles on the map.
""",
    'depends': [
        'web_google_maps',
    ],
    'website': 'https://apps.odoo.com/apps/modules/12.0/web_google_maps_drawing/',
    'demo': [],
    'images': [
        'static/description/icon.png',
        'static/description/thumbnails.png',
    ],
    'data': [
        'data/google_maps_library.xml',
        'views/template.xml',
        'views/res_config_settings.xml',
    ],
    'qweb': [
        'static/src/xml/drawing.xml',
    ],
    'installable': True
}
