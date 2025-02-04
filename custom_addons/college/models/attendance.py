from odoo import models, fields, api, _

class CollegeAttendance(models.Model):
    _name = 'college.attendance'
    _description = 'Student Attendance'
    _inherit = 'mail.thread'

    student_id = fields.Many2one('college.student', string='Student', required=True, tracking=True)
    teacher_id = fields.Many2one('college.teacher', string="Teacher", compute="_compute_teacher", store=True)
    date = fields.Date(string='Date', required=True, default=fields.Date.context_today, tracking=True)
    status = fields.Selection(
        [('present', 'Present'), ('absent', 'Absent'), ('late', 'Late')],
        string='Status', required=True, tracking=True
    )
    notes = fields.Text(string='Notes')
    present=fields.Boolean(string="Present",default=False)
    classroom_id=fields.Many2one('college.classroom', string="Class",required=True)
    
    
    @api.depends('student_id')
    def _compute_teacher(self):
        for record in self:
            record.teacher_id = record.student_id.teacher_id.id if record.student_id else False

    @api.onchange('status')
    def _onchange_status(self):
        for record in self:
            record.present = record.status == 'present'

    _sql_constraints = [
        ('unique_attendance', 'unique(student_id, date)', 'Attendance for this student on the same date already exists!')
    ]
