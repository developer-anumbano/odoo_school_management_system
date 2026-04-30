from odoo import models, fields, api

class Exam(models.Model):
    _name = 'school.exam'
    _description = 'Exam'

    name = fields.Char(string='Exam Name', required=True)
    exam_type = fields.Selection([
        ('monthly', 'Monthly Test'),
        ('midterm', 'Mid Term'),
        ('final', 'Final Term'),
    ], string='Exam Type', required=True)
    classroom_id = fields.Many2one('school.classroom', string='Class')
    subject_id = fields.Many2one('school.subject', string='Subject')
    exam_date = fields.Date(string='Exam Date')
    total_marks = fields.Integer(string='Total Marks', default=100)
    pass_marks = fields.Integer(string='Pass Marks', default=40)
    result_ids = fields.One2many('school.result', 'exam_id', string='Results')


class Result(models.Model):
    _name = 'school.result'
    _description = 'Exam Result'

    exam_id = fields.Many2one('school.exam', string='Exam')
    student_id = fields.Many2one('school.student', string='Student', required=True)
    marks_obtained = fields.Float(string='Marks Obtained')
    total_marks = fields.Float(string='Total Marks')
    percentage = fields.Float(string='Percentage', compute='_compute_percentage', store=True)
    grade = fields.Char(string='Grade', compute='_compute_grade', store=True)
    state = fields.Selection([
        ('pass', 'Pass'),
        ('fail', 'Fail'),
    ], string='Result', compute='_compute_grade', store=True)

    @api.depends('marks_obtained', 'total_marks')
    def _compute_percentage(self):
        for rec in self:
            if rec.total_marks > 0:
                rec.percentage = (rec.marks_obtained / rec.total_marks) * 100
            else:
                rec.percentage = 0

    @api.depends('percentage')
    def _compute_grade(self):
        for rec in self:
            if rec.percentage >= 90:
                rec.grade = 'A+'
                rec.state = 'pass'
            elif rec.percentage >= 80:
                rec.grade = 'A'
                rec.state = 'pass'
            elif rec.percentage >= 70:
                rec.grade = 'B'
                rec.state = 'pass'
            elif rec.percentage >= 60:
                rec.grade = 'C'
                rec.state = 'pass'
            elif rec.percentage >= 40:
                rec.grade = 'D'
                rec.state = 'pass'
            else:
                rec.grade = 'F'
                rec.state = 'fail'