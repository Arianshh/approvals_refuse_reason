from odoo import fields, models


class ApprovalRefuseReason(models.Model):
    _name = 'hr.approval.refuse.reason'

    reason = fields.Char('Reason')
    request_id = fields.Many2one('approval.request')
    approver_id = fields.Many2one('approval.approver')


class ApprovalRequest(models.Model):
    _inherit = 'approval.request'

    refusal_reason_ids = fields.One2many('hr.approval.refuse.reason', 'request_id', string='Refusal Reasons')
