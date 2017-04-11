# -*- coding: utf-8 -*-

import urllib
from openerp import models

class res_partner(models.Model):
    _inherit = "res.partner"

    def google_map_img(self, cr, uid, ids, zoom=8, width=298, height=298, key='', context=None):
        url = super(res_partner, self).google_map_img(
            cr, uid, ids, zoom, width, height, context).replace(
            'center=', 'markers=')
        return "%s&%s" % (url, urllib.urlencode({ 'key': key }))