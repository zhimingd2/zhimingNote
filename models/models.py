# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ZhimingNote(models.Model):
    _name = "zhiming.note"
    _description = "Zhiming Note Test"

    name = fields.Char(string="NoteMain", request=True)

