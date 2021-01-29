# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductTemplate(models.Model):

    _inherit = 'product.template'

     price_2 = fields.monetary(string="Precio 2")


