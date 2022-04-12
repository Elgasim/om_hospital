from odoo import fields, models, api
class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'HospitalAppointment'
    _rec_name = 'ref'

    patient_id = fields.Many2one('hospital.patient',string='Patient')
    ref = fields.Char(string="Reference")
    gender = fields.Selection(related='patient_id.gender',string="Gender")
    appointment_time = fields.Datetime("Appointment Time", default=fields.Datetime.now)
    booking_date = fields.Date("Booking Date", default=fields.Date.today)
    prescription = fields.Html("Prescription")
    priority = fields.Selection([('0','Normal'),
                                 ('1','Low'),
                                 ('2','High'),
                                 ('3','Very High')],string="Priority")
    state = fields.Selection([('draft','Draft'),
                                 ('in_consultation','In Consultation'),
                                 ('done','Done'),
                                 ('cancel','Cancelled')],string="State",default="draft",required=True)

    @api.onchange("patient_id")
    def onchange_patient_id(self):
        self.ref = self.patient_id.ref

    def action_test(self):
        print('GOOOOOOOOOO')
        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'successfully clicking',
                'type': 'rainbow_man',
            }
        }

