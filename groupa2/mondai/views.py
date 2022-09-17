from django.shortcuts import render

# Create your views here.
def mondaiListView(request):
	return render(request, "mondai/mondai-list.html")
