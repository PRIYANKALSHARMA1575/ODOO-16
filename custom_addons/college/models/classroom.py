from odoo import models, fields,api

class CollegeClass(models.Model):
    _name = 'college.classroom'
    _description = 'Classroom'

    name = fields.Char(string="Name", required=True)
    department_id = fields.Many2one('college.department', string="Department")
    attendance_ids = fields.One2many('college.attendance', 'classroom_id', string="Attendance")

    def name_get(self):
        """ Method to display the name in the format 'Class Name - Department Name' """
        result = []
        for record in self:
            name = f"{record.name} - {record.department_id.name}" if record.department_id else record.name
            result.append((record.id, name))
        return result
