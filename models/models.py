# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class osm__inventory_qr(models.Model):
#     _name = 'osm__inventory_qr.osm__inventory_qr'
#     _description = 'osm__inventory_qr.osm__inventory_qr'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
