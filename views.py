from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404
import csv
from .models import Facture, Categorie
from .forms import FactureForm, CategorieForm

# Create your views here.
def accueil(request):
    return render(request,'accueil_template.html',{})


#BILLS 
def homepage(request):
    #Retrieve datas stored in the database 
    factures = Facture.objects.all()
    return render(request, 'homepage_template.html',{'factures':factures})


def ajout_facture(request):
    
    if request.method == "POST":
        form = FactureForm(request.POST)
        
         #If form is correct save & redirect to homepage, else we redo the form
        if form.is_valid():
            num_fact = form.cleaned_data['num_fact']
            coordonnees_client = form.cleaned_data['coordonnees_client']
            coordonnes_entreprise = form.cleaned_data['coordonnees_entreprise']
            date = form.cleaned_data['date_facture']
            nom = form.cleaned_data['nom_produit']
            quantite = form.cleaned_data['quantite']
            prix_ht = form.cleaned_data['prix_ht']
            tva = form.cleaned_data['tva']
            prix_ttc = form.cleaned_data['prix_ttc']
            idcat = form.cleaned_data['refid_categorie']
            enreg = Facture (num_fact=num_fact, coordonnees_client=coordonnees_client, coordonnees_entreprise=coordonnes_entreprise,
                            date_facture=date, nom_produit=nom, quantite=quantite, prix_ht=prix_ht, tva=tva, prix_ttc=prix_ttc,
                            refid_categorie=idcat)
            enreg = form.save()
            return HttpResponseRedirect('homepage')
        else : 
            return render(request, 'ajout_template.html',{'form':form}) 
    else:
        form = FactureForm()
        return render(request, 'ajout_template.html',{'form':form}) 


def update_facture(request,num_fact):
    
    #Get the num_fact chosen 
    try :
        data = get_object_or_404(Facture,num_fact = num_fact)
    except Facture.DoesNotExist :
        raise Http404("Facture inexistante")
    
    if request.method == "POST":
        form = FactureForm(request.POST or None, instance = data)

        #If form is correct save & redirect to homepage, else we redo the form
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('homepage')
        else :
            return render(request, 'modify_template.html',{'form':form})
        
    else:
            form = FactureForm(instance = data)
            return render(request, 'modify_template.html',{'form':form})


def delete_facture(request,id):
    
    #Get the num_fact chosen 
    if request.method == "POST":
        data = get_object_or_404(Facture,num_fact = id)
        data.delete()
        return HttpResponseRedirect('/homepage')
    else :
        return render(request, 'delete_template.html', {})



def export_facture(request):

    if request.method == "POST":
        fileformat = request.POST['file']
        bills = Facture.objects.all()

        #Verify if the format chosen == CSV 
        if fileformat == 'CSV':
            reponse = HttpResponse(content_type='text/csv')
            reponse['Content-Disposition'] = 'attachment; filename="factures.csv"'

            #Write on the csv file
            writer = csv.writer(reponse)
            writer.writerow(
                ['num_fact','coordonnees_client','coordonnees_entreprise','date_facture','nom_produit','quantite','prix_ht','tva','prix_ttc','refid_categorie']
            )
            for fact in bills:
                writer.writerow(
                    [fact.num_fact, fact.coordonnees_client, fact.coordonnees_entreprise, fact.date_facture, fact.nom_produit, fact.quantite, 
                    fact.prix_ht, fact.tva, fact.prix_ttc, fact.refid_categorie]
                )
            return reponse
        else:
            return HttpResponse('<strong>Mauvais format !!!</strong>')
    else: 
        return render(request, 'export_template.html',{})


def import_facture(request):

    if request.method == "POST":
        csvfile = request.FILES['csv_file']

        #if the format == .csv then save in the database, if not return a HttpResponse
        if csvfile.name.endswith('.csv'):
            filedata = csvfile.read().decode('utf-8')
            lignes = filedata.split('\n')
            for li in lignes:
                fields = li.split(',')
                data = {}
                data['num_fact'] = fields[0]
                data['coordonnees_client'] = fields[1]
                data['coordonnees_entreprise'] = fields[2]
                data['date_facture'] = fields[3]
                data['nom_produit'] = fields[4]
                data['quantite'] = fields[5]
                data['prix_ht'] = fields[6]
                data['tva'] = fields[7]
                data['prix_ttc'] = fields[8]
                data['refid_categorie'] = fields[9]
                form = FactureForm(data)
                if form.is_valid():
                    form.save()
                    return HttpResponseRedirect('/homepage')
                else:
                    return HttpResponse('Erreur pour télécharger le fichier csv')
        else:
            return HttpResponse('<strong>Le format doit être .csv</strong>')
    else:
        return render(request,'import_template.html',{})





#CATEGORIES 
def homepagecat(request):
    #Retrieve datas stored in the database 
    categories = Categorie.objects.all()
    return render(request, 'homepagecat_template.html', {'categories':categories})


def ajout_categorie(request):

    #Get the id chosen 
    if request.method == "POST":
        form = CategorieForm(request.POST)

         #If form is correct save & redirect to homepage, else we redo the form
        if form.is_valid():
            nom = form.cleaned_data['nom_cat']
            date = form.cleaned_data['date_creation']
            saving = Categorie(nom_cat = nom, date_creation = date)
            saving = form.save()
            return HttpResponseRedirect('/homepagecat/')
        else:
            return render(request, 'ajoutcat_template.html', {'form':form})
    else:
        form = CategorieForm()
        return render(request, 'ajoutcat_template.html',{'form':form})


def update_categorie(request,_id):

    #Get the id chosen 
    try : 
        data = get_object_or_404(Categorie, id_categorie =_id)
    except Categorie.DoesNotExist:
        return HttpResponse('<strong> La catégorie est inexistant, veuillez la créer svp </strong>')
    
    if request.method == "POST":
        form = CategorieForm(request.POST or None, instance = data)

         #If form is correct save & redirect to homepage, else we redo the form
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/homepagecat/')
        else:
            return render(request, 'modifycat_template.html')
    else:
        form = CategorieForm()
        return render(request,'modifycat_template.html',{'form':form})


def delete_categorie(request, id_):
    
    #Get the id chosen 
    if request.method == "POST":
        data = get_object_or_404(Categorie, id_categorie = id_)
        data.delete()
        return HttpResponseRedirect('/homepagecat/')
    else:
        return render(request, 'deletecat_template.html',{})



