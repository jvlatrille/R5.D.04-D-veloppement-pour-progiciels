from odoo import models, fields, api

class Book(models.Model):
    _inherit = "library.book"

    notice_ids = fields.One2many("library.notice", "book_id", string="Avis")
    language_ids = fields.Many2many("library.language", string="Langues disponibles")

    previous_book_id = fields.Many2one("library.book", string="Livre précédent")
    next_book_ids = fields.One2many("library.book", "previous_book_id", string="Suites")

    notice_count = fields.Integer(compute="_compute_notice_count", string="Nombre d'avis")

    @api.depends("notice_ids")
    def _compute_notice_count(self):
        for book in self:
            book.notice_count = len(book.notice_ids)
