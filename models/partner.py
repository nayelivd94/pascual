## -*- coding: utf-8 -*-

from openerp import models, fields, api, _, tools
from openerp.exceptions import UserError, RedirectWarning, ValidationError
import xlrd
import shutil
import logging
_logger = logging.getLogger(__name__)
class ResPartner(models.Model):
    _inherit="res.partner"
    phone = fields.Char(string="Telefono", required=True)
    vat = fields.Char(string='RFC', help="Tax Identification Number. "
                                         "Fill it if the company is subjected to taxes. "
                                         "Used by the some of the legal statements.", required=True)

    @api.model
    def create(self, vals):
        child_id = []
        if 'child_ids' in vals:
            vals['type'] = 'contact';
            print(vals)
            child_id.append(vals['child_ids'])
            if len(child_id[0]) == 0:
                raise UserError('Es necesar dar de alta una  Dirección de Entrega')
        return super(ResPartner, self).create(vals)
