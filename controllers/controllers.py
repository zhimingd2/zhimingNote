# -*- coding: utf-8 -*-
from odoo import http

# class ZhimingNote(http.Controller):
#     @http.route('/zhiming_note/zhiming_note/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/zhiming_note/zhiming_note/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('zhiming_note.listing', {
#             'root': '/zhiming_note/zhiming_note',
#             'objects': http.request.env['zhiming_note.zhiming_note'].search([]),
#         })

#     @http.route('/zhiming_note/zhiming_note/objects/<model("zhiming_note.zhiming_note"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('zhiming_note.object', {
#             'object': obj
#         })