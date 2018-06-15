# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class PlanDefinition(models.Model):
    _name = 'workflow.plan.definition'
    _description = 'Plan Definition'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(
        string='Name',
        help='Human-friendly name for the Plan Definition',
        required=True,
    )
    description = fields.Text(
        string='Description',
        help='Summary of nature of plan',
    )
    type_id = fields.Many2one(
        string='Workflow type',
        comodel_name='workflow.type',
        ondelete='restrict', index=True,
        required=True,
    )
    state = fields.Selection(
        [('draft', 'Draft'),
         ('active', 'Active'),
         ('retired', 'Retired'),
         ('unknown', 'Unknown')],
        required=True,
        default='draft',
    )
    direct_action_ids = fields.One2many(
        string='Parent actions',
        comodel_name='workflow.plan.definition.action',
        inverse_name='direct_plan_definition_id',
    )
    activity_definition_id = fields.Many2one(
        string='Activity definition',
        comodel_name='workflow.activity.definition',
        description='Main action',
    )
    action_ids = fields.One2many(
        string='All actions',
        comodel_name='workflow.plan.definition.action',
        inverse_name='plan_definition_id',
        readonly=True,
    )

    @api.multi
    def _check_plan_recursion(self, plan_ids):
        self.ensure_one()
        if self.id in plan_ids:
            raise UserError(_(
                'Error! You are attempting to create a recursive definition'))
        plan_ids.append(self.id)
        for action in self.action_ids:
            if action.execute_plan_definition_id:
                action.execute_plan_definition_id._check_plan_recursion(
                    plan_ids
                )

    @api.multi
    def execute_plan_definition(self, vals, parent=False):
        """It will return the parent or the main activity.
        The action result could be of different models.
        """
        self.ensure_one()
        result = parent
        for action in self.direct_action_ids:
            act = action.execute_action(vals, parent)
            result = result or act
        return result
