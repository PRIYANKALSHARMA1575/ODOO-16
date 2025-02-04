from odoo import api, models, fields, _
from odoo.exceptions import ValidationError

class CollegeTeacher(models.Model):
    _name= 'college.teacher'
    _inherit = 'mail.thread'
    _description= 'Teacher records'
    _ref_name = 'ref'

    name = fields.Char(string="Name", required=True, tracking=True)
    contact_number= fields.Integer(string="Phone number", tracking=True)
    age=fields.Integer(string="Age", tracking=True)
    notes=fields.Text(string="Notes", tracking=True)
    gender=fields.Selection([('male','Male'),('female','Female'),('others','Others')], string="Gender", tracking=True)
    isIndian=fields.Boolean(string='Is Indian?', required=True, tracking=True)
    Nationality=fields.Char(string="Nationality", required=True,tracking=True)
    capitalized_name=fields.Char(string="Capitalized Name",compute='_compute_capitalized_name',readonly=False, store=True)
    ref=fields.Char(string="Reference",default=lambda self: _('New'))
    subject=fields.Char(string="Subject",tracking=True)
    students=fields.One2many('college.attendance','teacher_id',string="Students")
    attendance_ids=fields.One2many('college.attendance','teacher_id', string="Attendance Records")
    def name_get(self):
        res=[]
        for rec in self:
            name=f'{rec.ref} - {rec.name}'
            res.append(( rec.id,name))
        return res

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
        if isinstance(vals_list, dict):
            vals_list = [vals_list]
        for vals in vals_list:
            if not vals.get('ref') or vals['ref'] == 'New':
                vals['ref'] = self.env['ir.sequence'].next_by_code('college.teacher') or _('New')

        return super(CollegeTeacher,self).create(vals_list)

