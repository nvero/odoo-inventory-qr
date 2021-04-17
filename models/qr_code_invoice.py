# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.http import request
from odoo.addons.osm__inventory_qr.models.qr_code_base import generate_qr_code
 

class QRCodeInvoice(models.Model):
    _inherit = 'stock.picking'

    qr_image = fields.Binary("QR Code", compute='_generate_qr_code')
    qr_in_report = fields.Boolean('Show QR in Report')

    def _generate_qr_code(self):
        base_url = request.env['ir.config_parameter'].get_param('web.base.url')
        base_url += '/inventory/qr/?id=%s' % (self.id,)
        self.qr_image = generate_qr_code(base_url)


