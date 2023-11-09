# -*- coding: utf-8 -*-
from odoo import models, fields

class HrContractFormNomina(models.Model):
    _name = 'hr.contract.nomina'
    _description = 'Template for payroll contracts'
    _rec_name = 'c_partner_id'

    c_partner_id = fields.Many2one(comodel_name='res.partner', string='Empleado', help='Elige el nombre del empleado')
    employee_id = fields.Many2one(comodel_name='hr.employee')
    the_company_id = fields.Char(string="Compañía", help='Escribe el nombre de la compañia')
    street = fields.Char(string="Domicilio", help='Escribe el domicilio')
    rfc = fields.Char(string="RFC", help='Escribe su RFC')
    city = fields.Char(string="Ciudad", help='Escribe la Ciudad')
    beneficiaries_ids = fields.One2many(comodel_name='beneficiaries.payroll', inverse_name='beneficiaries_id',string='Beneficiarios')

class BeneficiariosNomina(models.Model):
    _name = 'beneficiaries.payroll'
    _description = 'Model for table of payroll beneficiaries'
    _rec_name = 'name'

    beneficiaries_id = fields.Many2one(comodel_name='hr.contract.nomina',readonly=True)
    name = fields.Char(string="Nombre del beneficiario", help='Escribe el nombre del beneficiario')
    relationship = fields.Char(string="Parentesco", help='Escribe su parentesco')
    phone = fields.Char(string="Numero de telefono", help='Escribe su numero de telefono')
    percentage = fields.Float(string='Porcentaje', help='Escribe el porcentaje')
    sequence = fields.Integer()


