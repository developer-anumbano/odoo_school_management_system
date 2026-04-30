from odoo import models, fields

class Student(models.Model):
    _name = 'school.student'
    _description = 'Student'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Student Name', required=True, tracking=True)
    roll_number = fields.Char(string='Roll Number', required=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], string='Gender', required=True)
    date_of_birth = fields.Date(string='Date of Birth')
    parent_name = fields.Char(string='Parent Name')
    parent_phone = fields.Char(string='Parent Phone')
    address = fields.Text(string='Address')
    image = fields.Image(string='Photo')
    state = fields.Selection([
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ], string='Status', default='active', tracking=True)
    classroom_id = fields.Many2one(
    'school.classroom',
    string='Class'
)