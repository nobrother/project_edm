# -*- coding: utf-8 -*-

from openerp import models, SUPERUSER_ID

class res_company(models.Model):
    _inherit = "res.company"

    def google_map_img(self, cr, uid, ids, zoom=8, width=298, height=298, key='', context=None):
        partner = self.browse(cr, SUPERUSER_ID, ids[0], context=context).partner_id
        return partner and partner.google_map_img(zoom, width, height, key, context=context) or None