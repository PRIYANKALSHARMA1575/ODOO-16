from odoo import models, fields

class CollegeTimetable(models.Model):
    _name = 'college.timetable'
    _description = 'College Timetable'

    subject_id = fields.Many2one('college.subject', string='Subject', required=True)
    classroom_id = fields.Many2one('college.classroom', string='Class', required=True)
    day = fields.Selection(
        [('monday', 'Monday'), ('tuesday', 'Tuesday'), ('wednesday', 'Wednesday'),
         ('thursday', 'Thursday'), ('friday', 'Friday'), ('saturday', 'Saturday')],
        string='Day', required=True
    )
    start_time = fields.Float(string='Start Time', required=True)
    end_time = fields.Float(string='End Time', required=True)
