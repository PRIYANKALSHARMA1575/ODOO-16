from odoo import api, models, fields, _
from odoo.exceptions import ValidationError

class CollegeStudent(models.Model):
    _name= 'college.student'
    _inherit = 'mail.thread'
    _description= 'Student records'

    name = fields.Char(string="Name", required=True, tracking=True)
    class_id = fields.Many2one('college.class', tracking=True)
    division = fields.Char(string="Division", tracking=True)
    contact_number= fields.Integer(string="Phone number", tracking=True)
    age=fields.Integer(string="Age", tracking=True)
    notes=fields.Text(string="Notes", tracking=True)
    gender=fields.Selection([('male','Male'),('female','Female'),('others','Others')], string="Gender", tracking=True)
    isIndian=fields.Boolean(string='Is Indian?', required=True, tracking=True)
    Nationality=fields.Char(string="Nationality", required=True,tracking=True)
    capitalized_name=fields.Char(string="Capitalized Name",compute='_compute_capitalized_name',readonly=False, store=True)
    ref=fields.Char(string="Reference",default=lambda self: _('New'))
    teacher_id=fields.Many2one('college.teacher',string="Teacher")
    attendance_ids=fields.One2many('college.attendance','student_id', string='Attendance Records')
    @api.onchange('Nationality')
    def _onchange_nationality(self):
        if self.Nationality=="India":
            self.isIndian=True
        else:
            self.isIndian=False

    @api.depends('name')
    def _compute_capitalized_name(self):
        for rec in self:
            if rec.name:
                 rec.capitalized_name=rec.name.upper()
            else:
                 rec.capitalized_name=''

    @api.constrains('isIndian','Nationality')
    def check_indian_nationality(self):
        for rec in self:
            if rec.isIndian and rec.Nationality=='':
                raise ValidationError(_("Nationality cannot be empty!"))

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['ref'] = self.env['ir.sequence'].next_by_code('college.student')
        return super(CollegeStudent,self).create(vals_list)

