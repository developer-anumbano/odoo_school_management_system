from odoo import models, fields

class Classroom(models.Model):
    _name = 'school.classroom'
    _description = 'Classroom'

    name = fields.Char(string='Class Name', required=True)
    section = fields.Char(string='Section', required=True)
    class_teacher_id = fields.Many2one(
        'school.teacher',
        string='Class Teacher'
    )
    student_ids = fields.One2many(
        'school.student',
        'classroom_id',
        string='Students'
    )
    total_students = fields.Integer(
        string='Total Students',
        compute='_compute_total_students'
    )

    def _compute_total_students(self):
        for record in self:
            record.total_students = len(record.student_ids)