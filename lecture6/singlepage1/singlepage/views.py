from django.shortcuts import render
from django.http import Http404 , HttpResponse

# Create your views here.
def index(request):
	return render(request, "singlepage/index.html")

data = ["This Is The First Page","This Is The Second Page","This Is The Third Page"]	

def section(request , num):
	if 1 <= num <= 3:
		return HttpResponse(data[num-1])
	else:
		raise Http404("No Such Section")	