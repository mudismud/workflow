from odoo import api, fields, models


class WizardResPartnerWorkflow(models.Model):
    _name = 'wizard.res.partner.workflow'

    @api.model
    def _default_type(self):
        return self.env.ref(self.env.context.get('type_ref'))

    partner_id = fields.Many2one('res.partner', required=True)
    type_id = fields.Many2one(
        'workflow.type', required=True, default=_default_type)
    plan_definition_id = fields.Many2one(
        'workflow.plan.definition',
        required=True,
        domain="[('type_id','=', type_id)]"
    )

    def _get_values(self):
        return {
            'res_model_id': self.env['ir.model'].search(
                [('model', '=', 'res.partner')]).id,
            'res_id': self.partner_id.id,
        }

    @api.multi
    def run(self):
        self.ensure_one()
        return self.plan_definition_id.execute_plan_definition(
            self._get_values())
