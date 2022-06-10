from django.shortcuts import render

from django.http import HttpResponse

projectslist = [
{
    'id': '1',
    'Project_Name' : 'e-commerce website',
    'Description' : 'This is the e-ecommerece wesite and makerting place to sell and buy products in online',
    'TopRated' :True
},
{
    'id' : '2',
    'Project_Name' : 'My Profile ',
    'Description' : 'A personal Website explain about the me and writing articles , blogs e.t.c',
    'TopRated' : False
},
{
    'id' : '3',
    'Project_Name' : 'Social Web app/ Website',
    'Description' : 'A website that done by social networking the people and connecting share ideas and views',
    'TopRated'    : True
}
]
    



def Projects(request):
    context = {'projects' :projectslist}
    return render(request,'projectweb/projectweb.html',context)

def Project(request,pk):
    projectObject = None

    for i in projectslist:
        if i['id'] == str(pk):
            projectObject = i
    return render(request,'projectweb/singlepage.html',{'project':projectObject})

def englishpage(request):
    name = "Ranga"
    age = 26
    context = {'name':name,'age':age}
    return render(request,'projectweb/englishphrases.html',context)

# Create your views here.
