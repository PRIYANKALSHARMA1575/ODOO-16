from odoo import models, fields,api

class CollegeDepartment(models.Model):
    _name = 'college.department'
    _description = 'Department'

    name = fields.Char(string="Department Name", required=True)
    classroom_ids = fields.One2many('college.classroom', 'department_id', string="Classrooms")

