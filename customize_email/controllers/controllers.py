# -*- coding: utf-8 -*-
# from odoo import http


# class CustomizeEmail(http.Controller):
#     @http.route('/customize_email/customize_email', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/customize_email/customize_email/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('customize_email.listing', {
#             'root': '/customize_email/customize_email',
#             'objects': http.request.env['customize_email.customize_email'].search([]),
#         })

#     @http.route('/customize_email/customize_email/objects/<model("customize_email.customize_email"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('customize_email.object', {
#             'object': obj
#         })
