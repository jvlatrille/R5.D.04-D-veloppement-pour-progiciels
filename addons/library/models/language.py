from odoo import models, fields

class Language(models.Model):
    _name = "library.language"
    _description = "Langue de traduction"

    name = fields.Char("Langue", required=True)
    flag = fields.Binary("Drapeau")
    book_ids = fields.Many2many("library.book", string="Livres disponibles")
