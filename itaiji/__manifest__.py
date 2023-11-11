# -*- coding: utf-8 -*-
{
    'name': "itaiji",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['web'],

    # static
    "assets": {
        "web.report_assets_common": [
            "itaiji/static/src/scss/fonts.scss",
            "itaiji/static/src/scss/custom.scss",
        ],
        "web.assets_backend": [
            "itaiji/static/src/scss/fonts.scss",
            "itaiji/static/src/scss/custom.scss",
        ],
        #"web.report_assets_pdf": []
        #"web.assets_common": []
        #"web.assets_frontend": []
    },

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
