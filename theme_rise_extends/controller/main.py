# -*- coding: utf-8 -*
from openerp import _
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

