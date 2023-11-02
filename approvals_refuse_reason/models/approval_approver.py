from odoo import fields, models


class ApprovalApprover(models.Model):
    _inherit = 'approval.approver'

    refusal_reason = fields.Text('Refusal Reason')

    def action_refuse(self):
        self.env['hr.approval.refuse.reason'].create(
            {'request_id': self.request_id.id, 'reason': self.refusal_reason, 'approver_id': self.id})
        super(ApprovalApprover, self).action_refuse()
