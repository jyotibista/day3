from django.shortcuts import render
from django.http import HttpResponse
import requests
import bs4

# Create your views here.
def home(request):
#    # return HttpResponse('Hello world')
#    names = ['jyoti','dixhya','anu','anuj']
#    d = {
#        'name' : names,
#        'college' : 'mbm'
#    }

    page = requests.get('https://fabpedigree.com/james/mathmen.htm')
    soup = bs4.BeautifulSoup(page.content,'html.parser')
    namelist = [ ]
    for names in soup.findAll('a'):

       if names.parent.name == ('li'):


           namelist.append(names.text)
    d= {
        'names': namelist
    }
    return render(request,'home.html',d)

def bootcamp(request):
    return HttpResponse('<h1> Hello bootcamp </h1>')