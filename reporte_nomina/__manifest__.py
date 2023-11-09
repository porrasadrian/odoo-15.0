##############################################################################
#
#
#
#
##############################################################################

{
    'name': 'Reporte Nomina',
    'version': '15.0',
    'category': '',
    'description': ''' Reporte de nomina
   ''',
    'summary': "",
    'author': "Adrian Porras",
    'website': '',
    'license': 'AGPL-3',
    'depends': [
        'om_hr_payroll',
        'hr',
    ],
     'data': [
         'security/security.xml',
         'security/ir.model.access.csv',
         'reports/paperformat.xml',
         'reports/paper_format_two.xml',
         'reports/hr_payslip_template_nomina.xml',
         'reports/hr_payslip_template_nomina_extended.xml',
         'reports/hr_payslip_template.xml',
         'reports/hr_payslip_template_extended.xml',
         'reports/hr_contracts_nomina.xml',
         'reports/hr_contracts_nomina_report.xml',
         'views/menu.xml',
         'views/hr_payslip_view.xml',
         'views/hr_employee_view_form.xml',
         'views/hr_payroll_structure_view_form.xml',
         'views/hr_contract.xml',
         'views/hr_contract_nomina.xml',





     ],

    'installable': True,
}
