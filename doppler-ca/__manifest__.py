# Copyright 2020 Vauxoo
# License LGPL-3 or later (http://www.gnu.org/licenses/lgpl).
{
    'name': 'Instance Creator for Doppler Canada',
    'summary': '''
    Instance creator for Doppler Canada. This is the app.
    ''',
    'author': 'Vauxoo',
    'website': 'https://www.vauxoo.com',
    'license': 'LGPL-3',
    'category': 'Installer',
    'version': '14.0.1.0.2',
    'depends': [
        'account_accountant',
        'crm',
        'hr_appraisal',
        'hr_expense',
        'hr_holidays',
        'l10n_ca',
        'project',
        'purchase',
        'sale_management',
        'stock',
        'website',
    ],
    'data': [
        'data/res_company_data.xml',
        'views/assets.xml',
        'views/templates/mail_templates.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
