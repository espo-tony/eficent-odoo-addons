# -*- coding: utf-8 -*-
# © 2015 Eficent Business and IT Consulting Services S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

{
    "name": "Procurement Project",
    "version": "9.0.1.0.0",
    "author": "Eficent Business and IT Consulting Services S.L., "
              "Odoo Community Association (OCA)",
    "website": "https://www.odoo-community.org",
    "category": "Purchase Management",
    "depends": ["procurement_analytic", "project"],
    "data": [
        "views/procurement_view.xml",
        "views/project_project_view.xml",
    ],
    'installable': False,
}
