from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate , login , logout
# Create your views here.
def index(request):
	if request.user.is_authenticated:
		return render(request, "authentication/index.html")
	return render(request, "authentication/login.html")

def signin(request):
	if request.method == "POST":
		username = request.POST["username"] 
		password = request.POST["password"] 
		user = authenticate(request, username=username , password=password)
		if user is not None:
			login(request, user)
			return HttpResponseRedirect(reverse("index"))
		else:
			return render(request, "authentication/login.html",{
			"message": "Invalid Credentials"
		})	
	return render(request, "authentication/login.html")	

def signout(request):
	logout(request)
	return render(request, "authentication/login.html",{
		"message": "Successfully Logged Out"
		})	