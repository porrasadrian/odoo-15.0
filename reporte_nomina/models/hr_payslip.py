# -*- coding: utf-8 -*-
from odoo import models, fields,api

class HrPayslip(models.Model):
    _inherit = 'hr.payslip'
    _description = 'Modulo para Reporte de Nomina'

    fecha_pago = fields.Selection([
        ('week_1', '15'),('week_2','28'),('week_3','30'),('week_4','31')], string='Fecha De Pago')
    company_database = fields.Many2one('res.company', string='Empresa', default=lambda self: self.env.company)
    no_nomina = fields.Char(related="employee_id.no_nomina")













