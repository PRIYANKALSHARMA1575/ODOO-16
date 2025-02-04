from odoo import models, fields

class CollegeSubject(models.Model):
    _name = 'college.subject'
    _description = 'College Subject'

    name = fields.Char(string='Subject Name', required=True)
    teacher_id = fields.Many2one('college.teacher', string='Teacher', required=True)
    classroom_id = fields.Many2one('college.classroom', string='Class', required=True)
