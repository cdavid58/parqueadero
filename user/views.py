from django.http import HttpResponse
from django.shortcuts import render,redirect
from operations import Operations_User


def Login(request):
	if 'verifi' in request.session:
		if Operations_User().Login(request.session['user_name'], request.session['psswd'])['result']:
			return redirect('ListRegister')	
	if request.is_ajax():
		p_l = Operations_User().Login(request.GET['user_name'], request.GET['psswd'])
		if p_l['result']:
			request.session['user_name'] = request.GET['user_name']
			request.session['psswd'] = request.GET['psswd']
			request.session['parking_lot'] = p_l['parking_lot']
			request.session['type_user'] = p_l['type_user']
		print(p_l['result'])
		return HttpResponse(p_l['result'])

	return render(request,'login.html')

def Index(request):
	request.session['verifi'] = True
	return redirect('ListRegister')

def Add_User(request):
	if request.is_ajax():
		return HttpResponse(Operations_User().Create_User(request.GET,request.session['parking_lot']))
	return render(request,'user/add.html')

def List_User(request):
	return render(request,'user/list_user.html',{'list_user':Operations_User().List_User()})

def LogOut(request):
	del request.session['verifi']
	return redirect('/')

def Edit_User(request,pk):
	if request.is_ajax():
		request.session['user_name'] = request.GET['user_name']
		request.session['psswd'] = request.GET['psswd']
		request.session['type_user'] = request.GET['type_user']
		return HttpResponse(Operations_User().Edit_User(request.GET,pk))
	return render(request,'user/edit.html',{'user':Operations_User().Get_User(pk)})

def Delete_User(request):
	if request.is_ajax():
		return HttpResponse(Operations_User().Delete_User(request.GET['pk']))
