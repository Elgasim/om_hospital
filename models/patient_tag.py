from datetime import date
from odoo import fields, models, api
class PatientTag(models.Model):
    _name = 'patient.tag'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'PatientTag'

    name = fields.Char(string="Name")
    active = fields.Boolean(string="Active")
    color = fields.Integer(string="Color")
    color_2 = fields.Char(string="Color 2")
