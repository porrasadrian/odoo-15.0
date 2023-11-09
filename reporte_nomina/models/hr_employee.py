# -*- coding: utf-8 -*-
from odoo import models, fields

class HrEmployee(models.Model):
    _inherit = 'hr.employee'
    _description = 'Datos del empleado'

    curp_employee = fields.Char(string='CURP')
    def _get_text_nomina(self):
        return "1100"
    no_nomina = fields.Char(string='No. Nómina', default=_get_text_nomina)
    edad = fields.Integer(string="Edad")


