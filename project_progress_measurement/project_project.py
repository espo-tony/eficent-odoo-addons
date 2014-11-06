# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2014 Eficent (<http://www.eficent.com/>)
#              <contact@eficent.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from osv import fields, osv


class project(osv.osv):

    _inherit = "project.project"

    _columns = {
        'progress_measurements': fields.one2many('project.progress.measurement',
                                                 'project_id',
                                                 'Measurements'),
    }

    def copy(self, cr, uid, id, default=None, context=None):

        if context is None:
            context = {}
        if default is None:
            default = {}

        default['progress_measurements'] = []

        return super(project, self).copy(cr, uid, id, default=default, context=context)

project()