from django.shortcuts import render

from django.http import HttpResponse

projectslist = [
{
 'id': '1',
    'Project Name' : 'e-commerce website',
    'Descripition' : 'This is the e-ecommerece wesite and makerting place to sell and buy products in online'

},
{
    'id' : '2',
    'Project Name' : 'My Profile ',
    'Description' : 'A personal Website explain about the me and writing articles , blogs e.t.c'
},
{
    'id' : '3',
    'Project Name' : 'Social Web app/ Website',
    'Description' : 'A website that done by social networking the people and connecting share ideas and views'
}
]
    



def Projects(request):
    return render(request,'projectweb/projectweb.html')

def Project(request,pk):
    return render(request,'projectweb/singlepage.html')

def englishpage(request):
    name = "Ranga"
    age = 26
    context = {'name':name,'age':age}
    return render(request,'projectweb/englishphrases.html',context)

# Create your views here.
