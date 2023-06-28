import pandas as pd
from odoo import models, fields, api

class SalesImport(models.TransientModel):
    _name = 'sales.import'

    file = fields.Binary('Excel File', required=True)

    def import_sales(self):
        df = pd.read_excel(file, sheet_name='Sheet1')  # Assurez-vous que le nom de la feuille correspond à votre fichier Excel

        for _, row in df.iterrows():
            sale_values = {
                'name': row['Order Number'],  # Remplacez 'Order Number' par le nom de la colonne correspondant au numéro de commande
                'partner_id': row['Customer ID'],  # Remplacez 'Customer ID' par le nom de la colonne correspondant à l'ID client
                # Ajoutez d'autres champs selon vos besoins
            }

            sale = self.env['sale.order'].create(sale_values)

            # Vous pouvez également ajouter des lignes de commande, des taxes, etc., en fonction de votre fichier Excel

        # Après l'import, vous pouvez effectuer d'autres actions ou afficher un message de réussite
        # Exemple : return {'type': 'ir.actions.act_window_close'}

