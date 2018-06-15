# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import api, exceptions, fields, models, _


class ActivityDefinition(models.Model):
    _name = 'workflow.activity.definition'
    _description = 'Activity Definition'
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
        string='Workflow Type',
        comodel_name='workflow.type',
        ondelete='restrict', index=True, required=True,
        help="Type of worklow this activity definition can be used in",
    )
    model_ids = fields.Many2many(
        comodel_name='ir.model',
        related='type_id.model_ids'
    )
    model_id = fields.Many2one(
        string='Model',
        comodel_name='ir.model',
        required=True,
        domain="[('id', 'in', model_ids)]"
    )
    model = fields.Char(
        related='model_id.model',
        readonly=True,
    )
    state = fields.Selection(
        [('draft', 'Draft'),
         ('active', 'Active'),
         ('retired', 'Retired'),
         ('unknown', 'Unknown')],
        required=True,
        default='draft',
    )
    service_id = fields.Many2one(
        string='Resource Product',
        comodel_name='product.product',
        help='Product that represents this resource',
        required=False,
        ondelete='restrict', index=True,
    )
    quantity = fields.Integer(
        string='Quantity',
        help='How much to realize',
        default=1,
    )
    action_ids = fields.One2many(
        string='Subsequent actions',
        comodel_name='workflow.plan.definition.action',
        inverse_name='activity_definition_id',
        readonly=True,
    )

    @api.constrains('type_id')
    def _check_type_id(self):
        for rec in self:
            if rec.action_ids:
                raise exceptions.UserError(
                    _('Type cannot be modified if the record has relations'))

    @api.onchange('type_id')
    def _onchange_type_id(self):
        self.model_id = False
        return {
            'domain': {
                'model_id': [('id', 'in', self.type_id.model_ids.ids)],
            },
        }

    def _get_activity_values(self, vals, parent=False, plan=False, action=False
                             ):
        values = vals.copy()
        return values

    @api.multi
    def execute_activity(self, vals, parent=False, plan=False, action=False):
        self.ensure_one()
        values = self._get_activity_values(vals, parent, plan, action)
        model_obj = self.env[self.model_id.model]
        ids = []
        for i in range(0, self.quantity):
            ids.append(model_obj.create(values).id)
        return model_obj.browse(ids)
