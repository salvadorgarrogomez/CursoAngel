from odoo import fields,api,models


class CrmTicket(models.Model):
    _name = 'crm.ticket'
    _inherits = {'crm.lead': 'lead_id'}
    _description = 'CRM Ticket'

    lead_id = fields.Many2one(
        comodel_name='crm.lead',
        string='Lead',
        required=True,
        ondelete='cascade',
    )

    actions_todo = fields.Html()

    def action_set_won_rainbowman(self):
        self.ensure_one()
        self.lead_id.action_set_won_rainbowman()
