from odoo import models, fields

class Notice(models.Model):
    _name = "library.notice"
    _description = "Avis sur les livres"

    text = fields.Html("Avis")
    note = fields.Integer("Note", required=True)
    book_id = fields.Many2one("library.book", string="Livre concerné", ondelete="cascade")
