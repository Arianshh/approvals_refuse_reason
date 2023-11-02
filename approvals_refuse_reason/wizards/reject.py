from odoo import fields, models


class RejectionReasonWizard(models.TransientModel):
    _name = 'hr.approval.refuse'
    _description = "Approval Rejection wizard"

    reason = fields.Char(string="Reason", required=True)

    def action_refuse(self):
        active_obj = self.env[self.env.context.get('active_model')].browse(
            self.env.context.get('active_id'))
        approver = active_obj.approver_ids.filtered(lambda x: x.user_id.id == self.env.uid)
        approver.write({
            'refusal_reason': self.reason})
        approver.action_refuse()
        return True
