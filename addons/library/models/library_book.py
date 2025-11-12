# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Book(models.Model):
    _name = 'library.book'
    _description = 'Les livres de la bibliothèque'

    name = fields.Char("Title", required=True)
    isbn = fields.Char("ISBN")
    active = fields.Boolean("Actif ?", default=True)
    date_published = fields.Date("Date published")
    image = fields.Binary("Cover")

    # --------------------------------------------------------
    # Bouton : Vérifier la validité du code ISBN
    # --------------------------------------------------------
    def button_check_isbn(self):
        for book in self:
            if not book.isbn:
                raise ValidationError("Le code ISBN est vide.")
            digits = [int(x) for x in str(book.isbn) if x.isdigit()]
            if len(digits) != 13:
                raise ValidationError("ISBN invalide (doit contenir 13 chiffres).")

            total = 0
            for index, digit in enumerate(digits[:12]):
                total += digit if (index % 2) == 0 else digit * 3

            reste = total % 10
            cle_theorique = 0 if reste == 0 else 10 - reste
            if cle_theorique != digits[-1]:
                raise ValidationError("ISBN invalide.")
        return True
