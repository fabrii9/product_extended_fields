from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    supplier_code = fields.Char(string="Codigo de proveedor", index=True)
    brand = fields.Char(string="Marca")