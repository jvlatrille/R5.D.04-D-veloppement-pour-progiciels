from odoo import models, fields

class Notice(models.Model):
    _name = "library.notice"
    _description = "Avis sur un livre"

    book_id = fields.Many2one("library.book", string="Livre")
    text = fields.Char("Texte")
    note = fields.Integer("Note")
    state = fields.Selection([
        ('draft', 'Brouillon'),
        ('accepted', 'Accepté'),
        ('rejected', 'Rejeté'),
    ], default='draft', string="État")
