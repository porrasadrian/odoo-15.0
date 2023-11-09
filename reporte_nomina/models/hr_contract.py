# -*- coding: utf-8 -*-
from odoo import models, fields

class HrContract(models.Model):
    _inherit = 'hr.contract'


    hr_contract_nomina = fields.Many2one(comodel_name='hr.contract.nomina', string="Plantilla de contrato")
    hr_beneficiares = fields.Many2one(comodel_name='beneficiaries.payroll')
    contract_payment = fields.Monetary(string='Pago Contrato', help='Escribe el pago que se generará en el contrato')




