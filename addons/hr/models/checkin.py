from odoo import fields, models

class CheckIn(models.Model):
    _name = "hr.checkin"
    _description = "Check in status of each employees"

    checkin_status = fields.Boolean("Check-In Status", default=True)

    time_checkin = fields.Datetime("Time Check-In",required=True)

    employee_id = fields.Many2one(comodel_name="hr.employee","user_id",string="Employee ID")
    employee_name = fields.Char("Name")