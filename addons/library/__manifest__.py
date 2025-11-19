# -*- coding: utf-8 -*-
{
    'name': "Library",
    'summary': "Application de gestion de bibliothèque",
    'description': """
Application de gestion de bibliothèque.
    """,
    'author': "My Company",
    'website': "https://www.yourcompany.com",
    'category': 'Services/Library',
    'version': '18.0.1.0.0',
    'depends': ['base'],
    'application': True,
    'license': 'AGPL-3',
    'data': [
        'security/library_security.xml',
        'security/ir.model.access.csv',
        'views/library_menu.xml',
        'views/book_views.xml',
        'views/language_views.xml',
        'views/notice_views.xml',
        'views/book_kanban.xml',
        'views/language_kanban.xml',
    ],
    'demo': [
        'demo/demo.xml',
        'demo/library.book.csv',
        'demo/library.notice.csv',
    ],
}
