# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

{
    'name': 'Workflow in Activity Mail',
    'summary': 'Workflow Activity',
    'version': '11.0.1.0.0',
    'author': 'Creu Blanca, Eficent, Odoo Community Association (OCA)',
    'category': 'Medical',
    'website': 'https://github.com/OCA/vertical-medical',
    'license': 'LGPL-3',
    'depends': [
        'workflow_base',
        'mail',
    ],
    'data': [
        'data/workflow_type.xml',
        'wizard/wizard_res_partner_workflow.xml',
        'views/workflow_activity_definition.xml',
        'views/res_partner_views.xml',
    ],
    'demo': [
        'demo/workflow_demo.xml'
    ],
    'application': False,
    'installable': True,
    'auto_install': False,
}
