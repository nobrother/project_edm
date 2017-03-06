# -*- coding: utf-8 -*
from openerp import http, _
from openerp.http import request
from openerp.addons.website_sale.controllers.main import website_sale

import collections

class WebsiteSale(website_sale):

    order_by = {
        'anew': {'query': 'is_new DESC, id DESC', 'display_name': _('New'), 'code': 'anew'},
        'aold': {'query': 'is_new ASC, id ASC', 'display_name': _('Old'), 'code': 'aold'},
        'natoz': {'query': 'name ASC', 'display_name': _('Name : A to Z'), 'code': 'natoz'},
        'nztoa': {'query': 'name desc', 'display_name': _('Name : Z to A'), 'code': 'nztoa'},
        'phtl': {'query': 'list_price DESC, id DESC', 'display_name': _('Price : High to Low'), 'code': 'phtl'},
        'plth': {'query': 'list_price ASC, id DESC', 'display_name': _('Price : Low to High'), 'code': 'plth'},
    }
    order_by = collections.OrderedDict(sorted(order_by.items()))

    def _get_search_order(self, post):
        """ Bug fix the order query """
        return 'website_published desc, %s' % \
               self.order_by.get(post.get('order', ''), { 'query': 'website_sequence desc' })['query']

    @http.route()
    def shop(self, page=0, category=None, search='', ppg=False, **post):

        res = super(WebsiteSale, self).shop(page=page, category=category, search=search,
                                             ppg=ppg, **post)

        url = request.httprequest.__dict__['environ'].get('PATH_INFO', '/shop')
        keep = request.context.get('keep', False)
        if keep:
            keep.path = url

            # Remove '?category' query
            if keep.args['category']:
                del keep.args['category']


        return res

