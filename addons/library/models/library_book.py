# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class LibraryBook(models.Model):
    _inherit = 'library.book'

    notice_ids = fields.One2many(
        "library.notice",
        "book_id",
        string="Avis",
        domain=[('state', '=', 'accepted')]
    )

    language_ids = fields.Many2many(
        "library.language",
        string="Langues disponibles"
    )

    previous_book_id = fields.Many2one(
        "library.book",
        string="Livre précédent"
    )

    next_book_ids = fields.One2many(
        "library.book",
        "previous_book_id",
        string="Suites"
    )

    notice_count = fields.Integer(
        compute="_compute_notice_count",
        string="Nombre d'avis"
    )

    state = fields.Selection([
        ('negociation', 'En négociation'),
        ('writing', 'En écriture'),
        ('printing', 'En impression'),
        ('published', 'Publié'),
    ], default='negociation', string="État", group_expand='_expand_states')

    @api.model
    def _expand_states(self, states, domain, order=None):
        """Return all states for grouping in kanban/list views."""
        return [s[0] for s in self._fields['state'].selection]


    @api.depends('notice_ids')
    def _compute_notice_count(self):
        for book in self:
            book.notice_count = len(book.notice_ids)

    @api.constrains("isbn")
    def _check_isbn_auto(self):
        for book in self:
            if not book.isbn:
                continue

            digits = [int(x) for x in book.isbn if x.isdigit()]
            if len(digits) != 13:
                raise ValidationError("ISBN invalide : doit contenir 13 chiffres.")

            total = 0
            for i, d in enumerate(digits[:12]):
                total += d if i % 2 == 0 else d * 3

            reste = total % 10
            cle = 0 if reste == 0 else 10 - reste

            if cle != digits[-1]:
                raise ValidationError("ISBN invalide.")


    def action_publish(self):
        for book in self:
            book.state = 'published'

