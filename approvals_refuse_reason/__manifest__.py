# Copyright 2023 Arian Shariat <arian.shariat@gmail.com>
# License LGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Approval Refusal Reason",
    "author": "Arian Shariat",
    "support": "arian.shariat@gmail.com",
    "version": "15.0",
    "license": "LGPL-3",
    "category": "Human Resources/Approvals",
    "website": "https://github.com/Arianshh",
    "summary": "Adds reason to refuse process.",
    "depends": ['approvals'],
    'images': ['static/description/header.png'],
    "data": ['security/ir.model.access.csv',
             'wizards/reject_wizard.xml',
             'views/approval_request_views.xml', ],
    "installable": True,
    "application": True,
}
