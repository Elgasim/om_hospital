from datetime import date
from odoo import fields, models, api
class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hpspital Patient'

    name = fields.Char(string="Name",tracking=True)
    ref = fields.Char(string="Reference")
    age = fields.Integer(string="Age",tracking=True,compute="_compute_age", store=True)
    date_of_birth = fields.Date('Date of birth')
    gender = fields.Selection([('male','Male'),('female','Female')],string="Gender",tracking=True)
    active = fields.Boolean(string="Active",default=True)
    document = fields.Binary(string="Document")
    patient_image = fields.Image(string="Patient Image")
    file_name =fields.Char(string="Document Name")

    @api.depends("date_of_birth")
    def _compute_age(self):
        today = date.today()
        for rec in self:
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 0
