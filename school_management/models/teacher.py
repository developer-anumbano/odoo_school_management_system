from odoo import models, fields

class Teacher(models.Model):
    _name = 'school.teacher'
    _description = 'Teacher'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Teacher Name', required=True, tracking=True)
    employee_id = fields.Char(string='Employee ID', required=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], string='Gender', required=True)
    qualification = fields.Char(string='Qualification')
    specialization = fields.Char(string='Subject Specialization')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    joining_date = fields.Date(string='Joining Date')
    salary = fields.Float(string='Salary')
    image = fields.Image(string='Photo')
    state = fields.Selection([
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ], string='Status', default='active', tracking=True)