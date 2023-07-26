from django.http import HttpResponse
from django.shortcuts import render
from operations import Operation

def ListRegister(request):
	if request.is_ajax():
		data = request.GET
		print("Entre")
		result = Operation().Operations_Schedule(data['plate'],data['helmet'],data['note'],request.session['user_name'])
		return HttpResponse(True)
	return render(request,'request/register.html',{'data':Operation().Get_List_Schedule()})

def Elimina(request):
	if request.is_ajax():
		data = request.GET
		result = Operation().Operations_Schedule(data['plate'],data['helmet'],data['note'],request.session['user_name'])
		return HttpResponse(True)

def Print_Ticket(request,pk):
	return render(request,'ticket.html',{'information':Operation().Get_Last_Record(pk)})

def Print_Ticket_Exit(request,pk):
	return render(request,'ticket_exit.html',{'information':Operation().Get_Last_Record(pk)})


def History(request):
	return render(request,'request/history.html',{'data':Operation().Get_History()})

