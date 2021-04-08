from django.urls import path
from . import views

urlpatterns = [
    path('accueil',views.accueil, name='accueil'),
    path('homepage',views.homepage, name='home'),
    path('add',views.ajout_facture, name='add'),
    path('<str:num_fact>',views.update_facture, name='update'),
    path('delete/<str:id>',views.delete_facture, name='delete'),
    path('export/',views.export_facture, name='export'),
    path('import/',views.import_facture, name='import'),
    path('homepagecat/',views.homepagecat, name='homepagecat'),
    path('addcat/',views.ajout_categorie, name='addcat'),
    path('updatecat/<str:_id>',views.update_categorie, name='updatecat'),
    path('deletecat/<str:id_>',views.delete_categorie, name='deletecat')
]