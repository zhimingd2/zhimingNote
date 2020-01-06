# -*- coding: utf-8 -*-

from odoo import models, fields, api

class zhiming_note(models.Model):
    _name = 'zhiming_note.zhiming_note'

     name = fields.Char("MainName")
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100