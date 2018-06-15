# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import api, exceptions, fields, models, _


class ActivityDefinition(models.Model):
    _inherit = 'workflow.activity.definition'

    workflow_activity_type_id = fields.Many2one(
        'mail.activity.type', domain=[]
    )
    activity_note = fields.Text()
    model = fields.Char(
        related='model_id.model',
        readonly=True,
    )

    def _get_activity_values(self, vals, parent=False, plan=False, action=False
                             ):
        values = super()._get_activity_values(vals, parent, plan, action)
        if self.model_id.model == 'mail.activity':
            values.update({
                'activity_type_id': self.workflow_activity_type_id.id,
                'name': self.name,
                'note': self.activity_note
            })
        return values
