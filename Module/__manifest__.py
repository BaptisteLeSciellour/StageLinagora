{
    'name': 'Module Transition',
    'version': '1.0',
    'summary': 'Module personnalisé pour l importation des ventes',
    'description': """
        Module personnalisé pour importer les ventes à partir d'une feuille Excel dans le module Vente d'Odoo.
    """,
    'category': 'Sales',
    'author': 'Le Sciellour',
    'depends': ['sale'],
    'data': [
        'views/sales_import_view.xml',
    ],
    'demo': [],
    'installable': True,
    'application': False,
}