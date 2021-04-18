# -*- coding: utf-8 -*-
from odoo import http


class OsmInventoryQr(http.Controller):

    @http.route('/inventory/qr/', auth='public', website=True)
    def index2(self, **kw):
        picking_id = kw.get('picking_id')
        id = kw.get('id')
        data = http.request.env['stock.picking'].search([('id','=', picking_id)])
        return http.request.render('osm__inventory_qr.qr_page', {
            'root': '/osm__inventory_qr/osm__inventory_qr',
            'docs': data,
            'move_id': id
        })

