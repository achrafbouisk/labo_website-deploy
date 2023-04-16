from django.contrib import admin
from .models import Accueil, informations, Qui_Somme_Nous, equipe, certificat, AccueilInfo, actualite, Contact
# Register your models here.

admin.site.register(Accueil)
admin.site.register(AccueilInfo)
admin.site.register(informations)
admin.site.register(Qui_Somme_Nous)
admin.site.register(equipe)
admin.site.register(certificat)
admin.site.register(actualite)
admin.site.register(Contact)


admin.site.site_header  =  "Agrilabo admin"  
admin.site.site_title  =  "Agrilabo admin site"
admin.site.index_title  =  "Agrilabo Admin"
