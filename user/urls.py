from django.conf.urls import url
from .views import *

urlpatterns=[
	url(r'^$',Login,name="Login"),
	url(r'^Index/$',Index,name="Index"),
	url(r'^List_User/$',List_User,name="List_User"),
	url(r'^Add_User/$',Add_User,name="Add_User"),
	url(r'^LogOut/$',LogOut,name="LogOut"),
	url(r'^Edit_User/(\d+)/$',Edit_User,name="Edit_User"),
	url(r'^Delete_User/$',Delete_User,name="Delete_User"),
]