# -*- coding: utf-8 -*-
{
    'name': "osm__inventory_qr",

    'summary': """
        QR Inventory
    """,

    'description': """
        QR Inventory
    """,

    'author': "OSM",
    'website': "http://www.osm.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','stock', 'website'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/qr.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'external_dependencies': {
        'python' : ['pyusb','pyserial','qrcode'],
    },
}
