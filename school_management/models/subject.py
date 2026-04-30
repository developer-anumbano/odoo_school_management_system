from odoo import models, fields

class Subject(models.Model):
    _name = 'school.subject'
    _description = 'Subject'

    name = fields.Char(string='Subject Name', required=True)
    code = fields.Char(string='Subject Code', required=True)
    total_marks = fields.Integer(string='Total Marks', default=100)
    pass_marks = fields.Integer(string='Pass Marks', default=40)
    teacher_id = fields.Many2one(
        'school.teacher',
        string='Subject Teacher'
    )
    classroom_ids = fields.Many2many(
        'school.classroom',
        string='Classes'
    )