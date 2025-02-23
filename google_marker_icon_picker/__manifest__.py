# -*- coding: utf-8 -*-
{
    'name': 'Google Marker Icon Picker',
    'version': '13.0.1.0.0',
    'author': 'Yopi Angi',
    'license': 'AGPL-3',
    'maintainer': 'Yopi Angi<yopiangi@gmail.com>',
    'support': 'yopiangi@gmail.com',
    'category': 'Extra Tools',
    'description': """
Google Marker Icon Picker
=========================
- New widget `google_marker_picker` allowing user to assign marker's color
  manually. To apply the selecter marker on map, you can tell map view by
  adding attribute color='[field_name]'
""",
    'website': 'https://apps.odoo.com/apps/modules/13.0/google_marker_icon_picker/',
    'depends': [
        'web_google_maps',
    ],
    'data': [
        'views/template.xml',
    ],
    'qweb': [
        'static/src/xml/marker_color.xml',
    ],
    'demo': [],
    'images': [
        'static/description/icon.png',
    ],
    'installable': True,
}
