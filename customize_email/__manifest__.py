# -*- coding: utf-8 -*-
{
    'name': "Correo personalizado",
    'summary': """
        Este es un modulo que crea una plantilla personalizada para un correo electronico""",
    'description': """
         Este es un modulo que crea una plantilla personalizada para un correo electronico
    """,
    'author': "Adrian Porras",
    'website': "http://www.yourcompany.com",
    'category': 'Email',
    'version': '15.0',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'sale_management',
        'sale',
    ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'data/email_customize.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
