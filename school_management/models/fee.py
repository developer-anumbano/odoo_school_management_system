from odoo import models, fields, api

class Fee(models.Model):
    _name = 'school.fee'
    _description = 'Fee Management'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    student_id = fields.Many2one('school.student', string='Student', required=True)
    classroom_id = fields.Many2one('school.classroom', string='Class')
    fee_type = fields.Selection([
        ('monthly', 'Monthly Fee'),
        ('admission', 'Admission Fee'),
        ('exam', 'Exam Fee'),
        ('other', 'Other'),
    ], string='Fee Type', required=True)
    amount = fields.Float(string='Amount', required=True)
    due_date = fields.Date(string='Due Date')
    payment_date = fields.Date(string='Payment Date')
    state = fields.Selection([
        ('unpaid', 'Unpaid'),
        ('paid', 'Paid'),
    ], string='Status', default='unpaid', tracking=True)

    def action_mark_paid(self):
        self.state = 'paid'
        self.payment_date = fields.Date.today()