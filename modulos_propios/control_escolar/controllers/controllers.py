# -*- coding: utf-8 -*-
# from odoo import http


# class ControlEscolar(http.Controller):
#     @http.route('/control_escolar/control_escolar/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/control_escolar/control_escolar/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('control_escolar.listing', {
#             'root': '/control_escolar/control_escolar',
#             'objects': http.request.env['control_escolar.control_escolar'].search([]),
#         })

#     @http.route('/control_escolar/control_escolar/objects/<model("control_escolar.control_escolar"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('control_escolar.object', {
#             'object': obj
#         })
