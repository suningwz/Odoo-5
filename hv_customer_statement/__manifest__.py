# -*- encoding: utf-8 -*-
##############################################################################
#
#    odoo, Open Source Management Solution
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>). All Rights Reserved
#    $Id$
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


{
    'name': 'Customer Statement',
    'version': '1.0.1',
    'category': 'Customer Statement',
    'summary': 'Customer Statement',
    'description': "",
    'author': "Havi Technology",
    'website': "havi.com.au",
    'depends': [
        'account',
        'hv_message'
    ],
    'data': [
        'security/ir.model.access.csv',
        'security/cust_statement_security.xml',
        'data/email_template_view.xml',
        'views/custom_data.xml',
    ],
    'installable': True,
}
