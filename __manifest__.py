# -*- coding: utf-8 -*-
{
    'name': "corona_virus_api",

    'summary': """
        Corona Virus API
	special thanks to https://services1.arcgis.com""",

    'description': """
        Corona Virus API
	special thanks to https://services1.arcgis.com
    """,

    'author': "yusup nur karimah",
    'website': "https://github.com/yusupnurkarimah",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'data/squence.xml',
    ],
}