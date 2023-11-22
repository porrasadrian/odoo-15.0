# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_cancel(self):
        res = super(SaleOrder, self).action_cancel()
        email_template_id = self.env.ref('customize_email.email_customize').id
        email_template = self.env["mail.template"].browse(email_template_id)
        email_template.send_mail(self.id, force_send=True)
        return res

