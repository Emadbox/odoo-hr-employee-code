from odoo import fields, models


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    employee_code = fields.Char()
