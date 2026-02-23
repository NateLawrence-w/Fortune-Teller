from django.shortcuts import render

# Create your views here.
def  fortune(request):
    return render(request, 'fortunes/fortune.html')