# -*- coding: utf-8 -*-
# from odoo import http


# class Itaiji(http.Controller):
#     @http.route('/itaiji/itaiji', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/itaiji/itaiji/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('itaiji.listing', {
#             'root': '/itaiji/itaiji',
#             'objects': http.request.env['itaiji.itaiji'].search([]),
#         })

#     @http.route('/itaiji/itaiji/objects/<model("itaiji.itaiji"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('itaiji.object', {
#             'object': obj
#         })
