# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

{
    'name': 'Medical Workflow',
    'summary': 'Medical workflow base',
    'version': '11.0.1.0.0',
    'author': 'Creu Blanca, Eficent, Odoo Community Association (OCA)',
    'category': 'Medical',
    'website': 'https://github.com/OCA/vertical-medical',
    'license': 'LGPL-3',
    'depends': [
        'product'
    ],
    'data': [
        'data/ir_sequence.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/workflow_menu.xml',
        'views/workflow_activity_definition.xml',
        'views/workflow_plan_definition.xml',
        'views/workflow_plan_definition_action.xml',
        'views/workflow_type.xml',
    ],
    'demo': [
        'demo/workflow_demo.xml'
    ],
    'application': False,
    'installable': True,
    'auto_install': False,
}
