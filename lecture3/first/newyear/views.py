from django.shortcuts import render
import datetime
# Create your views here.
def index(request):
	now = datetime.datetime.now()
	return render(request, "newyear/newyear.html", {
		"newyear": now.month == 1 and mow.day == 1
		})