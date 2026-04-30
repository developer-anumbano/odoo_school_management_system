from odoo import models, fields, api

class Attendance(models.Model):
    _name = 'school.attendance'
    _description = 'Student Attendance'

    date = fields.Date(string='Date', required=True, 
                      default=fields.Date.today)
    classroom_id = fields.Many2one(
        'school.classroom',
        string='Class', required=True
    )
    teacher_id = fields.Many2one(
        'school.teacher',
        string='Teacher'
    )
    attendance_line_ids = fields.One2many(
        'school.attendance.line',
        'attendance_id',
        string='Attendance Lines'
    )


class AttendanceLine(models.Model):
    _name = 'school.attendance.line'
    _description = 'Attendance Line'

    attendance_id = fields.Many2one(
        'school.attendance',
        string='Attendance'
    )
    student_id = fields.Many2one(
        'school.student',
        string='Student', required=True
    )
    state = fields.Selection([
        ('present', 'Present'),
        ('absent', 'Absent'),
        ('leave', 'Leave'),
    ], string='Status', default='present')