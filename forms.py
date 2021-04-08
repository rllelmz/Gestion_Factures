from django import forms

from Factures.models import Categorie, Facture


class FactureForm(forms.ModelForm):
    class Meta : 
        model = Facture
        fields = ['num_fact','coordonnees_client','coordonnees_entreprise','date_facture','nom_produit','quantite',
                  'prix_ht','tva','prix_ttc','refid_categorie']

class CategorieForm(forms.ModelForm):
    class Meta :
        model = Categorie
        fields = ['nom_cat','date_creation']
