from django.db import models

# Create your models here.
class Facture(models.Model):
    num_fact = models.CharField(primary_key=True, max_length=25)
    coordonnees_client = models.CharField(max_length=150)
    coordonnees_entreprise = models.CharField(max_length=150)
    date_facture = models.DateField()
    nom_produit = models.CharField(max_length=50)
    quantite = models.IntegerField()
    prix_ht = models.FloatField()
    tva = models.FloatField()
    prix_ttc = models.FloatField()
    refid_categorie = models.ForeignKey('Categorie', models.DO_NOTHING, db_column='RefId_categorie')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Facture'


class Categorie(models.Model):
    id_categorie = models.AutoField(db_column='Id_categorie', primary_key=True)  # Field name made lowercase.
    nom_cat = models.CharField(max_length=50)
    date_creation = models.DateField()

    class Meta:
        managed = False
        db_table = 'Categorie'