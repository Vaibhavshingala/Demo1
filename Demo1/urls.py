
#from django.contrib import admin
from django.urls import path
from.import view 

#urlpatterns = [
#   path('demo/', admin.site.urls),
#]
urlpatterns = [
    path('', view.homepage),
	path('contact/', view.contact, name='contact'),
	path('services/', view.services, name='services'),
	path('serviceslist/', view.serviceslist),
	path('products/', view.products),
	path('wordc/', view.wordcount, name='wordc'),
	path('count/', view.countword, name='count'),
	path('about/', view.about, name='about'),
	path('address/', view.address, name='address'),
	path('name/', view.name, name='name'),
]
