# -*- coding: utf-8 -*-


{
    'name': 'Hospital Management',
    'version': '15.0.0',
    'sequence': -100,
    'author': 'Mohammed',
    'category': 'Hospital',
    'website': 'https://www.elgasim.com/',
    'summary': 'Hospital management System',
    'description': """Hospital management System""",
    'depends': ['base','mail','product'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/patient_view.xml',
        'views/female_patient_view.xml',
        'views/male_patient_view.xml',
        'views/kid_patient_view.xml',
        'views/female_patient_context_view.xml',
        'views/male_patient_context_view.xml',
        'views/kid_patient_context_view.xml',
        'views/appointment_view.xml',
    ],
    'demo': [],
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
