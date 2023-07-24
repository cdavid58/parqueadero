from django.conf.urls import url
from .views import *

urlpatterns=[
	url(r'^ListRegister/$',ListRegister,name="ListRegister"),
	url(r'^Elimina/$',Elimina,name="Elimina"),
	url(r'^Print_Ticket/(\w+)/$',Print_Ticket,name="Print_Ticket"),
	url(r'^Print_Ticket_Exit/(\w+)/$',Print_Ticket_Exit,name="Print_Ticket_Exit"),
	url(r'^History/$',History,name="History"),
]