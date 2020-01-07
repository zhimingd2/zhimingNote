# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ZhimingNote(models.Model):
    _name = "zhiming.note"
    _description = "Zhiming Note Test"

    name = fields.Char(string="User Name", request=True)
    phone = fields.Char(string="Phone number")
    note_items = fields.One2many("mynotes.mynoteitems", "note_id")

class mynotes_item(models.Model):
    _name = 'mynotes.mynoteitems'

    note_id = fields.Many2one('mynotes.mynotes','items')
    notes = fields.Text("Notes")
