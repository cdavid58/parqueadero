from django.http import HttpResponse
from django.shortcuts import render
from operations import Operations_User


def Login(request):
	if request.is_ajax():
		return HttpResponse(Operations_User().Login(request.GET['user_name'], request.GET['psswd']))
	return render(request,'login.html')

def Index(request):
	return render(request,'index.html')